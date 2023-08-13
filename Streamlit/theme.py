import streamlit as st

def apply_theme(primary_color, background_color, text_color):
    st.markdown(
        f"""
        <style>
            body {{
                color: {text_color};
                background-color: {background_color};
            }}
            .stButton > button {{
                background-color: {primary_color};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.title("Theme Test")

    selected_theme = st.sidebar.selectbox("Select Theme", ["Light", "Dark", "Green", "Blue"])

    if selected_theme == "Dark":
        apply_theme(primary_color="#333", background_color="#121212", text_color="#FFFFFF")
    elif selected_theme == "Green":
        apply_theme(primary_color="#00FF00", background_color="#FFFFFF", text_color="#000000")
    elif selected_theme == "Blue":
        apply_theme(primary_color="#0000FF", background_color="#FFFFFF", text_color="#000000")
    else:
        apply_theme(primary_color="#FFFFFF", background_color="#FFFFFF", text_color="#000000")

if __name__ == "__main__":
    main()
