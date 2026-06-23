from langgraph.graph import StateGraph
from agents import (
    manager_agent_node,
    web_agent_node,
    paper_agent_node,
    visual_agent_node,
    writer_agent_node,
    critic_agent_node
)

def create_nodes(workflow: StateGraph):
    # Add all nodes to the workflow
    workflow.add_node("manager_agent", manager_agent_node)
    workflow.add_node("web_agent", web_agent_node)
    workflow.add_node("paper_agent", paper_agent_node)
    workflow.add_node("visual_agent", visual_agent_node)
    workflow.add_node("writer_agent", writer_agent_node)
    workflow.add_node("critic_agent", critic_agent_node)