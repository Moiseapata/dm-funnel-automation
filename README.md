# DM Funnel Automation 🚀

**AI-powered workflows for Instagram DM funnels** – prompts, scripts, and automation templates for high-converting copy.

## 🎯 Why This Repo?

This repo contains everything needed to automate DM funnel copy for creators and brands:
- **Optimized prompts** for Claude to generate high-converting DM sequences.
- **Python scripts** to automate copy generation and KPI analysis.
- **Real-world examples** of DM funnels for different tones and offers (Amy Porterfield, Prince EA).

## 📁 Structure

```
dm-funnel-automation/
├── prompts/                    # Claude prompt templates
│   ├── opt-in-pdf.md           # Free PDF lead magnet
│   ├── webinar-registration.md # Webinar signups
│   ├── sales-sequence.md       # High-ticket offers
│   └── re-engagement.md        # Inactive lead reactivation
├── scripts/                    # Automation tools
│   ├── generate_variants.py    # Batch variant generator
│   └── analyze_kpis.py         # Funnel performance tracker
├── examples/                   # Real DM examples
│   ├── amy_porterfield/
│   └── prince_ea/
└── README.md
```

## 🤖 How It Works

### 1. Generate DM Sequences with Claude

Use any prompt template from `/prompts` to generate 10+ DM variants:

```bash
python scripts/generate_variants.py opt-in-pdf 10
```

### 2. Automate with Python

- **`generate_variants.py`**: Batch-generates copy variants via Claude API.
- **`analyze_kpis.py`**: Tracks reply rates, opt-in rates, and funnel performance.

### 3. Optimize Based on KPIs

- Test variants in real campaigns.
- Use `analyze_kpis.py` to identify top performers.
- Feed winning patterns back into your prompts.

## 📝 Example Workflow

1. **Brief**: Client wants to promote a free PDF.
2. **Prompt**: Use `prompts/opt-in-pdf.md` in Claude.
3. **Generate**: Run `generate_variants.py` to create 10 variants.
4. **Test**: A/B test the top 3 variants in real DMs.
5. **Optimize**: Use `analyze_kpis.py` to refine the winner.

## 🔧 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Moiseapata/dm-funnel-automation.git
   ```
2. Install dependencies:
   ```bash
   pip install anthropic
   ```
3. Set your Claude API key:
   ```bash
   export ANTHROPIC_API_KEY="your-key-here"
   ```

## 🚀 Who Is This For?

- **Copywriters** who want to automate repetitive DM tasks.
- **Agencies** scaling DM funnel production for clients.
- **AI builders** integrating LLMs into marketing workflows.

## 📌 Key Features

- ✅ **Tone adaptation**: Friendly, direct, inspirational, or premium.
- ✅ **KPI-driven**: Optimize based on real response rates.
- ✅ **Scalable**: Generate 100+ variants in minutes.
- ✅ **Ethical by default**: No fake scarcity, no manipulative tactics.

## 📬 Contact

For questions or collaborations, open an issue on this repo.
