from google.adk.agents import Agent

from agents.sub_agents.Automation.agent import Automation_agent
from agents.sub_agents.Content_Creation_Generation.agent import Content_creation_generation_agent
from agents.sub_agents.Customer_Service.agent import Customer_service_agent
from agents.sub_agents.Data_Analysis.agent import Data_analysis_insights_agent
from agents.sub_agents.inspiration.agent import inspiration_agent

# Example 1: Simple built-in tool
from google.adk.tools.google_search_tool import google_search

# google_search_tool = FunctionTool(func=google_search)

# Example 2: Agent as a tool
from agents.tools.search import google_search_grounding

# Example 3: Function tool
from agents.tools.places import PlacesService
from google.adk.tools import FunctionTool
places_tool = FunctionTool(func=PlacesService().find_place_from_text)
from agents.prompt import ROOT_AGENT_INSTR

from agents.sub_agents.inspiration.agent import place_agent, news_agent
root_agent = Agent(
    model="gemini-2.0-flash-001",
    name="root_agent",
    description="agents",
    instruction=ROOT_AGENT_INSTR,
    tools=[places_tool],
    sub_agents=[
        inspiration_agent,
        Automation_agent,
      Content_creation_generation_agent,
      Customer_service_agent,
      Data_analysis_insights_agent

    ]
   
)