from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import FunctionTool
from agents.sub_agents.Automation.automation_agent import AutomationAgent
from agents.sub_agents.Automation.prompt import Automation_Agent_Instruction

# Instantiate the AutomationAgent
automation_agent_instance = AutomationAgent()

# Define tools using FunctionTool (not AgentTool)
automate_business_process_tool = FunctionTool(
    func=automation_agent_instance.automate_business_process
)

manage_sdlc_tool = FunctionTool(
    func=automation_agent_instance.manage_software_development_lifecycle
)

handle_intricate_task_tool = FunctionTool(
    func=automation_agent_instance.handle_intricate_task
)

# Define the Automation Agent
Automation_agent = Agent(
    model="gemini-2.0-flash",
    name="automation_agent",
    instruction=Automation_Agent_Instruction,
    description="Automates business processes, SDLC stages, and intricate task management.",
    tools=[
        automate_business_process_tool,
        manage_sdlc_tool,
        handle_intricate_task_tool
    ]
)
