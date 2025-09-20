from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("AI Assistant Activated. Type 'quit' to exit.")
    print("You can ask me to calculate something or just chat.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="")