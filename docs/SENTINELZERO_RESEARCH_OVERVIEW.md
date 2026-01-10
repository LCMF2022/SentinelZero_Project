# SentinelZero — Research Overview

## Executive Summary
SentinelZero addresses a critical gap in post-audit DeFi protocol security:
even audited smart contracts remain vulnerable due to hidden economic, governance,
and infrastructure risks. Smaller projects often lack resources for continuous
monitoring, leaving the ecosystem exposed to repeated exploits.

SentinelZero provides a **data-driven, automated risk monitoring framework**
that identifies potential exploits, evaluates systemic vulnerabilities, and
produces actionable intelligence for developers, auditors, and investors.

---

## 1. Historical Case Studies

### 1.1 The DAO (2016)
- Contract Logic Exploit
- ~$50M ETH lost
- Root Cause: Reentrancy vulnerability
- SentinelZero Flag: `LOGIC_ORDER_RISK`

### 1.2 bZx Oracle Manipulation (2020)
- Oracle / Economic Exploit
- ~$1M USD lost
- Root Cause: Single-source oracle + flash loan
- SentinelZero Flag: `ORACLE_DEPENDENCY_RISK`

### 1.3 Ronin Bridge (2022)
- Infrastructure / Governance Exploit
- ~$625M USD lost
- Root Cause: Low validator decentralization, key compromise
- SentinelZero Flag: `INFRASTRUCTURE_TRUST_RISK`

---

## 2. Cross-Case Correlation
- Audit blind spots: code correctness alone does not prevent exploits
- Centralization multiplies impact across all cases
- Delayed detection is common; continuous monitoring is critical
- External dependencies (oracles, bridges) frequently ignored

---

## 3. Exploit Taxonomy
1. Contract Logic Exploits → `LOGIC_ORDER_RISK`
2. Oracle & Economic Exploits → `ORACLE_DEPENDENCY_RISK`
3. Governance & Permission Exploits → `GOVERNANCE_CENTRALIZATION_RISK`
4. Infrastructure & Bridge Exploits → `INFRASTRUCTURE_TRUST_RISK`
5. Monitoring & Response Failures → `OBSERVABILITY_GAP_RISK`

**Amplification Factors:**
- Centralization  
- Liquidity thinness  
- Governance latency  
- Monitoring absence  

---

## 4. Risk Scoring Framework
- Scores based on taxonomy signals and amplification factors
- Weighted scoring by category:
  - Contract Logic 25%
  - Oracle & Economic 25%
  - Governance & Permission 20%
  - Infrastructure & Bridge 20%
  - Monitoring & Response 10%
- Risk Levels:
  - Low (0–0.3)
  - Medium (0.31–0.6)
  - High (0.61–0.8)
  - Critical (0.81–1.0)
- Continuous learning: each new exploit updates signals, weights, and modifiers

---

## 5. MVP Dashboard Blueprint
**Sections:**
- Protocol Overview Panel
- Global Risk Score
- Risk Breakdown by Category
- Detected Risk Signals
- Historical Exploit Similarity
- Timeline & Event Monitor
- Actionable Recommendations

**Key Features:**
- Visualize risk in real-time
- Show historical patterns
- Prioritize alerts
- Advisory recommendations for devs and investors

---

## 6. Strategic Value
- Moves beyond static audits
- Quantifies post-audit risk
- Predictive intelligence for protocols
- Ideal for grants, foundations, and institutional adoption

**Repository:** [SentinelZero GitHub](https://github.com/LCMF2022/SentinelZero)
