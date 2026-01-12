import json

def load_knowledge():
    with open('knowledge_base.json', 'r') as f:
        return json.load(f)

def analyze_protocol(name, features):
    knowledge = load_knowledge()
    risk_score = 0
    matches = []

    # O "Cérebro" comparando o novo protocolo com ataques passados
    for exploit in knowledge['exploits_registry']:
        for indicator in exploit['risk_indicators']:
            if indicator.lower() in [f.lower() for f in features]:
                risk_score += 33  # Aumenta o risco se encontrar padrão suspeito
                matches.append(f"ALERTA: Padrão similar ao ataque {exploit['project']} ({indicator})")

    # Limitando o score a 100
    final_score = min(risk_score, 100)
    
    print(f"\n--- Relatório SentinelZero para: {name} ---")
    print(f"Índice de Risco: {final_score}/100")
    if matches:
        for m in matches: print(m)
    else:
        print("Nenhum padrão de ataque histórico detectado até o momento.")

# SIMULAÇÃO: Imagine que você está analisando um novo protocolo agora
# Você, como consultor, identifica essas características:
caracteristicas_vistas = ["Low liquidity pool", "Flash loan involvement"]

analyze_protocol("Projeto Novo DeFi", caracteristicas_vistas)
