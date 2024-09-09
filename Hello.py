from pathlib import Path
import streamlit as st
from PIL import Image
import numpy as np
import time
import random

#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

curr_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile=curr_dir / "data" / "PROF.png"
startuppic= curr_dir / "data" / "startupbotrec.png"
htmldynamic= curr_dir / "data" / "htmldynamicpic.jpg"
calvpic = curr_dir / "data" / "calvisbhendi.png"
cssfile=curr_dir /"styles" / "main.css"
resume_f=curr_dir / "data" / "Resume.pdf"
cal_pic=Image.open(calvpic)
startup_pic=Image.open(startuppic)
htmldyn_pic=Image.open(htmldynamic)
def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

#Sample Example
#text = "This is an example of streamlit text with typewriter effect :)"
#speed = 10
#typewriter(text=text, speed=speed)

TITLE= "Tushar Singh"
Page_IC= ":technologist:"
NAME= "Tushar Singh"
DESC="""
I am a Software Developer with 3 years of experience as an ML Engineer and Researcher, grounded in Electronics Engineering and driven by a passion for AI. Specializing in NLP, Reinforcement Learning, AGI, and Computer Vision, I love solving complex challenges and creating innovative solutions. As an avid reader, I continuously explore new ideas and emerging trends, blending curiosity with technical expertise to push the boundaries of AI technology."""

st.set_page_config(page_title=TITLE, page_icon=Page_IC)

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
EMAIL="📬tsingh1897@gmail.com"
MEDIA_SOC={
    "🤖 GitHub":"https://github.com/tusu18",
    "🏢 LinkedIn":"https://www.linkedin.com/in/tushar-singh-4326b7188/",
    "Others":""
    
}

