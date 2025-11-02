from IPython.display import Image, display
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from utils import format_messages

from file_tools import ls, read_file, write_file
from state import DeepAgentState

# Mock search result
search_result = """The Model Context Protocol (MCP) is an open standard protocol developed 
by Anthropic to enable seamless integration between AI models and external systems like 
tools, databases, and other services. It acts as a standardized communication layer, 
allowing AI models to access and utilize data from various sources in a consistent and 
efficient manner. Essentially, MCP simplifies the process of connecting AI assistants 
to external services by providing a unified language for data exchange. """


# Mock search tool
@tool(parse_docstring=True)
def web_search(
    query: str,
):
    """Search the web for information on a specific topic.

    This tool performs web searches and returns relevant results
    for the given query. Use this when you need to gather information from
    the internet about any topic.

    Args:
        query: The search query string. Be specific and clear about what
               information you're looking for.

    Returns:
        Search results from search engine.

    Example:
        web_search("machine learning applications in healthcare")
    """
    return search_result


FILE_USAGE_INSTRUCTIONS = """You have access to a virtual file system to help you retain and save context.                                  

## Workflow Process                                                                                            
1. **Orient**: Use ls() to see existing files before starting work                                             
2. **Save**: Use write_file() to store the user's request so that we can keep it for later                     
3. **Read**: Once you are satisfied with the collected sources, read the saved file and use it to ensure that you directly answer the user's question."""

# Add mock research instructions
SIMPLE_RESEARCH_INSTRUCTIONS = """IMPORTANT: Just make a single call to the web_search tool and use the result provided by the tool to answer the user's question."""

# Full prompt
INSTRUCTIONS = (
        FILE_USAGE_INSTRUCTIONS + "\n\n" + "=" * 80 + "\n\n" + SIMPLE_RESEARCH_INSTRUCTIONS
)


def call_file_agent():
    # Create agent using create_react_agent directly
    model = init_chat_model(model="google_genai:gemini-2.5-flash", temperature=0.0)
    tools = [ls, read_file, write_file, web_search]

    # Create agent with system prompt
    agent = create_react_agent(
        model, tools, prompt=INSTRUCTIONS, state_schema=DeepAgentState
    )

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Give me an overview of Model Context Protocol (MCP).",
                }
            ],
            "files": {},
        }
    )
    format_messages(result["messages"])