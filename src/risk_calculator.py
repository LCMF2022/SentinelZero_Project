import json
import csv

# Load sample exploit data
with open("src/sample_data.json", "r") as f:
    protocols = json.load(f)

weights = {
    "contract_logic": 0.25,
    "oracle_economic": 0.25,
    "governance_permission": 0.20,
    "infrastructure_bridge": 0.20,
    "monitoring_response": 0.10
}

amplifiers = {
    "centralization": 1.2,
    "low_liquidity": 1.1,
    "no_monitoring": 1.15
}

def calculate_risk(protocol):
    score = 0
    for cat, weight in weights.items():
        signal_value = protocol["signals"].get(cat, 0)
        score += signal_value * weight
    
    amp = 1
    for key in amplifiers:
        if protocol.get(key, False):
            amp *= amplifiers[key]
    final_score = min(score * amp, 1.0)
    return round(final_score, 2)

output = []
for proto in protocols:
    risk = calculate_risk(proto)
    output.append({
        "protocol": proto["name"],
        "risk_score": risk,
        "classification": (
            "Low" if risk <= 0.3 else
            "Medium" if risk <= 0.6 else
            "High" if risk <= 0.8 else
            "Critical"
        )
    })

keys = ["protocol", "risk_score", "classification"]
with open("risk_scores.csv", "w", newline="") as f:
    dict_writer = csv.DictWriter(f, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(output)

print("Risk scoring complete! Results saved to risk_scores.csv")

Add risk_calculator prototype

