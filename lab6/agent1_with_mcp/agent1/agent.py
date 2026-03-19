from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import StreamableHTTPConnectionParams, McpToolset

load_dotenv()
"""Creates an ADK Agent equipped with tools from the MCP Server."""
tools =  McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="http://localhost:8000/mcp",timeout=120.0
            ),
            # Optional: Filter which tools from the MCP server are exposed
            # tool_filter=['list_directory', 'read_file']
        )

root_agent = LlmAgent(
    name="weather_time_agent",
    model="gemini-2.5-flash-lite",
    description="Agent that provides weather and time information for cities.",
    instruction="You help users with time and weather information for various cities.",
    tools=[tools],
)
