
import time
import random

def retry_with_backoff(fn, max_retries=5, initial_delay=2):
    """
    Retries a function with exponential backoff.
    """
    delay = initial_delay
    for i in range(max_retries):
        try:
            return fn()
        except Exception as e:
            error_str = str(e).lower()
            # Only retry on rate limits or server overloads
            is_retryable = any(x in error_str for x in ["429", "too many requests", "503", "unavailable", "rate limit"])
            
            if is_retryable and i < max_retries - 1:
                wait_time = delay + random.uniform(0, 1) # Add jitter
                print(f"⚠️ API Busy/Rate Limited. Retrying in {wait_time:.1f}s... (Attempt {i+1}/{max_retries})")
                time.sleep(wait_time)
                delay *= 2 # Exponential increase
            else:
                # If not retryable or max retries reached, raise the original error
                raise e
    return None
