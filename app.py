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

# -------------------------------
# DATA LOADING
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("monthly_exchange_rates (1).csv")
    df['Month'] = pd.to_datetime(df['Month'])
    return df

df = load_data()
currencies = ['AUD_LKR', 'GBP_LKR', 'JPY_LKR', 'KWD_LKR', 'USD_LKR']

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Jump to section:",
    [
        "Home",
        "Trends Overview",
        "Currency Insights",
        "Volatility & Stability",
        "Data Table & Download"
    ]
)

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":
    st.markdown(
        """
        <style>
        .hero-banner {
            position: relative;
            background-image: url('https://raw.githubusercontent.com/taniamotha/DSPL-INDIVIDUAL/main/global-currency-background_115579-405.avif');
            background-size: cover;
            background-position: center;
            height: 300px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 2rem;
            border-radius: 12px;
        }
        .hero-text {
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
        }
        </style>

        <div class="hero-banner">
            <div class="hero-text">Sri Lanka Exchange Rate Dashboard</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("##### Empowering policy decisions through global FX insights")

    st.subheader("Project Purpose")
    st.write("This dashboard helps Sri Lankan government officials monitor and analyze historical currency exchange rate trends for key global currencies.")

    st.subheader("Key Features")
    st.markdown("""
    - Interactive exchange rate visualizations (2000–2025)  
    - Country-specific currency insights  
    - Volatility and stability comparisons  
    - Exportable historical data  
    """)

    st.subheader("Intended Users")
    st.markdown("""
    - Government economists  
    - Policy advisors  
    - Financial regulators  
    - Academic researchers
    """)

    st.subheader("Data Source")
    st.markdown("""
    - [Central Bank of Sri Lanka](https://www.cbsl.gov.lk/rates-and-indicators/exchange-rates/daily-indicative-exchange-rates)  
    - Monthly averaged rates (2000–2025)
    """)

    st.subheader("Disclaimer")
    st.write("This dashboard is for academic purposes and may not reflect real-time exchange rate fluctuations.")
# -------------------------------
# TRENDS OVERVIEW
# -------------------------------
elif page == "Trends Overview":
    st.header("Trends Overview")

    st.subheader("1. Average Exchange Rate (2000–2025)")
    avg_rates = df[currencies].mean().reset_index()
    avg_rates.columns = ['Currency', 'Average Rate']
    bar_fig = px.bar(avg_rates, x='Currency', y='Average Rate', color='Currency',
                     title='Average Exchange Rate vs. LKR (2000–2025)', template='plotly_white')
    st.plotly_chart(bar_fig, use_container_width=True)

    st.subheader("2. Cumulative Currency Movement Over Time")
    df_melted = df.melt(id_vars='Month', var_name='Currency', value_name='Rate')
    area_fig = px.area(df_melted, x='Month', y='Rate', color='Currency',
                       title='Cumulative Exchange Rate Trends (2000–2025)', template='plotly_white')
    st.plotly_chart(area_fig, use_container_width=True)

    st.subheader("3. Currency Contribution to Overall Exchange Rate")
    avg_total = df_melted.groupby('Currency')['Rate'].mean().reset_index()
    pie_fig = px.pie(avg_total, names='Currency', values='Rate',
                     title='Average Contribution by Currency (2000–2025)', template='plotly_white', hole=0.4)
    st.plotly_chart(pie_fig, use_container_width=True)