from langchain.messages import SystemMessage, HumanMessage
from graph.state import ResearchPlan
from config.prompts import manager_prompt
from agents import get_llm

def create_manager_chain():
    llm = get_llm(temperature=0)
    structured_llm = llm.with_structured_output(
        ResearchPlan
    )

    return manager_prompt | structured_llm

def manager_node(state: dict) -> dict:
    chain = create_manager_chain()
    plan = chain.invoke({
        "original_query": state["original_query"]
    })
    
    return {
        "plan": plan
    }