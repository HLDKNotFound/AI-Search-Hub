import streamlit as st
from graph import app

def render_chat_engine():
    st.title("AI Agent")
    st.caption("An intelligent system that analyzes requests and generates reports.")

    # Initialize session state if it doesn't exist
    if "final_draft" not in st.session_state:
        st.session_state["final_draft"] = None
    if "logs" not in st.session_state:
        st.session_state["logs"] = []

    # Query input
    query = st.text_input(
        "Enter your analysis request:",
        placeholder="e.g., Summarize somethings..."
    )

    if st.button(
        "Run Workflow",
        use_container_width=True,
        type="primary"
    ):
        if not query:
            st.error("Plase enter a query before running the workflow!")
            return
        
        # Reset previous logs and results
        st.session_state["logs"] = []
        st.session_state["final_draft"] = None

        inputs = {"original_query": query}

        st.subheader("🔄 Agent Processing")

        # Display workflow execution status
        with st.status(
            "The agent is processing your request through the workflow...",
            expanded=True
        ) as status:
            try:
                for output in app.stream(inputs):
                    for key, value in output.items():
                        log_msg = f" **Node:** `{key}`"
                        st.markdown(log_msg)

                        # Display node output in an expandable section
                        with st.expander(f"View data from {key}"):
                            st.json(value)
                        
                        # Store logs in session state
                        st.session_state["logs"].append((key, value))

                        # Save the final report if available
                        if "draft_report" in value:
                            st.session_state["final_draft"] = value["draft_report"]

                    status.update(
                        label="Workflow completed successfully!",
                        state="complete",
                        expanded=False
                    )
            
            except Exception as e:
                status.update(
                    label="An error occurred during workflow execution!",
                    state="error"
                )
                st.error(f"Error details: {str(e)}")

    if st.session_state["final_draft"]:
        st.markdown("---")
        st.header("FINAL REPORT")

        # Render Makrodwn report
        st.markdown(st.session_state["final_draft"])

        # Download button
        st.download_button(
            label="Download Report (.md)",
            data=st.session_state["final_draft"],
            file_name="result.md",
            mime="text/markdown",
            use_container_width=True
        )            