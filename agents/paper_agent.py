from agents import get_llm
from tools.document_tools import lance_search
from config.prompts import paper_prompt

def create_paper_agent_chain():
    llm = get_llm(temperature=0)
    llm_with_tool = llm.bind_tools(
        [lance_search]
    )

    return paper_prompt | llm_with_tool

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
        "core_objective": plan.core_objective,
        "tasks": "\n".join([t.description for t in paper_tasks])
    })

    return {
        "research_data": [f"[PAPER DATA]: {response.content}"]
    }
