import os
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
#another way to implement - use inbuilt tavily search tool from langchain_tavily
from langchain_tavily import TavilySearch

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that search over internet
    args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(
    model = os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    base_url = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    temperature=0.7
)

tools = [search]

# Using the inbuilt TavilySearch tool from langchain_tavily
#tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("\n This is search agent demo")
    # LangSmith tracing is automatically enabled via LANGSMITH_TRACING=true in .env
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the Pune area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()