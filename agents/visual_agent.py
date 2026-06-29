import os
from langchain.agents import create_agent
from agents import get_llm
from config import visual_prompt
from config.settings import chart_path

from tools import python_repl_tool

def create_visual_agent_chain():
    llm = get_llm(temperature=0)

    tools = [python_repl_tool]

    visual_agent = create_agent(
        model=llm,
        tools=tools,
    )

    return visual_prompt | visual_agent

def visual_agent_node(state: dict) -> dict:
    research_data = "\n".join(state.get("research_data", []))

    if not research_data:
        return {"visual_assets": []}
    
    visual_agent = create_visual_agent_chain()

    file_name = "chart.png"
    file_path = os.path.join(chart_path, file_name)
    os.makedirs(chart_path, exist_ok=True)

    if os.path.exists(file_path):
        os.remove(file_path)

    response = visual_agent.invoke({
        "research_data": research_data,
        "chart_path": chart_path
    })
    print(response)
    chart_description = response["messages"][-1].content

    visual_assets_update = []

    if os.path.exists(file_path):
        visual_assets_update.append(
            file_path
        )
    else:
        print(f"Warning: Chart file was not generated at {file_path}")

    return {
        "visual_assets": visual_assets_update,
        "chart_description": chart_description
    }
