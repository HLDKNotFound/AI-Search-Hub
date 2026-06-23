from agents import get_llm
from tools import lance_search
from config import paper_prompt

from langchain.agents import create_agent

def create_paper_agent_chain():
    llm = get_llm(temperature=0)
    tools = [lance_search]

    agent_with_tool = create_agent(
        model=llm,
        tools=tools
    )

    return paper_prompt | agent_with_tool

def paper_agent_node(state: dict) -> dict:
    plan = state.get("plan")
    paper_tasks = [
        task for task in plan.tasks if task.agent_assignee == "paper_agent"
    ]
    if not paper_tasks:
        return {
            "research_data": []
        }
    
    chain = create_paper_agent_chain()
    response = chain.invoke({
        "objective": plan.objective,
        "tasks": "\n".join([t.description for t in paper_tasks])
    })

    search_result = response["messages"][-1].content
    
    return {
        "research_data": [f"[PAPER DATA]: {search_result}"]
    }
