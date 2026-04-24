import matplotlib.pyplot as plt
import numpy as np

def plot_volatility_squeeze(df, bands, compression, breakout, output_path):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(14, 7))

    # Price line
    ax.plot(df.index, df['Close'], color='white', lw=1.5, label='Price')

    # Bollinger Bands
    ax.plot(df.index, bands['upper'], color='#b39ddb', lw=1, alpha=0.8, label='Upper Band')
    ax.plot(df.index, bands['lower'], color='#b39ddb', lw=1, alpha=0.8, label='Lower Band')
    ax.plot(df.index, bands['middle'], color='#9575cd', lw=0.8, alpha=0.7, label='Middle Band')

    # Compression zones
    comp_zones = compression.astype(float)
    comp_zones[~compression] = np.nan
    ax.fill_between(df.index, df['Close'].min(), df['Close'].max(), where=compression, color='#1976d2', alpha=0.18, label='Compression')

    # Breakout markers
    ax.scatter(df.index[breakout], df['Close'][breakout], color='yellow', s=60, edgecolor='black', lw=1.2, zorder=10, label='Breakout')

    # Style
    ax.grid(True, color='#444444', alpha=0.25, linestyle='--', linewidth=0.7)
    ax.set_facecolor('#181a20')
    ax.tick_params(colors='#bdbdbd', labelsize=11)
    ax.spines['bottom'].set_color('#bdbdbd')
    ax.spines['top'].set_color('#bdbdbd')
    ax.spines['left'].set_color('#bdbdbd')
    ax.spines['right'].set_color('#bdbdbd')
    ax.margins(x=0)
    ax.legend(loc='upper left', fontsize=11, frameon=False, ncol=2)
    ax.set_xlabel('Date', color='#bdbdbd', fontsize=12, labelpad=10)
    ax.set_ylabel('Price', color='#bdbdbd', fontsize=12, labelpad=10)
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.show()
    plt.close()
