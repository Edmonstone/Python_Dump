import streamlit as st

def signup():
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    username = st.text_input('Enter your username')

    if st.button("Create my account"):
        st.success('Account created Successfully!')
        st.markdown('Please Login using your email and password')
        st.balloons()


if __name__ == "__main__":
    signup()