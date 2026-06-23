from graph.state import CriticFeedback
from agents import get_llm
from config import critic_prompt

def create_critic_chain():
    llm = get_llm(temperature=0)
    structured_llm = llm.with_structured_output(
        CriticFeedback
    )

    return critic_prompt | structured_llm

def critic_agent_node(state: dict) -> dict:
    chain = create_critic_chain()
    feedback = chain.invoke({
        "original_query": state["original_query"],
        "draft_report": state["draft_report"]
    })

    current_count = state.get("revision_count", 0) + 1

    return {
        "critic_feedback": feedback,
        "revision_count": current_count + 1
    }