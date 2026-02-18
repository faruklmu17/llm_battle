
import json
import os

STATS_FILE = "data/stats.json"

def record_result(model_a, model_b, winner):
    """
    Saves the result of a battle to data/stats.json
    winner: 'X', 'O', or 'Draw'
    """
    if not os.path.exists("data"):
        os.makedirs("data")
        
    stats = []
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, "r") as f:
                stats = json.load(f)
        except:
            stats = []

    # Map winner to actual model name
    result = "Draw"
    if winner == "X": result = model_a
    elif winner == "O": result = model_b

    entry = {
        "player_x": model_a,
        "player_o": model_b,
        "winner": result
    }
    
    stats.append(entry)

    # Keep only the last 50 entries
    if len(stats) > 50:
        stats = stats[-50:]
    
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)
