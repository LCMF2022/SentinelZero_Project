# Ronin Bridge Exploit (2022)

## 1. Incident Overview
- Protocol Name: Ronin Bridge (Axie Infinity)
- Date: March 2022
- Chain: Ronin / Ethereum
- Category: Bridge / Validator Compromise

## 2. Financial Impact
- Funds lost: ~USD 625M
- Assets involved: ETH, USDC
- Recovery status: Partial recovery with ecosystem intervention

## 3. Attack Vector
- Technical entry point: Compromised validator private keys
- Vulnerability type: Governance & infrastructure failure
- Preconditions required:
  - Low validator threshold (5 of 9)
  - Centralized validator control
  - Long inactivity in monitoring bridge withdrawals

## 4. Root Cause
- Excessive centralization of validator permissions
- Inadequate operational security (key management)
- Lack of real-time monitoring for large bridge transfers

## 5. Attack Execution Flow
1. Attacker compromised validator private keys
2. Generated fraudulent withdrawal approvals
3. Submitted signed bridge withdrawal transactions
4. Bridge validated signatures and released funds
5. Funds remained undetected for several days

## 6. Detection Possibility
- Large withdrawal events exceeding historical norms
- Unusual validator signature patterns
- Delayed detection due to absence of active monitoring

## 7. Preventive Signals (Retrospective)
- Validator concentration risk scoring
- Withdrawal size anomaly detection
- Inactive monitoring windows alerts

## 8. Mapping to SentinelZero
- Risk Category: Infrastructure & Governance Risk
- SentinelZero Flag:
  - Low validator decentralization
  - Infrequent monitoring of bridge flows
- Preventive Insight:
  - Highlight bridges with centralized validator sets and delayed alert systems
