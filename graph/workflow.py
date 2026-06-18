from langgraph.graph import StateGraph, START, END
from graph.state import State

from graph.nodes import create_nodes
from graph.edges import route_critic

def create_workflow():
    workflow = StateGraph(State)
    create_nodes(workflow)

    # Build adges
    workflow.add_edge(START, "manager_agent")

    # Fan-out: Manager Agent trigger 2 agent paralelly to collect data
    workflow.add_edge("manager_agent", "web_agent")
    workflow.add_edge("manager_agent", "paper_agent")
    
    # Fan-int: Wait for 2 collector agent then run Visaul Agent
    workflow.add_edge("web_agent", "visual_agent")
    workflow.add_edge("paper_agent", "visual_agent")

    workflow.add_edge("visual_agent", "writer_agent")
    workflow.add_edge("writer_agent", "critic_agent")

    # Conditional Edges to route Critic Agent
    workflow.add_conditional_edges(
        "critic_agent",
        route_critic,
        {
            "web_agent": "web_agent",           # Go to node "web_agent"
            "paper_agent": "paper_agent",       # Go to node "paper_agent"
            "writer_agent": "writer_agent",     # Go to node "writer_agent"
            "__end__": END                      # End the graph
        }
    )

    return workflow.compile()