# Long Asset vs Manual Short vs Short ETF

### Volatility, Path Dependency and Decay Simulation in Python

This project is a quantitative simulation that compares three different market exposures over time:

* **Long Asset (Buy & Hold)**
* **Manual Short Position** (borrow & sell, not rebalanced)
* **Short ETF** (daily rebalanced inverse exposure)

The purpose is to highlight how **volatility and daily compounding** affect different strategies, even when they are designed to be theoretically inverse.

---

## Objective

The simulation aims to:

* Compare long and short exposures under identical market conditions
* Show the difference between a **manual short** and a **short ETF**
* Demonstrate **volatility decay** and **path dependency**
* Explain why short ETFs can diverge from manual short positions over time

This is a **didactic project**, not a realistic trading model.

---

## Methodology

* Initial capital is fixed
* Daily price variations are randomly sampled from a predefined discrete set
* The simulation runs for a fixed number of days
* Three portfolios are tracked simultaneously:

  * Long asset value
  * Manual short value (non-compounding)
  * Short ETF value (daily rebalanced)
* Final returns and percentage differences are calculated

A fixed random seed is used to ensure reproducibility.

---

## Strategy Definitions

### Long Asset

A standard buy-and-hold position:

* Gains when the asset price increases
* Loses when the asset price decreases

---

### Manual Short

A simplified short-selling model:

* The asset is borrowed and sold once
* The position is **not rebalanced daily**
* Value is computed as:

```
Manual Short Value = 2 × Initial Investment − Current Asset Value
```

This preserves the theoretical inverse relationship with the underlying asset.

---

### Short ETF

A simplified inverse ETF model:

* Daily rebalanced to maintain inverse exposure
* Compounds returns daily
* Suffers from volatility decay over time

This mimics the behavior of real-world inverse ETFs under volatile conditions.

---

## Key Concepts Covered

* Path dependency
* Volatility decay
* Daily compounding effects
* Difference between static and rebalanced inverse exposure

---

## Output

The script prints:

* Periodic profit & loss updates during the simulation
* Final portfolio values and returns
* The absolute and percentage difference between Manual Short and Short ETF
* A verification check showing that the manual short remains inversely linked to the asset

---

## Limitations

This model is intentionally simplified:

* Returns are sampled from a discrete set, not a continuous distribution
* No transaction costs, funding rates, or taxes
* No margin calls or leverage constraints
* Short ETF behavior is simplified and not tied to a specific real product

Despite these simplifications, the model clearly illustrates volatility-related effects.

---

## How to Run

Ensure you have Python 3 installed, then run:

```
python etf-vs-cfd.py
```

