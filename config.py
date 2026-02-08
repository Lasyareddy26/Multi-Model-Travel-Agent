import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_KEYS = [os.getenv("GEMINI_KEY_1")]
    GROQ_KEYS = [os.getenv("GROQ_KEY_1")]
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    
    # Flash is faster and has higher free-tier limits
    SMART_MODELS = ["gemini/gemini-2.5-flash"] 
    FAST_MODELS = ["groq/llama-3.3-70b-versatile"]
    
    PROMPT_DIR = Path("prompts")

    @staticmethod
    def load_prompt(filename):
        path = Config.PROMPT_DIR / filename
        return path.read_text(encoding="utf-8") if path.exists() else "{input}"