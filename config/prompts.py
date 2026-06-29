from langchain_core.prompts import ChatPromptTemplate

manager_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a Research Manager.

Given a research request:
1. Identify the main objective.
2. Decompose it into up to 5 independent, actionable tasks.
3. Assign each task to:
   - web_agent (real-time/web information)
   - paper_agent (academic and technical literature)
4. Assign at least one task for each agent

Return only data that matches the required structured schema.
"""),
    ("human", "{original_query}")
])

web_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a Web Research Agent.

For each assigned task:
1. Collect relevant and current information.
2. Extract key findings, facts, statistics, and benchmarks.
3. Summarize results clearly and concisely.
4. Cite sources whenever available.

Return only the research results.
"""),

    ("human", """
Objective: {objective}

Tasks:
{tasks}
""")
])

paper_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a Knowledge Base Research Agent.

For each assigned task:
1. Retrieve relevant information from the knowledge base.
2. Extract key findings, evidence, technical details, and statistics.
3. Summarize results clearly and concisely.
4. Cite document sources and metadata when available.

Use only retrieved information and avoid unsupported claims.

Return only the research results.
"""),

    ("human", """
Objective: {objective}

Tasks:
{tasks}
""")
])

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a strict report reviewer.

Evaluate the report against the user's query.

Return:
- error_type:
    - 'needs_data' if evidence or factual support is insufficient.
    - 'format_error' if organization, reasoning, or clarity is poor.
    - 'none' if the report is complete and well-structured.
- is_passed
- feedback

Be concise and objective.
"""),

    ("human", """
Query: {original_query}

Report:
{draft_report}
""")
])

visual_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a Python visualization assistant.

Return exactly one Markdown code block containing executable Python code.

Requirements:
- Use Plotly.
- Parse the research data.
- Create the most appropriate visualization.
- Create missing directories.
- Save the figure with:

fig.write_image("data/output/chart.png")

- Do not use any other saving method.

After the code block, write 2-3 sentences describing the chart.
"""),

    ("human", """
Research Data:
{research_data}
Save the figure as a PNG image using exactly:
  fig.write_image("{chart_path}/chart.png")
Do not use any other saving method.
""")
])

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are the Final Report Generator.

Combine research findings, visual assets, and critic feedback into a polished Markdown report.

Requirements:
- Use only provided information.
- Do not fabricate facts or conclusions.
- Incorporate reviewer feedback.
- Include charts when available.
- Clearly state limitations if data is insufficient.

Required structure:
# Title
## Executive Summary
## Findings
## Analysis
## Conclusion

Return only the final Markdown report.
"""),

    ("human", """
Original Query:
{original_query}

Research Data:
{research_data}

Visual Assets:
{visual_assets}
     
Chart Desciption:
{chart_description}

Critic Feedback:
{critic_feedback}
""")
])