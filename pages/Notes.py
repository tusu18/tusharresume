from pathlib import Path
import streamlit as st
from PIL import Image
import numpy as np
import time
#from streamlit_option_menu import option_menu
TITLE= "MyNotes"
Page_IC= "📁"
NAME= "Notes"
curr_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
cssfile=curr_dir / "main.css"
st.set_page_config(page_title=TITLE, page_icon=Page_IC)
with open(cssfile) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

#from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.switch_page_button import switch_page


button_text = "Home🏚️", "MyNotes📒", "Blogs📃","Data👜"

for text, col in zip(button_text, st.columns(len(button_text))):
    if col.button(text):
        if text=="Home🏚️":
            switch_page("Hello")
        elif text == "Blogs📃":
            switch_page("Blog")
        elif text == "MyNotes📒":
            switch_page("Notes")
        elif text == "Data👜":
            switch_page("Data")   
st.subheader("Notes")
st.write("#")
st.write("Computer Vision Series")
st.video('https://www.youtube.com/watch?v=8jXIAWg_yHU&list=PLjMXczUzEYcHvw5YYSU92WrY8IwhTuq7p&ab_channel=JosephRedmon')
st.write("#")
st.write("NLP Walkthrough Series")
st.video('https://www.youtube.com/watch?v=rmVRLeJRkl4&list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ&ab_channel=StanfordOnline')
st.write("#")
st.write("MLops Series")
st.video('https://www.youtube.com/watch?v=NgWujOrCZFo&list=PLkDaE6sCZn6GMoA0wbpJLi3t34Gd8l0aK&ab_channel=DeepLearningAI')
st.write("#")
st.write("ML System Design Series")
st.video('https://www.youtube.com/watch?v=OEiNnfdxBRE&list=PLSrTvUm384I9PV10koj_cqit9OfbJXEkq&index=1&ab_channel=StanfordMLSysSeminars')
st.write("#")
st.write("RL Series By Prof Sergey Levine")
st.video('https://www.youtube.com/watch?v=JHrlF10v2Og&list=PL_iWQOsE6TfXxKgI1GgyV1B_Xa0DxE5eH&index=1&ab_channel=RAIL')
st.write("#")
st.write("RL Series by Prof Steve")
st.video('https://www.youtube.com/watch?v=0MNVhXEX9to&list=PLMrJAkhIeNNQe1JXNvaFvURxGY4gE9k74&ab_channel=SteveBrunton')
st.write("#")
st.write("RL Series NPTEL")
st.video('https://www.youtube.com/watch?v=YaPSPu7K9S0&list=PLEAYkSg4uSQ0Hkv_1LHlJtC_wqwVu6RQX&ab_channel=ReinforcementLearning')
st.write("#")
st.write("Quantum Machine Learning")
st.video('https://www.youtube.com/watch?v=QtWCmO_KIlg&list=PLmRxgFnCIhaMgvot-Xuym_hn69lmzIokg&ab_channel=QuantumML')
st.write("#")
st.write("ML With Maths R,Python Series")
st.video('https://www.youtube.com/watch?v=vStJoetOxJg&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&ab_channel=DeepLearningAI')
st.write("#")
st.write("ML From Stat Lens Series")
st.video('https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&ab_channel=StatQuestwithJoshStarmer')
st.write("#")
st.write("Statistics In Depth Series")
st.video('https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&ab_channel=HarvardUniversity')

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)