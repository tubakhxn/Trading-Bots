import matplotlib.pyplot as plt
import numpy as np

def plot_liquidity_sweeps(df, swings, output_path="outputs/liquidity_sweeps.png"):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(16, 8), facecolor="#0d1117")
    ax.set_facecolor("#0d1117")

    # Price line
    price_col = 'Close' if 'Close' in df.columns else 'close'
    ax.plot(df.index, df[price_col], color="white", linewidth=2, label="Price")

    # Swing highs/lows
    ax.scatter(swings.index, swings['swing_high'], color="#888888", s=20, label="Swing Highs", zorder=3)
    ax.scatter(swings.index, swings['swing_low'], color="#888888", s=20, label="Swing Lows", zorder=3)

    # Bearish sweeps
    bearish_idx = swings.index[swings['bearish_sweep']]
    ax.scatter(bearish_idx, swings.loc[bearish_idx, 'high'], color="#ff266e", s=80, marker="v", label="Bearish Sweep", edgecolor="black", linewidth=1.5, zorder=4)
    # Highlight bearish sweep zones
    for idx in bearish_idx:
        zone = swings.loc[idx, 'bearish_sweep_zone']
        if not np.isnan(zone):
            ax.axhspan(zone*0.999, zone*1.001, color="#ff266e", alpha=0.18, zorder=1)

    # Bullish sweeps
    bullish_idx = swings.index[swings['bullish_sweep']]
    ax.scatter(bullish_idx, swings.loc[bullish_idx, 'low'], color="#39ff14", s=80, marker="^", label="Bullish Sweep", edgecolor="black", linewidth=1.5, zorder=4)
    # Highlight bullish sweep zones
    for idx in bullish_idx:
        zone = swings.loc[idx, 'bullish_sweep_zone']
        if not np.isnan(zone):
            ax.axhspan(zone*0.999, zone*1.001, color="#39ff14", alpha=0.18, zorder=1)

    ax.legend(loc="upper left", fontsize=12, frameon=False)
    ax.set_title("Liquidity Sweep Detection", fontsize=22, color="white", pad=20)
    ax.grid(True, color="#22272e", alpha=0.5)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor())
    plt.close()
