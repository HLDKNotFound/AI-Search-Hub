import streamlit as st
import os
from vectorstore import ingest_db

def render_sidebar():
    with st.sidebar:
        st.title("⚙️ System Configuration")
        st.caption("Manage input documents and the vector database status")
        st.markdown("---")

    st.subheader("📄 Upload Document")
    uploaded_file = st.file_uploader("Select a PDF file to ingest", type=["pdf"])

    # Create the input directory if it doesn't exist
    os.makedirs("data.input", exist_ok=True)
    sample_pdf_path = "data/input/Sammary.pdf"

    if uploaded_file:
        # Save the uploaded file, replacing PDF
        with open(sample_pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Trigger the ingestion process
        if st.button(
            "Start Database Ingestion",
            use_container_width=True,
            type="primary"
        ):
            with st.spinner("ingesting data into the VectorStore..."):
                try:
                    ingest_db(sample_pdf_path)
                    st.session_state["db_ingested"] = True
                    st.sucess("Data ingested successfully!")
                except Exception as e:
                    st.error(f"Error during ingestion: {str(e)}")
        
    st.markdown("---")

    # Display the current database status
    if st.session_state.get("db_ingested", False):
        st.success("🟢 Status: Database is ready")
    else:
        st.warning("🟡 Status: No new data has been ingested")