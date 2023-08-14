import streamlit as st
import login
import signup

second_page = "chatbot.py"

def main():
    # Streamlit UI
    st.title("Welcome Man!")

    # Auth
    choice = st.sidebar.selectbox('Get Validation', ['Signup', 'Login'])
    if choice == 'Signup':
        signup.signup()
    else:
        login.login()

if __name__ == "__main__":
    main()
