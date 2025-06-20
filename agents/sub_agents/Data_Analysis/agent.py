from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import FunctionTool
from agents.sub_agents.Data_Analysis.Data_Analysis_Insights_agent import DataAnalysisInsightsAgent
from agents.sub_agents.Data_Analysis.prompt import Data_Analysis_Insights_agent

# Instantiate the DataAnalysisInsightsAgent
data_analysis_agent_instance = DataAnalysisInsightsAgent()

# Wrapper for analyze_data to simplify the function signature for automatic function calling
def analyze_data_wrapper(data_sources: list[str]):
    """
    :param data_sources: List of data source identifiers (e.g., file paths, database URIs)
    """
    return data_analysis_agent_instance.analyze_data(data_sources)

# Wrapper for derive_insights to simplify the function signature for automatic function calling
def derive_insights_wrapper(query: str):
    return data_analysis_agent_instance.derive_insights(query)

# Wrapper for present_findings to simplify the function signature for automatic function calling
def present_findings_wrapper(audience: str, format: str = "summary"):
    return data_analysis_agent_instance.present_findings(audience, format=format)

# Define tools using FunctionTool (not AgentTool)
analyze_data_tool = FunctionTool(
    func=analyze_data_wrapper
)

derive_insights_tool = FunctionTool(
    func=derive_insights_wrapper
)

present_findings_tool = FunctionTool(
    func=present_findings_wrapper
)

# Define the Data Analysis & Insights Agent
Data_analysis_insights_agent = Agent(
    model="gemini-2.0-flash",
    name="data_analysis_insights_agent",
    instruction=Data_Analysis_Insights_agent,
    description="Performs autonomous data analysis, insight derivation, and collaborative presentation of findings.",
    tools=[
        analyze_data_tool,
        derive_insights_tool,
        present_findings_tool
    ]
)
