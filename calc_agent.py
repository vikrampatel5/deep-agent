from langgraph.prebuilt import create_react_agent

from langchain_google_genai import ChatGoogleGenerativeAI
from agent_tools import calculator
from utils import format_messages

def call_calc_agent():

    SYSTEM_PROMPT = "You are a helpful arithmetic assistant who is an expert at using a calculator"

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)
    tools = [calculator]

    agent = create_react_agent(
        model,
        tools,
        prompt = SYSTEM_PROMPT
    ).with_config({"recursion_limit":20})

    result1 = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is 3 * 5?",
                }
            ],
        }
    )

    print(format_messages(result1["messages"]))