import streamlit as st
import pandas as pd
import plotly.express as px
# -------------------------------
# PAGE CONFIG & THEME CUSTOMIZATION
# -------------------------------
st.set_page_config(
    page_title="Sri Lanka FX Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: white !important;
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #444444 !important;
    }

    /* Sidebar elements */
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Headings: dark grey */
    h1, h2, h3, h4, h5, h6 {
        color: #333333 !important;
    }

    /* Body text: medium grey */
    .stMarkdown, .markdown-text-container, .stText, p, .css-ffhzg2 {
        color: #555555 !important;
    }

    /* Widget labels (outside sidebar) */
    label, .stSelectbox label, .stRadio label {
        color: #555555 !important;
    }

    /* Button text */
    .stButton > button {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

