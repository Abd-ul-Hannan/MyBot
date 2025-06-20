from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import FunctionTool
from agents.sub_agents.Content_Creation_Generation.Content_Creation_Generation import ContentCreationGenerationAgent
from agents.sub_agents.Content_Creation_Generation.prompt import Content_Creation_Generation

# Instantiate the ContentCreationGenerationAgent
content_creation_agent_instance = ContentCreationGenerationAgent()

# Define tools using FunctionTool (not AgentTool)
generate_marketing_material_tool = FunctionTool(
    func=content_creation_agent_instance.generate_marketing_material
)

generate_report_tool = FunctionTool(
    func=content_creation_agent_instance.generate_report
)

generate_code_tool = FunctionTool(
    func=content_creation_agent_instance.generate_code
)

improve_code_tool = FunctionTool(
    func=content_creation_agent_instance.improve_code
)

generate_code_from_text_tool = FunctionTool(
    func=content_creation_agent_instance.generate_code_from_text
)

analyze_link_tool = FunctionTool(
    func=content_creation_agent_instance.analyze_link
)

google_search_link_tool = FunctionTool(
    func=content_creation_agent_instance.google_search_link
)

# Define the Content Creation & Generation Agent
Content_creation_generation_agent = Agent(
    model="gemini-2.0-flash",
    name="content_creation_generation_agent",
    instruction=Content_Creation_Generation,
    description="Generates marketing materials, reports, code, and improves or generates code from text using advanced orchestration.",
    tools=[
        generate_marketing_material_tool,
        generate_report_tool,
        generate_code_tool,
        improve_code_tool,
        generate_code_from_text_tool,
        analyze_link_tool,
        google_search_link_tool
    ]
)
