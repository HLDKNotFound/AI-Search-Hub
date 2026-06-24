from graph import app
from dotenv import load_dotenv
from scripts import ingest_paper

load_dotenv()

query = input("original query: ")

inputs = {
    "original_query": query
}

sample_pdf = "data/input/Summary.pdf"
ingest_paper(sample_pdf, "Pdf_file")

for output in app.stream(inputs):
    for key, value in output.items():
        print(f"Node: {key}")
        print(value)
        print("-" * 50)

        if "draft_report" in value:
            final_draft = value["draft_report"]

print("\n" + "="*20 + " FINAL DRAFT " + "="*20)


if final_draft:
    print(final_draft)
    with open("result.md", "w", encoding="utf-8") as f:
        f.write(final_draft)