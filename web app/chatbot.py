import streamlit as st
import requests
from datetime import datetime

# Groq API details
API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = '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'  # Example for Streamlit secrets

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def call_chatbot_api(prompt):
    """Improved API call function with better error handling"""
    try:
        payload = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [{
                "role": "user",
                "content": prompt
            }]
        }

        # Add timeout and retry logic
        max_retries = 2
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    API_URL,
                    headers=HEADERS,
                    json=payload,
                    timeout=10  # 10 second timeout
                )

                if response.status_code == 200:
                    data = response.json()
                    if "choices" in data and len(data["choices"]) > 0:
                        return data["choices"][0]["message"]["content"].strip()
                    return "🤖 I'm not sure how to respond to that."

                elif response.status_code == 503:
                    if attempt < max_retries - 1:
                        st.warning("Model loading, retrying...")
                        continue
                    return "🛠️ Model is still loading. Please try again in a moment."

                else:
                    return f"⚠️ API Error ({response.status_code}): {response.text[:200]}"

            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    st.warning("Request timed out, retrying...")
                    continue
                return "⏰ Request timed out. Please try again."

            except requests.exceptions.RequestException as e:
                return f"🔌 Connection Error: {str(e)}"

    except Exception as e:
        return f"❌ Unexpected Error: {str(e)}"


def app():
    # Apply consistent dark theme
    st.markdown("""
        <style>
        .stApp {
            background-color: #0D1117;
            color: #C9D1D9;
        }
        .stTextInput>div>div>input {
            background-color: #161B22;
            color: #C9D1D9;
            border: 1px solid #30363D;
        }
        .stChatMessage {
            border-radius: 8px;
            margin: 8px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🤖 Pathcoder Chatbot")
    st.caption("Ask me anything about tech careers, programming, or software development")

    # Initialize chat history with system message if empty
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [{
            "role": "assistant",
            "text": "Hello! I'm your tech career assistant. How can I help you today?",
            "time": datetime.now().strftime("%H:%M")
        }]

    # Display chat messages
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["text"])
            if "time" in message:
                st.caption(message["time"])

    # Chat input
    if prompt := st.chat_input("Type your question here..."):
        # Add user message to chat history
        user_message = {
            "role": "user",
            "text": prompt,
            "time": datetime.now().strftime("%H:%M")
        }
        st.session_state.chat_history.append(user_message)

        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(prompt)
            st.caption(user_message["time"])

        # Get and display assistant response
        with st.spinner("Thinking..."):
            response = call_chatbot_api(prompt)

            assistant_message = {
                "role": "assistant",
                "text": response,
                "time": datetime.now().strftime("%H:%M")
            }
            st.session_state.chat_history.append(assistant_message)

            with st.chat_message("assistant"):
                st.markdown(response)
                st.caption(assistant_message["time"])

        # Optional: Limit chat history size
        if len(st.session_state.chat_history) > 20:
            st.session_state.chat_history = st.session_state.chat_history[-20:]

