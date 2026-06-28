# Funnel KPI Analyzer
# Tracks DM funnel performance metrics

def calculate_conversion_rate(sent, replied, opted_in):
    """Calculate funnel conversion rates."""
    reply_rate = (replied / sent) * 100 if sent > 0 else 0
    optin_rate = (opted_in / replied) * 100 if replied > 0 else 0
    return reply_rate, optin_rate

def analyze_funnel(data):
    """Analyze complete funnel performance."""
    print("📊 Funnel Analysis")
    print(f"Messages Sent: {data['sent']}")
    print(f"Replies: {data['replied']}")
    print(f"Opt-ins: {data['opted_in']}")
    reply_rate, optin_rate = calculate_conversion_rate(
        data['sent'], data['replied'], data['opted_in']
    )
    print(f"Reply Rate: {reply_rate:.1f}%")
    print(f"Opt-in Rate: {optin_rate:.1f}%")

if __name__ == "__main__":
    # Example data
    test_data = {
        "sent": 100,
        "replied": 45,
        "opted_in": 22
    }
    analyze_funnel(test_data)
