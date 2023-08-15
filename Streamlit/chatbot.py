import streamlit as st
import requests
import plotly.figure_factory as ff
import numpy as np

def main():
    # Streamlit UI
    st.title("Edmonstone - AI Chatbot")
    
    # Set page layout
    st.sidebar.image("ck.jpg", use_column_width=True)

    st.sidebar.title(f"Happy Landing UserName")

    if st.button("Clear Conversation"):
        st.session_state.messages = []


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("You:"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Call OpenAI API to get response
        openai_api_key = "YOUR_OPENAI_API_KEY"
        api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }
        
        data = {
            "prompt": prompt,
            "max_tokens": 50
        }
        
        response = requests.post(api_url, json=data, headers=headers)
        response_text = response.json()["choices"][0]["text"]
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown("Third Eye: " + response_text)
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
        # Show toast and success messages
        st.info("Third Eye is typing...")
        st.success("Third Eye: " + response_text)

        # Clear user input
        st.text_input("You:", value="", key="user_input")


if __name__ == "__main__":
    main()