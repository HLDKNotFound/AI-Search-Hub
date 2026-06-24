from langchain.messages import SystemMessage, HumanMessage
from graph.state import ResearchPlan
from config import manager_prompt
from agents import get_llm

def create_manager_chain():
    llm = get_llm(
        temperature=0,
        max_tokens=8000
    )
    structured_llm = llm.with_structured_output(
        ResearchPlan
    )

    return manager_prompt | structured_llm

def manager_agent_node(state: dict) -> dict:
    chain = create_manager_chain()
    plan = chain.invoke({
        "original_query": state["original_query"]
    })
    
    return {
        "plan": plan
    }