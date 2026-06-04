import streamlit as st
from exa_py import Exa

# 1. Page Configuration
st.set_page_config(page_title="My Cute Exa Search Engine", page_icon="🌸", layout="centered")

# 2. Injecting Cute CSS Styles (Pastel colors, rounded corners, and animations)
st.markdown("""
    <style>
    /* Change the main website background to a soft pastel pink/purple gradient */
    .stApp {
        background: linear-gradient(135deg, #FFF0F5 0%, #E6E6FA 100%);
    }
    
    /* Style the text input box */
    div.stTextInput > div > div > input {
        border: 2px solid #FFB6C1 !important;
        border-radius: 20px !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
        background-color: #ffadd6 !important;
        color: #000000 !important;
        box-shadow: 0px 4px 10px rgba(255, 182, 193, 0.2);
    }
    
    /* Make the text box glow pink when clicked */
    div.stTextInput > div > div > input:focus {
        border-color: #FF69B4 !important;
        box-shadow: 0px 4px 15px rgba(255, 105, 180, 0.4) !important;
    }
    
    /* Style the Search Button */
    div.stButton > button {
        background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 20px !important;
        padding: 10px 30px !important;
        border: none !important;
        box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    
    /* Button hover animation */
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0px 6px 15px rgba(255, 105, 180, 0.5) !important;
    }
    
    /* Style for individual result cards */
    .result-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border-left: 5px solid #FF69B4;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.03);
    }
    
    .result-title a {
        color: #FF1493 !important;
        text-decoration: none !important;
        font-size: 18px;
        font-weight: bold;
    }
    
    .result-title a:hover {
        text-decoration: underline !important;
        color: #DB7093 !important;
    }
    
    .result-url {
        color: #BA55D3 !important;
        font-size: 13px;
        word-break: break-all;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Headers and Title
st.markdown("<h1 style='text-align: center; color: #FF69B4; font-family: Coding, sans-serif; margin-bottom: 0;'>🎀 Custom Search Engine 🎀</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8B008B; font-style: italic; margin-top: 0;'>Powered beautifully by the Exa API ✨</p>", unsafe_allow_html=True)

# 4. Initialize Exa Client
exa = Exa('EXA_API_KEY')

# 5. Search input
query = st.text_input("", placeholder="🔍 type something magical here...")

# 6. Search execution
if st.button("✨ Search the Web ✨"):
    if query:
        st.markdown(f"<h3 style='color: #FF69B4;'>🌸 Results for: <i>{query}</i></h3>", unsafe_allow_html=True)
        
        # Pull logic safely from Exa
        response = exa.search(
            query,
            num_results=10,
            type='keyword',
        )
        
        # Displaying results inside beautiful custom HTML cards
        for result in response.results:
            title = result.title if result.title else "Untitled Magical Page"
            
            card_html = f"""
            <div class="result-card">
                <div class="result-title"><a href="{result.url}" target="_blank">🔗 {title}</a></div>
                <div class="result-url">{result.url}</div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
    else:
        st.markdown("<p style='color: #FF69B4; font-weight: bold;'>Please type a query first! 💕</p>", unsafe_allow_html=True)