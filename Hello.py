import streamlit as st
from pathlib import Path
from PIL import Image
import time
import random
from streamlit_extras.switch_page_button import switch_page

# Set up paths and load images
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile = curr_dir / "data" / "PROF.png"
startuppic = curr_dir / "data" / "startupbotrec.png"
htmldynamic = curr_dir / "data" / "htmldynamicpic.jpg"
calvpic = curr_dir / "data" / "calvisbhendi.png"
cssfile = curr_dir / "styles" / "main.css"
resume_f = curr_dir / "data" / "Resume.pdf"

profile_pic = Image.open(profile)
startup_pic = Image.open(startuppic)
htmldyn_pic = Image.open(htmldynamic)
cal_pic = Image.open(calvpic)

# Constants
NAME = "Tushar Singh"
DESC = """Software Developer with 3 years of experience as an ML Engineer and Researcher. Specializing in NLP, Reinforcement Learning, AGI, and Computer Vision."""
EMAIL = "📬tsingh98@umd.edu"
MEDIA_SOC = {
    "🤖 GitHub": "https://github.com/tusu18",
    "🏢 LinkedIn": "https://www.linkedin.com/in/tushar-singh-4326b7188/",
    "✅ Phone": "+1-240-462-8779"
}

# Page configuration
st.set_page_config(page_title="Tushar Singh", page_icon=":technologist:", layout="wide")

# Load CSS
with open(cssfile) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Spotify-like theme and animations
st.markdown("""
<style>
body {
    background: linear-gradient(45deg, #1DB954, #191414);
    animation: gradientBG 15s ease infinite;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.stApp {
    opacity: 0;
    transition: opacity 1s ease-in-out;
}
.home-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.play-button {
    font-size: 24px;
    padding: 20px 40px;
    background-color: #1DB954;
    color: white;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
}
.play-button:hover {
    background-color: #1ED760;
    transform: scale(1.05);
}
.tile {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    transition: all 0.3s ease;
}
.tile:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# Main page
def main_page():
    st.markdown("""
    <div class="home-container">
        <button class="play-button" onclick="start_portfolio()">Let's Stream Tushar Singh Portfolio</button>
    </div>
    <script>
    function start_portfolio() {
        document.querySelector('.home-container').style.display = 'none';
        document.querySelector('.stApp').style.opacity = '1';
        setTimeout(() => {
            window.location.href = window.location.href + '?show_content=true';
        }, 1000);
    }
    </script>
    """, unsafe_allow_html=True)

# Content page
def content_page():
    # Navigation
    button_text = "Home🏚️", "Projects📁", "Skills🏅", "Experience💼"
    for text, col in zip(button_text, st.columns(len(button_text))):
        if col.button(text):
            switch_page(text.split('️')[0])

    # Profile section
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(profile_pic, width=220)
    with col2:
        st.title(NAME)
        st.write(DESC)
        st.download_button(
            label="Download Resume",
            data=open(resume_f, "rb").read(),
            file_name=resume_f.name,
            mime="application/octet-stream",
        )
        st.write(EMAIL)

    # Social media links
    cols = st.columns(len(MEDIA_SOC))
    for index, (platform, link) in enumerate(MEDIA_SOC.items()):
        cols[index].markdown(f"[{platform}]({link})")

    # Projects
    st.subheader("Featured Projects")
    projects = {
        "Alambana": "Multilingual voice-enabled LLM solution",
        "DCGenerator": "Convert hand-drawn sketches to websites",
        "CALVISION": "AI-powered calorie estimation from images",
        "Pratbhimbh": "Government policy Q&A bot with T5 model"
    }
    cols = st.columns(2)
    for i, (project, desc) in enumerate(projects.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="tile">
                <h3>{project}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    # Skills
    st.subheader("Top Skills")
    skills = ["Python", "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Reinforcement Learning"]
    for skill in skills:
        st.markdown(f"""
        <div class="tile">
            <h4>{skill}</h4>
        </div>
        """, unsafe_allow_html=True)

    # Book suggestion
    st.subheader("Book Suggestion 📖")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Type 'Hi' for a book suggestion!"):
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = random.choice([
                "The Tipping Point", "Dark Matter", "Sapiens", "Project Hail Mary",
                "Thinking Fast and Slow", "Recursion", "Shoe Dog", "Hooked"
            ])

            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

# Main app logic
if 'show_content' not in st.session_state:
    st.session_state.show_content = False

if not st.session_state.show_content:
    main_page()
else:
    content_page()

# Check URL parameters to show content
import streamlit.components.v1 as components
components.html(
    """
    <script>
    const urlParams = new URLSearchParams(window.location.search);
    const showContent = urlParams.get('show_content');
    if (showContent === 'true') {
        window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*');
    }
    </script>
    """,
    height=0,
)

if 'show_content' in st.experimental_get_query_params():
    st.session_state.show_content = True
