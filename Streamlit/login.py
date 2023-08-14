import streamlit as st
import pages.chatbot as chatbot

def login():
    st.title('Login Page')
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    login = st.button('Login')

    if login:
        if email == "test" and password == "test":
            chatbot.main()
        else:
            st.error("Invalid credentials. Please try again.")

if __name__ == "__main__":
    login()