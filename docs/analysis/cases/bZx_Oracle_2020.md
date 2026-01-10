# bZx Oracle Manipulation Attack (2020)

## 1. Incident Overview
- Protocol Name: bZx
- Date: February 2020
- Chain: Ethereum
- Category: Oracle / Economic Exploit

## 2. Financial Impact
- Funds lost: ~USD 1M
- Assets involved: ETH, WBTC, stablecoins
- Recovery status: Partial mitigation via protocol changes

## 3. Attack Vector
- Technical entry point: Price oracle manipulation via flash loans
- Vulnerability type: Oracle dependency without price validation
- Preconditions required:
  - On-chain oracle using low-liquidity DEX prices
  - Absence of time-weighted average pricing (TWAP)

## 4. Root Cause
- Reliance on a single price source
- No safeguards against short-term price distortion
- Flash loan availability without risk throttling

## 5. Attack Execution Flow
1. Attacker obtained a large flash loan
2. Manipulated asset price on a low-liquidity DEX
3. Oracle consumed manipulated price
4. bZx accepted inflated collateral value
5. Attacker extracted profit and repaid flash loan

## 6. Detection Possibility
- Sudden price deviation from market average
- Large flash loan transactions correlated with oracle updates
- High slippage events before protocol interactions

## 7. Preventive Signals (Retrospective)
- Cross-market price divergence alerts
- Oracle update frequency anomalies
- Flash loan + protocol interaction coupling

## 8. Mapping to SentinelZero
- Risk Category: Oracle Risk / Economic Attack
- SentinelZero Flag:
  - Single-source oracle dependency
  - Low-liquidity price feeds
- Preventive Insight:
  - Flag protocols where oracle prices diverge significantly from multi-source benchmarks
