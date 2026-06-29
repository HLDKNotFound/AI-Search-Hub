from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL

repl = PythonREPL()

@tool
def python_repl_tool(code: str) -> str:
    """
    A Python shell. Use this to execute Python commands.
    Input MUST be a valid Python script.
    If the output is an image or graph, ensure the code saves it to the specified directory.
    """

    return repl.run(code)