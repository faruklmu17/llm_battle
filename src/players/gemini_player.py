
from google import genai
import re
from .base import BasePlayer
from src.utils.retries import retry_with_backoff

class GeminiPlayer(BasePlayer):
    def __init__(self, model_name, api_key):
        super().__init__(model_name)
        self.client = genai.Client(api_key=api_key)
        self.model_id = model_name

    def get_move(self, game_state_prompt):
        system_instruction = (
            "You are playing Tic-Tac-Toe. "
            "You will receive the current board and available moves. "
            "Respond with ONLY the number of your choice (0-8). "
            "Do not explain your move. Just the number."
        )
        
        def call_api():
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=[system_instruction, game_state_prompt]
            )
            return response.text.strip()

        try:
            text = retry_with_backoff(call_api)
            if not text: return None
            
            # Extract digits from response
            match = re.search(r'\d', text)
            if match:
                return int(match.group())
        except Exception as e:
            print(f"Error calling Gemini: {e}")
        
        return None
