import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("vMjGre9u24YsXcX9Szn9vuXa0Wm8fQ3oWpp")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Uncomment for OpenAI

# LLM Configuration
LLM_PROVIDER = "groq"  # or "openai"
GROQ_MODEL = "openai/gpt-oss-120b"
# OPENAI_MODEL = "gpt-4-turbo-preview"  # Uncomment for OpenAI
LLM_TEMPERATURE = 0.2
MAX_TOKENS = 1024

# Embedding Configuration
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DIM = 384

# Text Splitting
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval
RETRIEVAL_K = 4
SIMILARITY_THRESHOLD = 0.7

# Database
DB_PATH = "rag_memory.db"
CHECKPOINT_PATH = "checkpoints.db"

# Token Pricing (USD per 1M tokens)
GROQ_PRICING = {"input": 0.27, "output": 0.27}  # Mixtral pricing
# OPENAI_PRICING = {"input": 10.0, "output": 30.0}  # GPT-4 Turbo pricing

# UI Configuration
PAGE_TITLE = "🤖 Advanced RAG with LangGraph"
PAGE_ICON = "🧠"
LAYOUT = "wide"