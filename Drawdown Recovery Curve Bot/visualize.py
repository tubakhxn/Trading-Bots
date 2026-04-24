import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

def plot_drawdown_recovery(events, df, output_path):
    plt.style.use('dark_background')
    plt.rcParams['axes.facecolor'] = '#0d1117'
    plt.rcParams['figure.facecolor'] = '#0d1117'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'
    plt.rcParams['axes.edgecolor'] = 'white'
    plt.rcParams['grid.color'] = '#222'
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['legend.fontsize'] = 10

    depths = np.array([e['depth'] for e in events]) * 100  # percent
    durations = np.array([e['duration'] for e in events])

    # Identify extreme events (top 5% by depth)
    if len(depths) > 0:
        extreme_mask = depths <= np.percentile(depths, 5)
    else:
        extreme_mask = np.array([])

    fig = plt.figure(figsize=(10, 7))
    gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1], hspace=0.25)

    # Main scatter plot
    ax0 = plt.subplot(gs[0])
    sc = ax0.scatter(depths, durations, c=durations, cmap='plasma', s=40, alpha=0.85, edgecolor='w', linewidth=0.5)
    if len(depths) > 0 and np.any(extreme_mask):
        ax0.scatter(depths[extreme_mask], durations[extreme_mask], c='#fffb00', s=80, label='Extreme', edgecolor='black', linewidth=1.2, zorder=10)
    # Regression curve
    if len(depths) > 2:
        z = np.polyfit(depths, durations, 2)
        p = np.poly1d(z)
        x_fit = np.linspace(depths.min(), depths.max(), 200)
        ax0.plot(x_fit, p(x_fit), color='white', lw=2, alpha=0.7, label='Poly fit')
    ax0.set_xlabel('Drawdown Depth (%)')
    ax0.set_ylabel('Recovery Time (days)')
    ax0.set_title('Drawdown Depth vs. Recovery Time')
    ax0.grid(True, linestyle='-', alpha=0.18)
    ax0.legend(loc='upper left', frameon=False, fontsize=10)
    cbar = plt.colorbar(sc, ax=ax0, pad=0.01)
    cbar.set_label('Recovery Time (days)', color='white')
    cbar.ax.yaxis.set_tick_params(color='white')
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

    # Drawdown time series
    ax1 = plt.subplot(gs[1], sharex=ax0)
    ax1.plot(df.index, df['Drawdown'] * 100, color='#fffb00', lw=1.5, label='Drawdown (%)')
    ax1.set_ylabel('Drawdown (%)')
    ax1.set_xlabel('Date')
    ax1.grid(True, linestyle='-', alpha=0.18)
    ax1.set_title('Drawdown Curve')
    ax1.legend(loc='lower left', frameon=False, fontsize=10)

    for label in ax1.get_xticklabels():
        label.set(rotation=15, horizontalalignment='right')

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
