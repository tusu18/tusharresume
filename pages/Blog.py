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
button_text = "Home", "MyNotes", "Blogs", "Data"

for text, col in zip(button_text, st.columns(len(button_text))):
    if col.button(text):
        if text=="Home":
            switch_page("app")
        elif text == "Blogs":
            switch_page("Blog")
        elif text == "MyNotes":
            switch_page("Notes")
        elif text == "Data":
            switch_page("Data")  
st.write("""

    One of the most common applications of generative AI and large language models (LLMs) is answering questions based on a specific external knowledge corpus. Retrieval-Augmented Generation (RAG) is a popular technique for building question answering systems that use an external knowledge base. To learn more, refer to Build a powerful question answering bot with Amazon SageMaker, Amazon OpenSearch Service, Streamlit, and LangChain.

Traditional RAG systems often struggle to provide satisfactory answers when users ask vague or ambiguous questions without providing sufficient context. This leads to unhelpful responses like “I don’t know” or incorrect, made-up answers provided by an LLM. In this post, we demonstrate a solution to improve the quality of answers in such use cases over traditional RAG systems by introducing an interactive clarification component using LangChain.

The key idea is to enable the RAG system to engage in a conversational dialogue with the user when the initial question is unclear. By asking clarifying questions, prompting the user for more details, and incorporating the new contextual information, the RAG system can gather the necessary context to provide an accurate, helpful answer—even from an ambiguous initial user query.


""")