from agents import get_llm
from config.prompts import writer_prompt

def create_writer_chain():
    llm = get_llm(temperature=0.1)

    return writer_prompt | llm

def writer_node(state: dict) -> dict:
    chain = create_writer_chain()

    original_query = state.get("original_query", "")
    research_data = "\n".join(state.get("research_data", []))
    visual_assets = "\n".join(state.get("visual_assets", []))
    feedback = state.get("feedback", "")

    response = chain.invoke({
        "origin_query": original_query,
        "research_data": research_data,
        "visual_asserts": visual_assets,
        "critic_feedback": feedback
    })

    return {
        "draft_report": response.content
    }