import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

model = ChatOpenAI(model="gpt-4o-mini", openai_api_base="https://openrouter.ai/api/v1")

system = SystemMessage(content="You are a smart person")
messages = [system]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    messages.append(HumanMessage(content=user_input))
    result = model.invoke(messages)
    print("AI:", result.content)
    messages.append(AIMessage(content=result.content))
