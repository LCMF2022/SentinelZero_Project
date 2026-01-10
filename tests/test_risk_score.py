def test_risk_score():
    sample = {"LID":0.2,"ESD":0.3,"IM":0.1,"ACD":0.15,"EDR":0.15,"HRD":0.1}
    assert sum(sample.values()) <= 1.0

