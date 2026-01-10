# Cross-Case Exploit Correlation Analysis

## Purpose
This document correlates historical exploit cases to identify recurring risk patterns,
systemic weaknesses, and failure points not adequately addressed by traditional audits.

The goal is to extract actionable risk signals that can be continuously monitored.

---

## Case Studies Included
- The DAO (2016) — Contract Logic Failure
- bZx (2020) — Oracle & Economic Manipulation
- Ronin Bridge (2022) — Infrastructure & Governance Compromise

---

## Correlated Risk Dimensions

### 1. Audit Blind Spots
Across all cases, the exploited components were:
- Technically “correct” at the code level
- Functionally vulnerable under real-world conditions

Audits failed to:
- Model adversarial economic behavior
- Detect governance centralization risks
- Simulate cross-contract or cross-system interactions

---

### 2. Time-Based Failure Patterns
All exploits shared delayed detection:
- No real-time anomaly alerts
- Long windows between exploit execution and discovery
- Reactive rather than preventive controls

This highlights monitoring as a critical missing layer.

---

### 3. Centralization as a Risk Multiplier
Each case contained a centralization factor:
- DAO: Governance rigidity
- bZx: Single-source oracle
- Ronin: Validator concentration

Centralization amplified impact and reduced response time.

---

### 4. External Dependency Risks
The exploited systems depended on:
- External contracts
- Market prices
- Off-chain governance decisions

These dependencies were not continuously assessed.

---

### 5. Signal Patterns Observed Pre-Exploit
Retrospective analysis reveals early warning signals:
- Abnormal transaction recursion
- Sudden market price deviations
- Unusually large value transfers

These signals were present but unmonitored.

---

## Cross-Case Risk Categories

| Risk Category | DAO | bZx | Ronin |
|-------------|-----|-----|-------|
| Contract Logic | ✅ | ❌ | ❌ |
| Oracle Dependency | ❌ | ✅ | ❌ |
| Governance Centralization | ⚠️ | ⚠️ | ✅ |
| Monitoring Absence | ✅ | ✅ | ✅ |

---

## SentinelZero Insight
Security failures are rarely isolated bugs.
They emerge from *combinations of small, tolerated risks*.

SentinelZero targets these combinations through:
- Continuous observability
- Historical pattern learning
- Real-time anomaly detection
