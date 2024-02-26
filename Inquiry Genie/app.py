import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()  # loading all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get responses.
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize streamlit app


st.set_page_config(
    page_title="Q&A Demo",
    layout="wide",
)

with st.sidebar:
    st.title("Gemini LLM Application")
    st.markdown(
        """
🌟 Explore the power of AI-driven question answering with Gemini, a cutting-edge Large Language Model developed by Google GenerativeAI.

🔮 Ask anything you're curious about, and let Gemini dazzle you with its insightful responses.

🚀 Dive into a world of endless knowledge and engage in fascinating conversations with this state-of-the-art language model.

🔍 Type your questions in the input field and watch as Gemini works its magic to provide you with accurate and informative answers.

🌌 Embark on a journey of discovery and discovery with Gemini LLM Application. Start asking now!
        """
    )
    

with open('wave.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.header("InquiryGenie: Unleashing Gemini's Answering Powers")
IInput = st.text_input("Input: ", key="IInput")
submit = st.button("Ask the question")

# When submit is clicked

if submit:
    answer = get_gemini_response(IInput)
    st.subheader("The Response is")
    st.write(answer)