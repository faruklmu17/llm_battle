
import json
import matplotlib.pyplot as plt
import numpy as np
import os

STATS_FILE = "data/stats.json"
OUTPUT_IMAGE = "data/performance_chart.png"

def generate_performance_graph():
    if not os.path.exists(STATS_FILE):
        print("No stats data found. Run some battles first!")
        return

    with open(STATS_FILE, "r") as f:
        data = json.load(f)

    # We need to track Wins, Losses, and Draws per model
    # Structure: { model_name: {"wins": 0, "losses": 0, "draws": 0} }
    model_stats = {}

    for game in data:
        p1 = game["player_x"]
        p2 = game["player_o"]
        winner = game["winner"]

        for p in [p1, p2]:
            if p not in model_stats:
                model_stats[p] = {"wins": 0, "losses": 0, "draws": 0}

        if winner == "Draw":
            model_stats[p1]["draws"] += 1
            model_stats[p2]["draws"] += 1
        elif winner == p1:
            model_stats[p1]["wins"] += 1
            model_stats[p2]["losses"] += 1
        elif winner == p2:
            model_stats[p2]["wins"] += 1
            model_stats[p1]["losses"] += 1

    models = sorted(model_stats.keys())
    wins = [model_stats[m]["wins"] for m in models]
    losses = [model_stats[m]["losses"] for m in models]
    draws = [model_stats[m]["draws"] for m in models]

    x = np.arange(len(models))
    width = 0.25

    plt.style.use('dark_background') # Premium dark mode look
    fig, ax = plt.subplots(figsize=(12, 7))

    rects1 = ax.bar(x - width, wins, width, label='Wins', color='#00C853', edgecolor='white', linewidth=0.5)
    rects2 = ax.bar(x, draws, width, label='Draws/Incomplete', color='#FFD600', edgecolor='white', linewidth=0.5)
    rects3 = ax.bar(x + width, losses, width, label='Losses', color='#D50000', edgecolor='white', linewidth=0.5)

    # Aesthetics
    ax.set_ylabel('Match Count', fontsize=12, color='white')
    ax.set_title('LLM Battle Arena: Performance (Last 50 Matches)', fontsize=16, fontweight='bold', pad=20, color='white')
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=10, rotation=15)
    ax.legend(frameon=True, facecolor='#333333', edgecolor='white')

    ax.grid(axis='y', linestyle='--', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom', color='white', fontweight='bold')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE, dpi=300) # High Resolution
    print(f"✨ Enhanced performance graph generated at: {OUTPUT_IMAGE}")

if __name__ == "__main__":
    generate_performance_graph()
