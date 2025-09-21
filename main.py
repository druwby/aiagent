import os
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(model="openai/gpt-4o-mini", base_url="https://models.github.ai/inference", api_key=os.getenv("GITHUB_TOKEN"))
    ##model = OpenAI(temperature=0, base_url="https://models.github.ai/inference", api_key=os.getenv("GITHUB_TOKEN"))

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("AI Assistant Activated. Type 'quit' to exit.")
    print("You can ask me to calculate something or just chat.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()