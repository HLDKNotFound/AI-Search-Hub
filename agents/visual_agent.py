import os
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import create_agent, AgentExecutor
from agents import get_llm
from config.prompts import visual_prompt
from config.settings import chart_path

def create_visual_agent():
    llm = get_llm(temperature=0)
    tools = [PythonREPLTool()]

    agent = create_agent(
        llm=llm,
        tools=tools,
        prompt=visual_prompt
    )
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )

    return agent_executor

def visual_node(state: dict) -> dict:
    research_data = "\n".join(state.get("research_data", []))

    if not research_data:
        return {"visual_assets": []}
    
    agent_executor = create_visual_agent()

    os.makedirs(chart_path, exist_ok=True)
    response = agent_executor.invoke({
        "research_data": research_data,
        "chart_path": chart_path
    })

    visual_assets_update = []

    if os.path.exists(chart_path):
        visual_assets_update.append(
            chart_path
        )

    return {
        "visual_assets": visual_assets_update
    }
