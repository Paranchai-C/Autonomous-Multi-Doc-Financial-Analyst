import os
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from termcolor import colored
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv(override=True)

# ==============================================================================
# 1. Project Folders
# ==============================================================================
DATA_FOLDER = "data"
DB_FOLDER = "chroma_db"

# ==============================================================================
# 2. Dataset Configuration
# ==============================================================================
# Default file-to-key mapping. 
# Better yet, this could be moved to a config.json or scanned from folder.
FILES = {
    "apple": "FY24_Q4_Consolidated_Financial_Statements.pdf",
    "tesla": "tsla-20241231-gen.pdf"
}

def get_llm(temperature=0):
    """Call OpenAI LLM"""
    return ChatOpenAI(
        model="gpt-4o-mini", # chaneg model
        temperature=temperature,
        api_key=os.getenv("OPENAI_API_KEY")
    )

def get_embeddings():
    """เรียกใช้งาน OpenAI Embeddings"""
    return OpenAIEmbeddings(
        model="text-embedding-3-small", #  text-embedding-3-large
        api_key=os.getenv("OPENAI_API_KEY")
    )