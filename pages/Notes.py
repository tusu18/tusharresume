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
button_text = "Home", "MyNotes", "Blogs","Data"

for text, col in zip(button_text, st.columns(len(button_text))):
    if col.button(text):
        st.write("#")
st.subheader("Notes")
st.write("""
         
         ML Docs
         
         """
    
) 