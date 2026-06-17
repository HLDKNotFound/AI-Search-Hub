from typing import TypedDict, List, Annotated, Literal
import operator
from pydantic import BaseModel, Field

# ==========================================
# 1. PYDANTIC MODELS
# ==========================================

class Task(BaseModel):
    task_id: int = Field(
        description="ID of the task."
    )
    description: str = Field(
        description="Detailed demonstration about the task."
    )
    agent_assignee: Literal["web_agent", "paper_agent"] = Field(
        description="Agent's name to assign this task."
    )

class ResearchPlan(BaseModel):
    objective: str = Field(
        description="Core object to query."
    )
    tasks: List[Task] = Field(
        description="List of the tasks to do."
    )

class CriticFeedback(BaseModel):
    is_passed: bool = Field(
        description="True if the report is satisfied, otherwrite False."
    )
    feedback: str = Field(
        description="Details about the error or unsatisfied data."
    )
    error_type: Literal["needs_web_data", "needs_paper_data", "format_error"] = Field(
        description="Error type: need web data, need paper data or format error"
    )

#===========================================
# 2. GRAPH STATE 
# ==========================================

class State(TypedDict):
    original_query: str 
    plan: ResearchPlan

    research_data: Annotated[List[str], operator.add]
    visual_assert: Annotated[List[str], operator.add]

    draft_report: str # markdown
    critic_feedback: CriticFeedback
    revision_count: int

