import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load API keys
load_dotenv()
os.environ["OPENAI_API_KEY"] = st.secrets["OPENROUTER_API_KEY"]
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini", openai_api_base="https://openrouter.ai/api/v1")

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("💬 AI Chatbot with GPT-4o Mini")

# Initialize chat history
if "messages" not in st.session_state:
    system = SystemMessage(content="You are a smart person")
    st.session_state.messages = [system]

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Invoke model
    result = model.invoke(st.session_state.messages)

    # Display AI response
    ai_response = result.content
    st.session_state.messages.append(AIMessage(content=ai_response))
    with st.chat_message("assistant"):
        st.markdown(ai_response)
