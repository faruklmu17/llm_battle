
from groq import Groq
import re
from .base import BasePlayer
from src.utils.retries import retry_with_backoff

class GroqPlayer(BasePlayer):
    def __init__(self, model_name, api_key):
        super().__init__(model_name)
        self.client = Groq(api_key=api_key)
        self.model_id = model_name

    def get_move(self, game_state_prompt):
        def call_api():
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional Tic-Tac-Toe player. You MUST pick a move that is currently available. Respond with ONLY the number (0-8) and nothing else."
                    },
                    {
                        "role": "user",
                        "content": game_state_prompt,
                    }
                ],
                model=self.model_id,
            )
            return chat_completion.choices[0].message.content.strip()

        try:
            text = retry_with_backoff(call_api)
            if not text: return None
            
            # Extract digits
            match = re.search(r'\d', text)
            if match:
                return int(match.group())
        except Exception as e:
            print(f"Error calling Groq: {e}")
            
        return None
