
import anthropic
import re
from .base import BasePlayer
from src.utils.retries import retry_with_backoff

class ClaudePlayer(BasePlayer):
    def __init__(self, model_name, api_key):
        super().__init__(model_name)
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model_id = model_name

    def get_move(self, game_state_prompt):
        def call_api():
            message = self.client.messages.create(
                model=self.model_id,
                max_tokens=10,
                system="You are a professional Tic-Tac-Toe player. Respond with ONLY the number (0-8) of your chosen move based on the board state. No chat, no explanation.",
                messages=[
                    {
                        "role": "user",
                        "content": game_state_prompt,
                    }
                ],
            )
            return message.content[0].text.strip()

        try:
            text = retry_with_backoff(call_api)
            if not text: return None
            
            # Extract digits
            match = re.search(r'\d', text)
            if match:
                return int(match.group())
        except Exception as e:
            print(f"Error calling Claude: {e}")
            
        return None
