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

        if "draft_report" in value:
            final_draft = value["draft_report"]

print("\n" + "="*20 + " FINAL DRAFT " + "="*20)

print(final_draft)