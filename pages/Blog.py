from pathlib import Path
import streamlit as st
from PIL import Image
import numpy as np
import time
#from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
curr_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
cssfile=curr_dir / "main.css"
TITLE= "Blogs"
Page_IC= "🤖"
NAME= "Blogs"
st.set_page_config(page_title=TITLE, page_icon=Page_IC)
with open(cssfile) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)


#from streamlit_extras.switch_page_button import switch_page
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
st.write("#")               
st.subheader("Important Blogs")            
st.link_button("Improve LLM responses in RAG use cases by interacting with the user","https://aws.amazon.com/blogs/machine-learning/improve-llm-responses-in-rag-use-cases-by-interacting-with-the-user/")
st.write("#")

 