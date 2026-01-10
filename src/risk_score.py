# Placeholder for risk scoring logic
def calculate_risk(dimensions):
    score = sum(dimensions.values())
    return min(score, 1.0)

if __name__ == "__main__":
    sample = {"LID":0.2,"ESD":0.3,"IM":0.1,"ACD":0.15,"EDR":0.15,"HRD":0.1}
    print("Sample Risk Score:", calculate_risk(sample))

