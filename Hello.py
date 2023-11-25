from pathlib import Path
import streamlit as st
from PIL import Image
import numpy as np
import time
import random

#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

curr_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile=curr_dir / "data" / "PROF.png"
cssfile=curr_dir /"styles" / "main.css"
resume_f=curr_dir / "data" / "Resume.pdf"

TITLE= "Tushar Singh"
Page_IC= ":technologist:"
NAME= "Tushar Singh"
DESC="""
Software Developer with bachelors in Electronics Engineering experience in AI/ML have a certain interest in NLP,RL,AGI,CV and an Avid Reader
"""
st.set_page_config(page_title=TITLE, page_icon=Page_IC)

#from streamlit_extras.switch_page_button import switch_page
button_text = "Home", "MyNotes", "Blogs","Data"

for text, col in zip(button_text, st.columns(len(button_text))):
    if col.button(text):
        st.write(text)
EMAIL="📬tsingh1897@gmail.com"
MEDIA_SOC={
    "🤖 GitHub":"",
    "🏢 LinkedIn":"https://www.linkedin.com/in/tushar-singh-4326b7188/",
    "Others":""
    
}

PROJECTS={
    "📦MITHYA":["- Working on a Multi lingual voice based LLM solution for the Government schemes recommendation for the needful in POC and initial stage",""],
    "📦DCGenerator":["- Converts Snippets or Images of hand drawn poc of a app to ready to deploy website using Yolov7 for detectiona and KNN for the prediction and code generation",""],
    "📦CALVISION":["- Was a novel approach on using TinyML for Onboard Detection of Top 25 Indian Cuisines Foods with Calories prediction on the portion size using skeleteon of YOLOv3 at the times later upgraded to yolov4 deployed it on Android device using SDK and Tflite","https://www.linkedin.com/feed/update/urn:li:activity:6731645057734082560/"],
    "📦Pratbhimbh":["- A website with a Bot trained on the RNNs using RASA framework and the NeuralsMF implementation for the collaborative recommendations of the Mentors for Mentee to get the Policies and different pathway for the Startup world","https://github.com/tusu18/startup_bot"],
    "📦BLURR IMAGE DETECTION APP":["- This project is made on Blur dataset by CERT and it is deployed on heroku using streamlitI have extracted several features from the images using HPF such as Sobel,Laplace,Scharr better known to detect high deviation or corner since the blur images are too smooth.. Using these features and stratifying the data as the data set was quite imbalance i have fitted the model using various model such as XgbClassifier,TReeClassifier,KNN,SVC","https://blurredapp.herokuapp.com/"]
    
}

#Loading css pdf prof

with open(cssfile) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_f,"rb") as pdf:
    pdfby=pdf.read()
profile_pic=Image.open(profile)

#---Main

col1,col2 = st.columns(2,gap="small") 
with col1:
    st.image(profile_pic,width=220) 
with col2:
    st.title(NAME)
    st.write(DESC)
    st.download_button(
        label="Download Resume",
        data=pdfby,
        file_name=resume_f.name,
        mime="application/octet-stream",
    )
    st.write(EMAIL)

#--links and everything
st.write("#")
cols=st.columns(len(MEDIA_SOC))
for index,(plt,link) in enumerate(MEDIA_SOC.items()):
    cols[index].write(f"[{plt}]({link})")
    
# Experience

