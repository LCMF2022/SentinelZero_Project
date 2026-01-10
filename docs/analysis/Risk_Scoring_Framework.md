# Risk Scoring Framework

## Objective
Quantify protocol risk using historical exploit patterns, observable signals,
and amplification factors to produce actionable risk scores.

---

## Scoring Model

### 1. Base Categories
| Category | Weight | Description |
|----------|--------|-------------|
| Contract Logic | 25% | Reentrancy, access control, state mismanagement |
| Oracle & Economic | 25% | Single-source or manipulable data feeds |
| Governance & Permission | 20% | Centralized control, admin keys, delayed governance |
| Infrastructure & Bridge | 20% | Validator concentration, cross-chain vulnerabilities |
| Monitoring & Response | 10% | Lack of alerts, slow response, observability gaps |

**Total:** 100%

---

### 2. Signal Scoring
For each observable signal in the Exploit Taxonomy:
- Assign 0 (absent) / 1 (partial) / 2 (present)  
- Multiply by category weight

**Example:**  
| Signal | Observed | Weight | Score |
|--------|----------|--------|-------|
| External calls before state updates | Present | 25% | 0.25*2 = 0.50 |
| Single-source oracle | Partial | 25% | 0.25*1 = 0.25 |
| Admin key concentration | Absent | 20% | 0 |

**Protocol Risk Score:** 0.50 + 0.25 + 0 = 0.75 (normalized)

---

### 3. Amplification Modifiers
- Centralization factor: x1.2  
- Low liquidity assets: x1.1  
- No monitoring: x1.15  

**Final Risk Score:**  
`Risk_Score = Base_Score * Amplification_Modifiers`

---

### 4. Risk Categories
| Score | Classification | Action |
|-------|----------------|--------|
| 0–0.3 | Low | Standard monitoring |
| 0.31–0.6 | Medium | Flag for review |
| 0.61–0.8 | High | Developer alert & limited exposure |
| 0.81–1.0 | Critical | Immediate intervention suggested |

---

### 5. Continuous Learning
- Each exploit detected feeds back into:
  - Signal definitions
  - Weight adjustments
  - Amplification modifiers

- Risk scoring **evolves dynamically** with new attacks.

---

## SentinelZero Differentiation
- Moves beyond audits (“code correct?”)
- Provides **predictive insights**
- Quantifies systemic risk, not just single vulnerabilities
- Offers developers and investors a **trust metric** for decision-making
