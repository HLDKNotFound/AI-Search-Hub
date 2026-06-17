from graph import app
from dotenv import load_dotenv

load_dotenv()

query = input("original query: ")

inputs = {
    "original_query": query
}

for output in app.stream(inputs):
    for key, value in output.items():
        print(f"Node: {key}")
        print(value)
        print("-" * 50)