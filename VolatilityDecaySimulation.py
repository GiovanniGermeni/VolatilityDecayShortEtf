# Returns are sampled from a discrete set to highlight volatility effects
import random

# Simulation parameters
SEED = 30
INITIAL_INVESTMENT = 200
DAYS = 100

# Daily variations to test
VARIATIONS = (0.02, -0.03, -0.04, 0.05)
# Alternative scenarios:
# VARIATIONS = (-0.01, -0.02, -0.03, -0.04)  # Bearish trend
# VARIATIONS = (0.1, 0.02, 0.03, 0.04)        # Bullish trend

random.seed(SEED)

# Initialize portfolios
asset_value = INITIAL_INVESTMENT      # Long position (buy)
short_manual = INITIAL_INVESTMENT     # Manual short (borrow & sell)
short_etf = INITIAL_INVESTMENT        # Short ETF (daily rebalanced)

print("=" * 90)
print(f"SIMULATION: {DAYS} days with seed={SEED}")
print("=" * 90)
print(f"Initial Investment: ${INITIAL_INVESTMENT}")
print(f"Variations: {[f'{v*100:+.0f}%' for v in VARIATIONS]}")
print("=" * 90)
print(f"{'Day':<6} {'Asset P&L':<15} {'Manual Short':<15} {'ETF Short':<15} {'Daily Var':<12}")
print("-" * 90)
print(f"{'0':<6} ${'0.00':>8}{'':<6} ${'0.00':>8}{'':<6} ${'0.00':>8}{'':<6}  -")

for day in range(1, DAYS + 1):
    # Random daily variation
    daily_var = VARIATIONS[random.randint(0, len(VARIATIONS) - 1)]
    
    # Update asset price
    asset_value += asset_value * daily_var
    
    # Manual short: Value = 2 × Initial - Current Asset Price
    # Explanation: You have $100 cash from selling + $100 initial - debt (current price)
    short_manual = (INITIAL_INVESTMENT * 2) - asset_value
    
    # Short ETF: Daily rebalanced, compounds inverse returns
    short_etf -= short_etf * daily_var
    
    # Print every 10 days to avoid clutter, or print all for detailed view
    if day % 10 == 0 or day <= 10 or day == DAYS + 1:
        print(f"{day:<6} {f'${asset_value - INITIAL_INVESTMENT:>8.2f}':<15} "
              f"{f'${short_manual - INITIAL_INVESTMENT:>8.2f}':<15} "
              f"{f'${short_etf - INITIAL_INVESTMENT:>8.2f}':<15} "
              f"{f'{daily_var * 100:+.0f}%':<12}")

print("=" * 90)

# Final results
print("\nFINAL RESULTS:")
print("-" * 90)

asset_return = (100 * (asset_value - INITIAL_INVESTMENT)) / INITIAL_INVESTMENT
short_return = (100 * (short_manual - INITIAL_INVESTMENT)) / INITIAL_INVESTMENT
etf_return = (100 * (short_etf - INITIAL_INVESTMENT)) / INITIAL_INVESTMENT


print(f"Long Asset:            ${asset_value:>8.2f}  ({asset_return:>+.2f}%)")
print(f"Manual Short:          ${short_manual:>8.2f}  ({short_return:>+.2f}%)")
print(f"Short ETF (SSIL):      ${short_etf:>8.2f}  ({etf_return:>+.2f}%)")

# Analysis
print("\nANALYSIS:")
print("-" * 90)
difference = abs(short_manual - short_etf)
decay_pct = (1 - short_etf / short_manual) * 100 if short_manual > short_etf else (1 - short_manual / short_etf) * 100

print(f"Difference: ${difference:.2f} ({decay_pct:.2f}% volatility decay)")

# Verify inverse relationship
asset_change = asset_value - INITIAL_INVESTMENT
short_change = short_manual - INITIAL_INVESTMENT
print(f"Verification:")
print(f"  Asset change: ${asset_change:+.2f}")
print(f"  Manual short change: ${short_change:+.2f}")
print(f"  Sum (should be ~$0): ${asset_change + short_change:+.2f}")
