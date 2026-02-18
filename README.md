# LLM Battle Arena: The Four-Way Clash 🏆

![Performance Chart](data/performance_chart.png)

An autonomous "AI Arena" where the world's most powerful Large Language Models (LLMs) compete in a strategic round-robin tournament. 

## ⚔️ The Contenders

This arena orchestrates battles between four distinct AI architectures:

1.  **Google Gemini**: The multimodal powerhouse (e.g., `gemini-flash-latest`).
2.  **Anthropic Claude**: The reasoned strategist (e.g., `claude-3-5-sonnet-20241022`).
3.  **DeepSeek**: The high-efficiency challenger (e.g., `deepseek-chat`).
4.  **Meta Llama (via Groq)**: The open-weights speedster (e.g., `llama-3.3-70b-versatile`).

---

## 🏗 How the Battle Works

The arena follows a strict **Orchestration Loop**:

1.  **State Extraction**: The `TicTacToe` engine generates a visual/textual representation of the board with numbered markers.
2.  **Strategic Prompting**: The system prompts the active AI to analyze the board and return **exactly one number** (0-8) for a winning move.
3.  **Validation & Retry**: 
    *   Models have **3 attempts** to provide a valid legal move.
    *   **Exponential Backoff** (2s, 4s, 8s...) ensures battles aren't lost to API rate limits or server "high demand" spikes.
4.  **Tracking**: Every match outcome is recorded in `data/stats.json` and visualized.

---

## 📊 Result Display & Tracking

*   **Live Console View**: Real-time board rendering and AI move logs.
*   **Historical Data**: A rolling window of the **last 50 matches** is maintained to ensure rankings reflect current model versions.
*   **Automatic Visualization**: After every match, a premium **Dark Mode** bar chart (see top) is updated to show Wins, Losses, and Draws.

---

## 🛠 Local Setup

### 1. Requirements
```bash
pip install google-genai anthropic openai groq matplotlib numpy python-dotenv
```

### 2. Configure Environment
Create a `.env` file with your API keys:
```env
GEMINI_API_KEY = your_key
CLAUDE_API_KEY = your_key
DEEPSEEK_API_KEY = your_key
GROQ_API_KEY = your_key
```

### 3. Start the Arena
```bash
python3 main.py
```

## 📅 Roadmap
- [x] **Phase 1**: Core Engine & Engine Verification
- [x] **Phase 2**: Multi-Model SDK Integration (Gemini, Claude, DeepSeek, Groq)
- [x] **Phase 2.5**: Automated Round-Robin Tournament Logic
- [ ] **Phase 3**: Chess-style Elo Rating System
- [ ] **Phase 4**: Advanced Strategic Games (Connect Four, Chess)
