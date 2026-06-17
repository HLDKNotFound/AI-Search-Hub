from agents import get_llm
from tools.search_tools import tavily_search
from config.prompts import web_prompt

def create_web_agent_chain():
    llm = get_llm(temperature=0)
    llm_with_tools = llm.bind_tools(
        [tavily_search]
    )

    return web_prompt | llm_with_tools

def web_agent_node(state: dict) -> dict:
    plan = state.get("plan")

    web_tasks = [
        task for task in plan.tasks if task.agent_assignee == "web_agent"
    ]
    if not web_tasks:
        return {
            "research_data": []
        }
    
    chain = create_web_agent_chain()
    response = chain.invoke({
        "objective": plan.objective,
        "tasks": "\n".join([t.description for t in web_tasks])
    })

    return {
        "research_data": [f"[WEB DATA]: {response.content}"]
    }