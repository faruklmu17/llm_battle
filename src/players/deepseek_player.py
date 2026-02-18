
from openai import OpenAI
import re
from .base import BasePlayer
from src.utils.retries import retry_with_backoff

class DeepSeekPlayer(BasePlayer):
    def __init__(self, model_name, api_key):
        super().__init__(model_name)
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.model_id = model_name

    def get_move(self, game_state_prompt):
        def call_api():
            response = self.client.chat.completions.create(
                model=self.model_id,
                messages=[
                    {"role": "system", "content": "You are a professional Tic-Tac-Toe player. Respond with ONLY the number (0-8) of your chosen move based on the board state. No chat, no explanation."},
                    {"role": "user", "content": game_state_prompt},
                ],
                max_tokens=10,
                stream=False
            )
            return response.choices[0].message.content.strip()

        try:
            text = retry_with_backoff(call_api)
            if not text: return None
            
            # Extract digits
            match = re.search(r'\d', text)
            if match:
                return int(match.group())
        except Exception as e:
            print(f"Error calling DeepSeek: {e}")
            
        return None
