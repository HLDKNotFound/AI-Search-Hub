import os
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import create_agent
from agents import get_llm
from config.prompts import visual_prompt
from config.settings import chart_path

def create_visual_agent_chain():
    llm = get_llm(temperature=0)
    tools = [PythonREPLTool()]

    visual_agent = create_agent(
        model=llm,
        tools=tools,
    )

    return visual_prompt | visual_agent

def visual_node(state: dict) -> dict:
    research_data = "\n".join(state.get("research_data", []))

    if not research_data:
        return {"visual_assets": []}
    
    visual_agent = create_visual_agent_chain()

    os.makedirs(chart_path, exist_ok=True)

    response = visual_agent.invoke({
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
