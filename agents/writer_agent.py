from agents import get_llm
from config import writer_prompt

def create_writer_chain():
    llm = get_llm(temperature=0.1)

    return writer_prompt | llm

def writer_agent_node(state: dict) -> dict:
    chain = create_writer_chain()

    original_query = state.get("original_query", "")
    research_data = "\n".join(state.get("research_data", []))
    visual_assets = "\n".join(state.get("visual_assets", []))
    chart_description = state.get("chart_description", "")
    feedback = state.get("feedback", "")


    response = chain.invoke({
        "original_query": original_query,
        "research_data": research_data,
        "visual_assets": visual_assets,
        "chart_description": chart_description,
        "critic_feedback": feedback
    })

    return {
        "draft_report": response.content
    }