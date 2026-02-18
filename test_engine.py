
from src.games.tictactoe import TicTacToe

def test_engine():
    print("Testing Game Engine Logic...")
    
    # Test 1: Horizontal Win
    game = TicTacToe()
    game.make_move(0) # X
    game.make_move(3) # O
    game.make_move(1) # X
    game.make_move(4) # O
    game.make_move(2) # X
    assert game.winner == "X", "Error: X should have won horizontally"
    print("✅ Horizontal win test passed")

    # Test 2: Diagonal Win
    game = TicTacToe()
    game.make_move(0) # X
    game.make_move(1) # O
    game.make_move(4) # X
    game.make_move(2) # O
    game.make_move(8) # X
    assert game.winner == "X", "Error: X should have won diagonally"
    print("✅ Diagonal win test passed")

    # Test 3: Draw
    game = TicTacToe()
    moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]
    for move in moves:
        game.make_move(move)
    assert game.winner == "Draw", "Error: Should be a draw"
    print("✅ Draw logic test passed")

if __name__ == "__main__":
    try:
        test_engine()
        print("\nALL PHASE 1 ENGINE TESTS PASSED! 🚀")
    except AssertionError as e:
        print(f"\n❌ Test Failed: {e}")
