# SentinelZero — MVP Dashboard Blueprint

## Purpose
The SentinelZero dashboard provides real-time and historical visibility into
post-audit protocol risk using data-driven exploit patterns and scoring.

It is designed for developers, auditors, investors, and ecosystem foundations.

---

## Core Dashboard Sections

### 1. Protocol Overview Panel
**Displayed Data:**
- Protocol name
- Chain (BNB Chain, Ethereum, etc.)
- TVL (if available)
- Audit status (audited / unaudited / partially audited)

**Visual Elements:**
- Protocol logo
- Chain badge
- Audit indicator

---

### 2. Global Risk Score
**Displayed Data:**
- Composite Risk Score (0–1)
- Risk classification (Low / Medium / High / Critical)

**Visual Elements:**
- Risk gauge or radial indicator
- Color-coded severity

**Derived From:**
- Risk Scoring Framework
- Amplification Modifiers

---

### 3. Risk Breakdown by Category
**Categories:**
- Contract Logic
- Oracle & Economic
- Governance & Permission
- Infrastructure & Bridge
- Monitoring & Response

**Visual Elements:**
- Radar chart or stacked bar chart
- Hover tooltips with signal explanations

---

### 4. Detected Risk Signals
**Displayed Data:**
- Active SentinelZero Flags
- Description of each detected signal
- Severity level

**Example:**
- `ORACLE_DEPENDENCY_RISK`
- `GOVERNANCE_CENTRALIZATION_RISK`

---

### 5. Historical Exploit Similarity
**Purpose:**
Show similarity between current protocol signals and past exploits.

**Displayed Data:**
- Matched historical cases
- Similarity percentage
- Impact comparison

**Example:**
- “Similar to bZx Oracle Attack (2020) — 72% similarity”

---

### 6. Timeline & Event Monitor
**Displayed Data:**
- Risk score evolution over time
- Major protocol events
- Alert history

**Visual Elements:**
- Line chart
- Event markers

---

### 7. Actionable Recommendations
**Displayed Data:**
- Suggested mitigations
- Monitoring priorities
- Governance improvements

**Tone:**
Advisory, non-intrusive, non-enforcing

---

## MVP Technical Scope (Non-Code)
- Data source: Public exploit datasets + manual tagging
- No on-chain enforcement
- Read-only observability
- Single-chain focus (BNB Chain)

---

## Target Users
- DeFi protocol teams
- Security auditors
- Grant committees
- Institutional investors

---

## SentinelZero Value Proposition
“From static audits to continuous risk intelligence.”
