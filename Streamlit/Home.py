import streamlit as st
import login
import signup
import chatbot
from streamlit import session_state

def main():
    # Initialize session state
    if "page" not in session_state:
        session_state.page = "main"

    # Page redirection logic
    if session_state.page == "main":
        validation()
    elif session_state.page == "chatbot":
        chatbot.main()

def validation():
    # Streamlit UI
    st.title("Welcome Man!")

    # Auth
    choice = st.sidebar.selectbox('Get Validation', ['Signup', 'Login'])
    if choice == 'Signup':
        signup.signup()
    else:
        token = login.login()
        if token == 1:
            redirect_to_new_page()
            st.button("C H A T   B O T")

def redirect_to_new_page():
    session_state.page = "chatbot"

def redirect_to_main_page():
    session_state.page = "main"
        

if __name__ == "__main__":
    main()
