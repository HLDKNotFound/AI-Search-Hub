from graph.state import State
from typing import Literal

def route_critic(state: State) -> Literal[
    "web_agent", "paper_agent", "writer_agent"
]:
    feedback = state.get("critic_feedback")
    revisions = state.get("revision_count", 0)

    if revisions >= 3 or (feedback and feedback.is_passed):
        return "__end__"
    elif feedback.error_type == "needs_web_data":
        return "web_agent"
    elif feedback.error_type == "needs_paper_data":
        return "paper_agent"
    elif feedback.error_type == "format_error":
        return "writer_agent"
    
    return "__end__"