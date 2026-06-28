import os
import anthropic
from typing import List

# Configuration
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
PROMPT_DIR = "prompts"
OUTPUT_DIR = "examples/generated_variants"

def read_prompt(file_name: str) -> str:
    """Read a prompt file and return its content."""
    file_path = os.path.join(PROMPT_DIR, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def generate_variants(prompt: str, num_variants: int = 10) -> List[str]:
    """
    Generate N variants of copy using Claude.
    Batch request — 1 API call, not N calls.
    """
    if not API_KEY:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY environment variable is not set."
        )

    client = anthropic.Anthropic(api_key=API_KEY)

    batch_prompt = f"""
    {prompt}

    ---

    Using the prompt and structure above, generate {num_variants} distinct DM sequence variants.
    Number each variant clearly (Variant 1, Variant 2, etc.).
    Vary the hooks, angles, and wording between each.
    """

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        temperature=0.8,
        messages=[{"role": "user", "content": batch_prompt}]
    )

    # Split response into individual variants
    raw_text = message.content[0].text
    variants = [v.strip() for v in raw_text.split("Variant") if v.strip()]
    return variants

def save_variants(variants: List[str], output_dir: str):
    """Save the variants to separate files."""
    os.makedirs(output_dir, exist_ok=True)
    for i, variant in enumerate(variants, start=1):
        file_path = os.path.join(output_dir, f"variant_{i}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"Variant {i}\n{'='*40}\n\n{variant}")
    print(f"✅ {len(variants)} variants saved to {output_dir}")

if __name__ == "__main__":
    import sys

    # Usage: python generate_variants.py opt-in-pdf 10
    prompt_name = sys.argv[1] if len(sys.argv) > 1 else "opt-in-pdf"
    num_variants = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    prompt = read_prompt(f"{prompt_name}.md")
    print(f"🔄 Generating {num_variants} variants using {prompt_name} template...")

    variants = generate_variants(prompt, num_variants)
    save_variants(variants, OUTPUT_DIR)
