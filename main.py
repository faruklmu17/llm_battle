from src.games.tictactoe import TicTacToe
from src.players.factory import get_player
from src.utils.tracker import record_result
from src.utils.visualize import generate_performance_graph
import time

def start_battle(model_a_name, model_b_name):
    print(f"--- BATTLE START: {model_a_name} vs {model_b_name} ---\n")
    
    game = TicTacToe()
    player_x = get_player(model_a_name)
    player_o = get_player(model_b_name)
    
    players = {"X": player_x, "O": player_o}
    
    while not game.is_game_over():
        current_symbol = game.current_player
        current_player_obj = players[current_symbol]
        
        print(f"--- Player {current_symbol}'s Turn ({current_player_obj.model_name}) ---")
        prompt = game.get_state_prompt()
        
        # Try to get a valid move (up to 3 times)
        success = False
        for attempt in range(3):
            move = current_player_obj.get_move(prompt)
            if move is not None and game.make_move(move):
                print(f"Move chosen: {move}")
                print(game.display_board())
                success = True
                break
            else:
                print(f"Invalid move or failure: {move} (Attempt {attempt+1}/3)")
        
        if not success:
            print(f"Model {current_player_obj.model_name} failed to provide a valid move after 3 attempts.")
            break
            
        time.sleep(0.5) # Slightly faster for tournaments
        
    print("\n--- GAME OVER ---")
    if game.winner == "Draw":
        print("Result: It's a DRAW!")
    elif game.winner:
        print(f"Result: Player {game.winner} ({players[game.winner].model_name}) WINS!")
    else:
        print("Result: Game ended prematurely (No Winner).")

    # Save data for Phase 3 and Graphing
    record_result(model_a_name, model_b_name, game.winner)
    generate_performance_graph()

if __name__ == "__main__":
    # Restarting Arena...
    for i in range(1):
        print(f"\n🚀 TOURNAMENT MATCH {i+1}")
        start_battle("gemini-flash-latest", "llama-3.3-70b-versatile")
        print("-" * 40)
