from agents import get_llm
from tools import tavily_search
from config import web_prompt

from langchain.agents import create_agent

def create_web_agent_chain():
    llm = get_llm(temperature=0)
    tools = [tavily_search]

    agent_with_tools = create_agent(
        model=llm,
        tools=tools
    )

    return web_prompt | agent_with_tools

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
    
    search_result = response["messages"][-1].content
    
    return {
        "research_data": [f"[WEB DATA]: {search_result}"]
    }