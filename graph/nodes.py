from langgraph.graph import StateGraph

from agents.manager_agent import manager_node
from agents.paper_agent import paper_agent_node
from agents.web_agent import web_agent_node
# from agents.visual_agent import visual_node
from agents.writer_agent import writer_node
from agents.critic_agent import critic_node

def create_nodes(workflow: StateGraph):
    # Add all nodes to the workflow
    workflow.add_node("manager_agent", manager_node)
    workflow.add_node("web_agent", web_agent_node)
    workflow.add_node("paper_agent", paper_agent_node)
    # workflow.add_node("visual_agent", visual_node)
    workflow.add_node("writer_agent", writer_node)
    workflow.add_node("critic_agent", critic_node)