"""
Configuration helper for the Day22 Lab.
Loads environment variables and provides shared configuration.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def get_config():
    """Return configuration dictionary."""
    return {
        "langchain_tracing_v2": os.getenv("LANGCHAIN_TRACING_V2", "true"),
        "langchain_api_key": os.getenv("LANGCHAIN_API_KEY"),
        "langchain_project": os.getenv("LANGCHAIN_PROJECT", "day22-langsmith-lab"),
        "langchain_endpoint": os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com"),
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "openai_base_url": os.getenv("OPENAI_BASE_URL"),
        "openai_model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "embedding_model": os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
    }

if __name__ == "__main__":
    config = get_config()
    print("✅ Config loaded successfully")
    print(f"   LangSmith project : {config['langchain_project']}")
    print(f"   OpenAI endpoint   : {config['openai_base_url']}")
    print(f"   Default LLM model : {config['openai_model']}")
    print(f"   Embedding model   : {config['embedding_model']}")
