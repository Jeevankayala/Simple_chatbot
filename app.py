import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API key from environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model with desired configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Initialize chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

def get_response(prompt):
  """Fetches response from Gemini model and updates history"""
  chat_session = model.start_chat(history=st.session_state["history"])
  response = chat_session.send_message(prompt)
  st.session_state["history"].append({"role": "model", "parts": [response.text]})
  return response.text


st.title("ChatGPT-like clone with Gemini")

# Display chat messages from history
for message in st.session_state["history"]:
  with st.chat_message(message["role"]):
    st.markdown(message["parts"][0])

# Accept user input
if prompt := st.chat_input("What is up?"):
  st.session_state["history"].append({"role": "user", "parts": [prompt]})
  with st.chat_message("user"):
        st.markdown(prompt)
  # Get response from Gemini and display it
  response = get_response(prompt)
  with st.chat_message("assistant"):
    st.markdown(response)
    # print(st.session_state["history"])

if st.button("Clear History"):
    if st.session_state["history"]:
      st.session_state["history"] = []  # Clear the history
      st.success("History cleared successfully")
      st.rerun()
    else:
       st.error("No History Found")