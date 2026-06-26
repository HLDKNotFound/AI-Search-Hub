import streamlit as st
from dotenv import load_dotenv

# Ensure set_page_config is the first Streamlit command in the script
st.set_page_config(
    page_title="Report Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables from the .env file
load_dotenv()

# Import UI components after configuring the page
from .components.sidebar import render_sidebar
from .components.chat_engine import render_chat_engine

def render_UI():
    # Render the sidebar
    render_sidebar()

    # Render the main application interface
    render_chat_engine()