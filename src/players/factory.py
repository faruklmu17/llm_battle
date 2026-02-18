from .base import RandomPlayer
from .gemini_player import GeminiPlayer
from .groq_player import GroqPlayer
import os
from dotenv import load_dotenv

# Load keys from .env
load_dotenv()

def get_player(model_id: str):
    """
    This is the switching logic. You pass a name, and it returns the right model.
    """
    if model_id == "random":
        return RandomPlayer("random")
    
    elif "gemini" in model_id:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")
        return GeminiPlayer(model_id, api_key)
        
    elif "llama" in model_id or "mixtral" in model_id:
        # Assuming these are running via Groq for this project
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")
        return GroqPlayer(model_id, api_key)
        
    else:
        # Fallback to Groq if the ID looks like a Groq model name
        api_key = os.getenv("GROQ_API_KEY")
        if api_key and ("gemma" in model_id or "groq" in model_id):
             return GroqPlayer(model_id, api_key)
             
        raise ValueError(f"Unknown model: {model_id}")
