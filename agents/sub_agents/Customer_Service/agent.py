from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import FunctionTool
from agents.sub_agents.Customer_Service.Customer_Service_Engagement import CustomerServiceEngagementAgent
from agents.sub_agents.Customer_Service.prompt import Customer_Service_Engagement

# Instantiate the CustomerServiceEngagementAgent
customer_service_agent_instance = CustomerServiceEngagementAgent()

# Define tools using FunctionTool (not AgentTool)
engage_customer_tool = FunctionTool(
    func=customer_service_agent_instance.engage_customer
)

resolve_ticket_tool = FunctionTool(
    func=customer_service_agent_instance.resolve_ticket
)

provide_info_tool = FunctionTool(
    func=customer_service_agent_instance.provide_info
)

# Define the Customer Service Agent
Customer_service_agent = Agent(
    model="gemini-2.0-flash",
    name="customer_service_agent",
    instruction=Customer_Service_Engagement,
    description="Handles customer engagement, ticket resolution, and provides information.",
    tools=[
        engage_customer_tool,
        resolve_ticket_tool,
        provide_info_tool
    ]
)
