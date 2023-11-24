from pathlib import Path
import streamlit as st
from PIL import Image


curr_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile=curr_dir / "data" / "PROF.jpg"
cssfile=curr_dir /"styles" / "main.css"
resume_f=curr_dir / "data" / "Resume.pdf"

TITLE= "Tushar Singh Resume"
Page_IC= ":wave:"
NAME= "Tushar Singh"
DESC="""
Software Developer experience in ML algorithms and an Avid Researcher
"""
EMAIL="tsingh1897@gmail.com"
MEDIA_SOC={
    "GitHub":"",
    "LinkedIn":"https://www.linkedin.com/in/tushar-singh-4326b7188/",
    "Others":""
    
}

PROJECTS={
    "MITHYA":["- Working on a Multi lingual voice based LLM solution for the Government schemes recommendation for the needful in POC and initial stage",""],
    "DCGenerator":["- Converts Snippets or Images of hand drawn poc of a app to ready to deploy website using Yolov7 for detectiona and KNN for the prediction and code generation",""],
    "CALVISION":["- Was a novel approach on using TinyML for Onboard Detection of Top 25 Indian Cuisines Foods with Calories prediction on the portion size using skeleteon of YOLOv3 at the times later upgraded to yolov4 deployed it on Android device using SDK and Tflite","https://www.linkedin.com/feed/update/urn:li:activity:6731645057734082560/"],
    "Pratbhimbh":["- A website with a Bot trained on the RNNs using RASA framework and the NeuralsMF implementation for the collaborative recommendations of the Mentors for Mentee to get the Policies and different pathway for the Startup world","https://github.com/tusu18/startup_bot"],
    "BLURR IMAGE DETECTION APP":["- This project is made on Blur dataset by CERT and it is deployed on heroku using streamlitI have extracted several features from the images using HPF such as Sobel,Laplace,Scharr better known to detect high deviation or corner since the blur images are too smooth.. Using these features and stratifying the data as the data set was quite imbalance i have fitted the model using various model such as XgbClassifier,TReeClassifier,KNN,SVC","https://blurredapp.herokuapp.com/"]
    
}
st.set_page_config(page_title=TITLE, page_icon=Page_IC)
#Loading csspdf prof

with open(cssfile) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_f,"rb") as pdf:
    pdfby=pdf.read()
profile_pic=Image.open(profile)

#---MAin

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
    
# _    Experience

st.write("#")
st.subheader("Experience")
st.write("""
         
         TCS(2021-)-SDE
         - 2.5 years of Experience as a Software Developer and ML Engineer.
         - Development of Payment Solution for different clients Using AI.
         - Worked for Rapid Labs collaberated with others to form chapter that specialises in latest tech developmet.
         
         Tata Proengage(2023-)-AI Developer
         - Working for non profit organisation within TATA for the development of an LLM based
           multi lingual chatbot recommender of Government Schemes.
           
         MedToureasy-Data Analyst Intern
         
         The Spark Foundation- Data Science & Analytics Intern
         
         """
    
) 
st.write("#")
st.subheader("Projects")
for p,l in PROJECTS.items():
    st.write(f"[{p}]({l[1]})")
    st.write(l[0])





        
          
    
                

