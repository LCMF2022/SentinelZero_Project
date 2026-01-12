import json
import requests

DEFILLAMA_ALL_PROTOCOLS = "https://api.llama.fi/protocols"

# Institutional Risk Weights
WEIGHTS = {
    "Low Liquidity": 25,
    "Sharp TVL Drop": 35,
    "Bridge Exposure": 30,
    "Governance Risk": 45,
    "Oracle Dependency": 40
}

def load_knowledge():
    try:
        with open('knowledge_base.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def translate_signals(llama_data):
    features = []
    tvl = llama_data.get("tvl", 0)
    change_7d = llama_data.get("change_7d", 0)
    category = llama_data.get("category", "Unknown")

    if tvl < 5000000: features.append("Low Liquidity")
    if change_7d <= -25: features.append("Sharp TVL Drop")
    if category == "Bridge": features.append("Bridge Exposure")
    elif category in ["Lending", "DAO", "Yield"]: features.append("Governance Risk")
    elif category in ["DEX", "Derivatives"]: features.append("Oracle Dependency")
    
    return features

def get_risk_label(score):
    if score < 25: return "🟢 LOW"
    if score < 55: return "🟡 MEDIUM"
    if score < 85: return "🟠 HIGH"
    return "🔴 CRITICAL"

def analyze_protocol(identifier):
    knowledge = load_knowledge()
    if not knowledge:
        print("❌ Error: knowledge_base.json not found.")
        return

    print(f"🔍 SentinelZero: Analyzing {identifier}...")
    response = requests.get(DEFILLAMA_ALL_PROTOCOLS)
    all_data = response.json()
    
    protocol_data = next((p for p in all_data if p["name"].lower() == identifier.lower() or p.get("slug","").lower() == identifier.lower()), None)

    if not protocol_data:
        print(f"❌ Protocol '{identifier}' not found in public database.")
        return

    observed_features = translate_signals(protocol_data)
    risk_score = 0
    alerts = []

    for exploit in knowledge["exploits_registry"]:
        for indicator in exploit["risk_indicators"]:
            if indicator in observed_features:
                risk_score += WEIGHTS.get(indicator, 10)
                alerts.append(f"⚠️ Alert: Pattern match - {indicator} (similar to {exploit['project']} case)")

    final_score = min(risk_score, 100)
    label = get_risk_label(final_score)

    print(f"\n{'='*45}")
    print(f"🛡️ SENTINELZERO TECHNICAL REPORT")
    print(f"{'='*45}")
    print(f"Protocol: {protocol_data['name']} | Cat: {protocol_data['category']}")
    print(f"Current TVL: ${protocol_data['tvl']:,.2f} | 7d Change: {protocol_data.get('change_7d', 0):.2f}%")
    print(f"Risk Signals: {', '.join(observed_features) if observed_features else 'Clear'}")
    print(f"\nFINAL SCORE: {final_score}/100 | STATUS: {label}")
    print(f"{'='*45}")

    if alerts:
        print("\nDETECTION LOGS:")
        for a in set(alerts): print(a)

if __name__ == "__main__":
    analyze_protocol("Aave")
