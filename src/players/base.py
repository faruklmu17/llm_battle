from abc import ABC, abstractmethod

class BasePlayer(ABC):
    def __init__(self, model_name):
        self.model_name = model_name

    @abstractmethod
    def get_move(self, game_state_prompt):
        """
        Takes the text description of the board and returns a move (int 0-8).
        """
        pass

class RandomPlayer(BasePlayer):
    """A baseline player that picks moves randomly."""
    import random
    
    def get_move(self, game_state_prompt):
        import re
        import random
        # Find digits in the prompt to know valid moves
        moves = [int(m) for m in re.findall(r'\d+', game_state_prompt.split("movies: ")[-1])]
        return random.choice(moves) if moves else None
