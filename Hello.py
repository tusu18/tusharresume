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

cal_pic = Image.open(calvpic)
startup_pic = Image.open(startuppic)
htmldyn_pic = Image.open(htmldynamic)
profile_pic = Image.open(profile)

# Constants
NAME = "Tushar Singh"
DESC = """I am a Software Developer with 3 years of experience as an ML Engineer and Researcher, grounded in Electronics Engineering and driven by a passion for AI. Specializing in NLP, Reinforcement Learning, AGI, and Computer Vision, I love solving complex challenges and creating innovative solutions."""
EMAIL = "📬tsingh98@umd.edu"
MEDIA_SOC = {
    "🤖 GitHub": "https://github.com/tusu18",
    "🏢 LinkedIn": "https://www.linkedin.com/in/tushar-singh-4326b7188/",
    "✅ Phone no": "+1-240-462-8779"
}

# Page configuration
st.set_page_config(page_title="Tushar Singh", page_icon=":technologist:", layout="wide")

# Load CSS
with open(cssfile) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Add Spotify-like animation and styling
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

# Typewriter effect function
def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

# Home page
def home_page():
    st.markdown("""
    <div class="home-container">
        <button class="play-button" onclick="start_portfolio()">Let's Play Tushar Singh Portfolio</button>
    </div>
    <script>
    function start_portfolio() {
        document.querySelector('.home-container').style.display = 'none';
        document.querySelector('.stApp').style.opacity = '1';
        setTimeout(() => {
            window.location.href = window.location.href + '?show_main_content=true';
        }, 1000);
    }
    </script>
    """, unsafe_allow_html=True)

# Main content
def main_content():
    # Navigation buttons
    button_text = "Home🏚️", "MyNotes📒", "Blogs📃", "Data👜"
    for text, col in zip(button_text, st.columns(len(button_text))):
        if col.button(text):
            switch_page(text.split('️')[0])

    # Profile section
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=220)
    with col2:
        st.title(NAME)
        typewriter(text=DESC, speed=14)
        with open(resume_f, "rb") as pdf:
            st.download_button(
                label="Download Resume",
                data=pdf.read(),
                file_name=resume_f.name,
                mime="application/octet-stream",
            )
        st.write(EMAIL)

    # Social media links
    st.write("#")
    cols = st.columns(len(MEDIA_SOC))
    for index, (plt, link) in enumerate(MEDIA_SOC.items()):
        if plt == "✅ Phone no":
            cols[index].write(f"[{plt}](tel:{link})")
        else:
            cols[index].write(f"[{plt}]({link})")

    # Experience section
    st.write("#")
    st.subheader("Experience💼")
    with st.expander("View Experience"):
        st.markdown("""
        <div class="tile">
        🔵 Tata Consultancy Services Ltd(2021-2024): SDE/Researcher
        
        **Automated Cheque Signature Verification**:
        - 🔸 Designed and implemented a robust cheque signature verification system.
        - 🔸 Achieved an **Equal Error Rate (EER)** reduction to **2.4%**.
        - 🔸 Decreased manual intervention by **40%** using **Convolutional Neural Networks (CNNs)** and **image enhancement algorithms**.
        
        **TableNet 2.0**:
        - 🔸 Contributed to **TableNet 2.0**, achieving precision scores of **0.97** for table detection and **0.94** for table extraction and structure detection.
        - 🔸 Addressed challenges with both bordered and borderless tables using advanced deep learning models.
        - 🔸 Documented findings in a white paper and deployed the solution as part of the TCS AI module for clients including **Assa Abloy** and **Bosch**.
        </div>
        """, unsafe_allow_html=True)

    # Skills section
    st.write("#")
    st.subheader("Skills 🏅")
    with st.expander("View Skills"):
        st.markdown("""
        <div class="tile">
        🔵 Python, ML, DL, GenAI, Java, OpenCV, Azure, Jenkins, Scala, RestApi, AWS, C++, Flask, SQL, Data Science, GAN, YOLO, Scrapy, SpringBoot, Statistics, Theano, Apache Spark, DSA, Heroku, Streamlit, Tableau
        </div>
        """, unsafe_allow_html=True)

    # Projects section
    st.write("#")
    st.subheader("Projects 📁")
    projects = {
        "Alambana": ["""Developing a multilingual voice-enabled solution powered by Large Language Models (LLMs), incorporating Whisper and Wav2Vec for accurate Automatic Speech Recognition (ASR) across multiple languages.""", "", ""],
        "DCGenerator": ["""Developing a framework to convert hand-drawn POC sketches or images of app designs into deployable websites by integrating state-of-the-art AI models and techniques.""", "", htmldyn_pic],
        "CALVISION": ["""A system that eliminates the need for manual data entry in calorie calculation, using computer vision and deep learning to estimate food volume and calories from images or short videos.""", "https://www.linkedin.com/feed/update/urn:li:activity:6731645057734082560/", cal_pic],
        "Pratbhimbh": ["""Implemented a T5 model using the RASA framework to create an advanced bot for initial mentoring and Q&A support on government policies and procedures.""", "https://github.com/tusu18/startup_bot", startup_pic],
    }
    
    for project, details in projects.items():
        with st.expander(project):
            st.markdown(f"""
            <div class="tile">
            <h3>{project}</h3>
            {details[0]}
            {'<br><a href="' + details[1] + '">Project Link</a>' if details[1] else ''}
            </div>
            """, unsafe_allow_html=True)
            if details[2]:
                st.image(details[2], use_column_width=True)

    # Book suggestion section
    st.write("#")
    st.subheader("Book Suggestion 📖")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Just Type Hi for a book suggestion!"):
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = random.choice([
                "The Tipping Point", "Dark Matter", "The Guest List", "Chip War",
                "The Outliers", "Deception Point", "Sapiens", "Start With Why",
                "Chanakya Chants", "And Then There Were None", "Freakonomics",
                "Think Fast and Slow", "Recursion", "Project Hail Mary",
                "One of Us is Lying", "Sharp Objects", "Shoe Dog",
                "Thinking Fast and Slow", "Drive", "Hooked", "Influence",
                "SuperIntelligence", "Founders at Work"
            ])

            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

# Main app logic
if 'show_main_content' not in st.session_state:
    st.session_state.show_main_content = False

if not st.session_state.show_main_content:
    home_page()
else:
    main_content()

# Check URL parameters to show main content
import streamlit.components.v1 as components
components.html(
    """
    <script>
    const urlParams = new URLSearchParams(window.location.search);
    const showMainContent = urlParams.get('show_main_content');
    if (showMainContent === 'true') {
        window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*');
    }
    </script>
    """,
    height=0,
)

if 'show_main_content' in st.experimental_get_query_params():
    st.session_state.show_main_content = True
