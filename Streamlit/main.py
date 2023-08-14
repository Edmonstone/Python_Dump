import streamlit as st
import subprocess
import chatbot
from streamlit_extras.switch_page_button import switch_page 


second_page = "chatbot.py"

def main():
    # Streamlit UI
    st.title("Welcome Man!")

    # Auth
    choice = st.sidebar.selectbox('Get Validation', ['Signup', 'Login'])
    if choice == 'Signup':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your username')

        if st.button("Create my account"):
            st.success('Account created Successfully!')
            st.markdown('Please Login using your email and password')
            st.balloons()

    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        login = st.button('Login')

        if login:
            if email == "test" and password == "test":
                placeholder = st.empty()
                
                # if st.success:
                    # st.markdown('<style>#MainMenu {visibility: hidden;}</style>', unsafe_allow_html=True)
                    # st.empty() 
                 # Clear the main content
                    # st.stop
                # switch_page(second_page)
                chatbot.main()

               
                # chatbot.main()  # Show the chatbot interface 
            else:
                st.error("Invalid credentials. Please try again.")


if __name__ == "__main__":
    main()
