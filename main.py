import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model = os.getenv("AZURE_OPENAI_DEPLOYMENT"), 
    base_url = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
)

def main():
    pass

if __name__ == "__main__":
    main()