PROJECTS={
    "📦Alambana":[""" - 🔸 Developing a multilingual voice-enabled solution powered by Large Language Models (LLMs), incorporating Whisper ,Wav2Vec modified for accurate Automatic Speech Recognition (ASR) across multiple languages.
- 🔸 Focused on government schemes recommendation, utilizing mBERT, XLM-RoBERTa for Natural Language Understanding (NLU to interpret user queries and context accurately.
- 🔸 Leveraging GPT-4 Multilingual , mT5 for Natural Language Generation (NLG), ensuring personalized and context-aware recommendations for users in their native language.
- 🔸 Implementing an efficient Text-to-Speech (TTS) system using models like Tacotron 2, FastSpeech 2 to deliver clear, natural-sounding voice outputs in multiple languages.
- 🔸 Currently in the Proof of Concept (POC) and initial development stages, focusing on optimizing Wav2Vec 2.0and XLM-RoBERTa for multilingual performance and improving speech recognition accuracy across diverse languages.
- 🔸 Exploring Deep Q-Networks (DQN), Policy Gradient Methods to build a dynamic recommendation engine that continuously learns from user feedback and interactions to suggest relevant government schemes.
- 🔸 Enhancing the solution with multimodal input capabilities (text and voice), utilizing models like SpeechT5 to handle both spoken and written inputs seamlessly, while personalizing responses based on the user's needs.""","",""],
    "📦DCGenerator":["""
- 🔸 Developing a framework to convert hand-drawn POC (Proof of Concept) sketches or images of app designs into deployable websites** by integrating state-of-the-art AI models and techniques.
- 🔸 Utilizing YOLOv7 for object detection** and image segmentation**, ensuring precise identification and extraction of design elements from scanned or photographed hand-drawn sketches.
- 🔸 Applying K-Nearest Neighbors (KNN) for feature classification and predictive modeling, enabling the alignment of detected design elements with a predefined set of templates or UI components.
- 🔸 Implementing an automated code generation pipeline that translates detected design elements into clean, standards-compliant HTML/CSS/JavaScript, facilitating rapid prototyping and design iteration.
- 🔸 Incorporating advanced image processing techniques like Pix2Pix for image-to-image translation and **Semantic Segmentation to enhance design alignment and visual fidelity.
- 🔸 Integrating motion capture and procedural animation to transform static designs into dynamic, interactive web elements, enhancing user engagement with responsive animations.
- 🔸 Utilizing Reinforcement Learning (RL) to optimize web layouts and Neural Style Transfer** to merge hand-drawn styles with modern web aesthetics, ensuring a polished and professional appearance.
- 🔸 Generating modular Web Components for easy integration and reusability, along with incorporating SS Animations and Transitions to enrich the visual appeal and responsiveness of the interface.
- 🔸 Suggesting different animations and styles through an AI-driven recommendation engine, enabling rapid deployment and showcasing of diverse design options to clients in real-time.
- 🔸 Enabling interactive prototyping with Generative Adversarial Networks (GANs) to create and demonstrate interactive prototypes based on client feedback, allowing for quick adjustments and refinements.
- 🔸 Incorporating user testing analytics and A/B Testing** to continually validate and refine design conversions and animations, ensuring optimal user experience and performance.""","",htmldyn_pic],
    "📦CALVISION":["""
    - 🔸 The system eliminates the need for manual data entry, a common feature of traditional calorie calculator apps where accuracy often falls short. Instead, users can simply capture an image or video of their meal, and the system provides instant calorie predictions based on portion size, currently focused on a limited selection of foods.
    - 🔸 Volume Estimation with DepthNet & YOLOv4: Utilized DepthNet in conjunction with YOLOv4 to estimate the volume of food items by generating depth maps from single images. The bounding box information from YOLOv4 is fused with the depth map for precise volume estimation.
	- 🔸 Single-Image Depth Estimation: Applied MonoDepth2 for accurate depth estimation from a single image, ensuring reliable weight predictions even when the camera captures from different angles.
    - 🔸 3D Reconstruction with NeRF & DPT: Implemented NeRF (Neural Radiance Fields) and DPT (Dense Prediction Transformer) to reconstruct 3D food models from short video sequences, enhancing the precision of volume estimation by analyzing multiple viewpoints.
	- 🔸 Weight Prediction Models: Developed a Support Vector Regression (SVR) model and experimented with Neural Networks for weight prediction. These models extract visual features such as area and depth from the images and depth maps to accurately estimate the weight of food items.
	- 🔸 Advanced Food Segmentation: Integrated DeepLabV3+ and Mask R-CNN for high-precision segmentation of individual food items, even when overlapping or mixed with other elements, improving the accuracy of detection and volume estimation.
	- 🔸 Optimized for Mobile Devices: Leveraged TinyML and TensorFlow Lite with techniques such as quantization and pruning to reduce model size, enhance inference speed, and enable real-time performance on mobile devices.
	- 🔸 Hardware Acceleration: Implemented Edge TPU and NPU acceleration, utilizing the advanced processing capabilities of modern mobile devices to achieve faster and more efficient real-time inference.
	- 🔸 Mobile-First Real-Time Solution: Developed an entirely mobile-based system that performs on-device inference without cloud dependency, allowing users to capture images or short videos and receive instant, accurate calorie predictions directly on their devices.
.""","https://www.linkedin.com/feed/update/urn:li:activity:6731645057734082560/",cal_pic],
    "📦Pratbhimbh":["""
    - 🔸 Website Development with Intelligent Bot**:
    - 🔸 Implemented a **T5 model** (Text-To-Text Transfer Transformer) using the **RASA framework** to create an advanced bot.
    - 🔸 Designed the bot to function as an initial mentor and provide Q&A support on government policies and procedures.
    - 🔸 Leveraged the T5 model’s capabilities for text generation to deliver accurate and contextually relevant responses to user inquiries.
    - 🔸 **Hybrid Recommendation System**:
    - 🔸 Adapted the Neural Matrix Factorization (NeuralsMF) model to enhance mentor recommendations.
    - 🔸 Made adjustments to the matrix factorization algorithm to better capture user preferences and interaction patterns.
    - 🔸 Achieved a **44% improvement** in top-k prediction accuracy compared to traditional collaborative filtering methods.
    - 🔸 Incorporated DropoutNet to address overfitting and improve the diversity and relevance of mentor recommendations.
    - 🔸 Utilized dropout regularization techniques to enhance the robustness and generalization of the recommendation system.
    - 🔸 Created a hybrid recommendation engine combining NeuralsMF and DropoutNet.
    - 🔸 Processed user profiles and preferences to deliver personalized mentor recommendations, enhancing the effectiveness of the mentoring process.
    - 🔸**Functional Components**:
    - 🔸 Developed the bot to serve as the first interaction point for users, offering initial guidance and assistance with government policy-related queries.
    - 🔸 Enabled the bot to handle a broad range of topics with contextually appropriate responses.
    - 🔸 Designed the bot to answer specific questions regarding government actions.
    - 🔸 Utilized the T5 model’s advanced natural language understanding and generation capabilities to ensure accurate responses.""","https://github.com/tusu18/startup_bot",startup_pic],
    "📦BLURR IMAGE DETECTION APP":["- 🔸 This project is made on Blur dataset by CERT and it is deployed on heroku using streamlitI have extracted several features from the images using HPF such as Sobel,Laplace,Scharr better known to detect high deviation or corner since the blur images are too smooth.Using these features and stratifying the data as the data set was quite imbalance i have fitted the model using various model such as XgbClassifier,TReeClassifier,KNN,SVC","https://blurredapp.herokuapp.com/",""]
    
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
    st.write(typewriter(text=DESC, speed=10))
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
         
    🔵 Tata Consultancy Services Ltd(2021-2024): SDE/Researcher
       **Automated Cheque Signature Verification**:
     - 🔸 Designed and implemented a robust cheque signature verification system.
     - 🔸 Achieved an **Equal Error Rate (EER)** reduction to **2.4%**.
     - 🔸 Decreased manual intervention by **40%** using **Convolutional Neural Networks (CNNs)** and **image enhancement algorithms**.
  
       **TableNet 2.0**:
     - 🔸 Contributed to **TableNet 2.0**, achieving precision scores of **0.97** for table detection and **0.94** for table extraction and structure detection.
     - 🔸 Addressed challenges with both bordered and borderless tables using advanced deep learning models.
     - 🔸 Documented findings in a white paper and deployed the solution as part of the TCS AI module for clients including **Assa Abloy** and **Bosch**.

       **Floor Plan Analysis and 3D Reconstruction**:
     - 🔸 Utilized **Masked Fast R-CNN** for precise instance segmentation and object detection, enabling accurate identification of architectural elements.
     - 🔸 Integrated **Transformers** to enhance model understanding of complex architectural layouts and relationships between elements.
     - 🔸 Focused on detecting features such as **windows**, **doors**, and **room layouts** using advanced **semantic segmentation** techniques.
     - 🔸 Developed a model to convert **2D floor plans** into **3D visualizations** with **photogrammetry** and **neural rendering** techniques, facilitating rapid and interactive design review.

       **Leadership and Mentorship**:
     - 🔸 Founded and led the **Tech FM** chapter, providing **AI/ML** mentorship and training to interns and executives, promoting knowledge transfer and skill development.

       **CI/CD Pipeline Management**:
     - 🔸 Created and maintained **CI/CD pipelines** using Jenkins, automating build, test, and deployment processes for reliable software releases.

       **Technical Troubleshooting**:
     - 🔸 Led technical troubleshooting and performance tuning, enhancing system scalability and performance to manage increasing transaction volumes efficiently.
    
    🔵 Tata Proengage(2023-): AI Developer
     - 🔸 Working with non profit organisation and collaborating within TATA group for the development of an LLM based
           multi lingual chatbot recommender of Government Schemes.
     - 🔸 Upskilling NGO workers in using of AI tools logistic as well as in engagement.
           
    🔵 MedToureasy(2020-2020)-Data Analyst Intern
     - 🔸 Deployed a ML model for the prediction of Donor Outcome which resulted into succesful campaign
     - 🔸 Made and integrated Analytic Dashboard using Tableau and MongoDb on Medical Facilities in several region.

    🔵 The Spark Foundation(2020-2020)- Data Science & Analytics Intern
     - 🔸 I taught Data Science and coding to aspirants from diverse 
            backgrounds
        
         """
    
) 
# Skills
st.write("#")
st.subheader("Skills 🏅")
on1 = st.toggle('Expand')
if on1:
    st.write("""
        🔵 Python,ML,DL,GenAI,Java,OpenCv,Azure,Jenkins,Scala,RestApi,AWS,,C++,Flask,SQL,Data
        Science,GAN,Yolo,Scrapy,SpringBoot,Statistics,Theano,Apache Spark,DSA,Heroku,Streamlit,Tableau
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
st.markdown(
    """
    <style>
    .css-1d391kg { /* Adjust the column class name as needed */
        margin-right: 20px; /* Adjust the value for spacing */
    }
    </style>
    """,
    unsafe_allow_html=True
)
for p,l in PROJECTS.items():
    if not on:
        st.write(f"[{p}]({l[1]})")
        col1,col2 = st.columns([10,2]) 
        with col2:
            if l[2]!="":  
                st.image(l[2],width=200) 
        with col1:
            st.write(l[0])

    else:
        st.write(f"[{p}]({l[1]})")

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
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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
                "Sharp Objects",
                "Freakonomics",
                "Shoe Dog",
                "Thinking Fast and Slow",
                "Drive",
                "Hooked",
                "Influence",
                "SuperIntelligence",
                "Founders at Work"
                
                
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
    





        
          
    
                