st.write("#")
st.subheader("Experience💼")
st.write("""
         
         🔵 Tata Consultancy Services Ltd(2021-): SDE
         - 🔸 2.5 years of Experience as a Software Developer and ML Engineer.
         - 🔸 Development of Payment Solution for different clients Using AI.
         - 🔸 Worked for Rapid Labs collaberated with others to form chapter TECH FM that specialises in latest tech developmet and train other associates on them.
         
         🔵 Tata Proengage(2023-): AI Developer
         - 🔸 Working for non profit organisation and collaborating within TATA group for the development of an LLM based
           multi lingual chatbot recommender of Government Schemes.
           
         🔵 MedToureasy(2020-2020)-Data Analyst Intern
         
         🔵 The Spark Foundation(2020-2020)- Data Science & Analytics Intern
         
         """
    
) 
# Skills
st.write("#")
st.subheader("Skills 🏅")
on1 = st.toggle('Expand')
if on1:
    st.write("""
        🔵 Python,ML,DL,GenAI,Java,OpenCv,Azure,Jenkins,Scala,RestApi,AWS,Flask,SQL,Data
        Science,GAN,Yolo,Scrapy,SpringBoot,Statistics,Apache Spark,DSA,Heroku,Streamlit,Tableau
        """
    
) 
else:
    st.write("""
        🔵 Python-Machine Learning-Deep Learning-GenAI-Java-Computer Vision-Jenkins-Scala-RestApi-AWS-Flask-SQL
    
""") 
# Certifications
st.write("#")
st.subheader("Certifications 🏆")
on2 = st.toggle('Expand.')
if not on2:
    st.write(f"""
             - 🔸[{"Machine Learning (Stanford University|Online)"}]({"https://www.coursera.org/account/accomplishments/verify/YCSQYMRYGTV8"})
             - 🔸[{"Neural Network and Deep Learning"}]({"https://www.coursera.org/account/accomplishments/verify/FWN7VRC78LBM"})
             - 🔸[{"Algorithmic Tool Box(UC SanDiego)"}]({"https://www.coursera.org/account/accomplishments/certificate/RJ74Y3JXLZKC"})
             - 🔸[{"The Complete Prompt Engineering for AI Bootcamp (2023) (Udemy)"}]({"https://www.udemy.com/certificate/UC-0102be5f-7435-43a8-8133-7d72988d68f5/"})
             - 🔸[{"IBM Data Science Specialization (Coursera)"}]({"https://www.coursera.org/account/accomplishments/professional-cert/7WE5MLFKUPLC"})
             - 🔸[{"Azure AI-900"}]({"https://www.credly.com/badges/0ecc59d1-22a4-4b0c-a5fd-43aa835dc732?source=linked_in_profile"})
             
        """
    
) 
else:
    st.write(f"""
             - 🔸[{"Machine Learning (Stanford University|Online)"}]({"https://www.coursera.org/account/accomplishments/verify/YCSQYMRYGTV8"})
             - 🔸[{"Neural Network and Deep Learning"}]({"https://www.coursera.org/account/accomplishments/verify/FWN7VRC78LBM"})
             - 🔸[{"Algorithmic Tool Box(UC SanDiego)"}]({"https://www.coursera.org/account/accomplishments/certificate/RJ74Y3JXLZKC"})
             - 🔸[{"The Complete Prompt Engineering for AI Bootcamp (2023) (Udemy)"}]({"https://www.udemy.com/certificate/UC-0102be5f-7435-43a8-8133-7d72988d68f5/"})
             - 🔸[{"IBM Data Science Specialization (Coursera)"}]({"https://www.coursera.org/account/accomplishments/professional-cert/7WE5MLFKUPLC"})
             - 🔸[{"Azure AI-900"}]({"https://www.credly.com/badges/0ecc59d1-22a4-4b0c-a5fd-43aa835dc732?source=linked_in_profile"})
             - 🔸[{"R Programming (Udemy)"}]({"https://www.udemy.com/certificate/UC-JPMETCNY/"})
             - 🔸[{"Taming Big Data with Apache Spark and Python - Hands On!(Udemy)"}]({"https://www.udemy.com/certificate/UC-05a2922d-e17f-497e-9fb9-43521936a679/"})
             - 🔸[{" Statistics for Data Science and Business Analysis  (Udemy)"}]({"https://www.udemy.com/certificate/UC-f3a18a96-df82-4530-93fd-0d8cef949057/"})
             - 🔸[{"Natural Language Processing in TensorFlow(Coursera)"}]({"https://www.coursera.org/account/accomplishments/certificate/R8S4VJ6WW9KX"})
           
        """)     
    

# Projects
st.write("#")
st.subheader("Projects 📁")
on = st.toggle('Short Description')
for p,l in PROJECTS.items():
    st.write(f"[{p}]({l[1]})")
    if on:
        st.write(l[0])

#st.write("#")
#st.subheader("Books Recommendations 📖")
#on3 = st.toggle('More')
#if on3:
#   st.write(f"""
#         - 🔸[{"Dark Matter"}]({"https://www.goodreads.com/book/show/27833670-dark-matter?ref=nav_sb_ss_4_5"})
 #        - 🔸[{"The Guest List"}]({"https://www.goodreads.com/book/show/52656911-the-guest-list?ref=nav_sb_ss_1_9"})
  #       - 🔸[{"Chip War"}]({"https://www.goodreads.com/book/show/2612.The_Tipping_Point"})
   #      - 🔸[{"The Outliers"}]({"https://www.goodreads.com/book/show/2612.The_Tipping_Point"})
    #     - 🔸[{"Deception Point"}]({"https://www.goodreads.com/book/show/2612.The_Tipping_Point"})
    #    """
  #  
#) 
#else:
 #   st.write(f"""
  #      
  #      - 🔸[{"The Tipping Point"}]({"https://www.goodreads.com/book/show/2612.The_Tipping_Point"})
  #      - 🔸[{"Dark Matter"}]({"https://www.goodreads.com/book/show/27833670-dark-matter?ref=nav_sb_ss_4_5"})
  #      - 🔸[{"The Guest List"}]({"https://www.goodreads.com/book/show/52656911-the-guest-list?ref=nav_sb_ss_1_9"})
  #      - 🔸[{"Chip War"}]({"https://www.goodreads.com/book/show/2612.The_Tipping_Point"})
  #     
#""") 
    

#CHat code from streamlit api


st.subheader("Book Suggestion 📖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Just Type Hi will suggest book I have read!"):
    # Add user message to chat history
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        assistant_response = random.choice(
            [
                "The Tipping Point",
                "Dark Matter",
                "The Guest List",
                "Chip War",
                "The Outliers",
                "Deception Point",
                "Sapiens",
                "Strt With Why",
                "Chanakya Chants",
                "And Then There where none",
                "Freakonomics",
                "Think Fast and Slow",
                "Recursion",
                "Project Hail Mary",
                "One of Us is Lying",
                "Sharp Objects"
                
                
            ]
        )
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    





        
          
    
                

