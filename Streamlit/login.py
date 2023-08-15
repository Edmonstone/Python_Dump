import streamlit as st
def login():
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    login = st.button('Login')
    if login:
        if email == "test" and password == "test":
            st.success('You are verified')
            st.markdown('Click to get into our Metaverse')
            st.balloons()
            return 1
        else:
            st.error("Invalid credentials. Please try again.")

if __name__ == "__main__":
    login()