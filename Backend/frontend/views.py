import streamlit as st
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def landingpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('streamlit_app')  # Redirect to the embedded Streamlit app
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'home.html', {'error_message': error_message})

    return render(request, 'home.html')

@login_required
def streamlit_view(request):
    # Use the streamlit.embed module to render the Streamlit app
    streamlit_iframe = st.write("<iframe sandbox='allow-same-origin allow-scripts' src='http://localhost:8502/' frameborder='0' width='100%' height='750'></iframe>", unsafe_allow_html=True)
    return render(request, 'streamlit_template.html', {'streamlit_iframe': streamlit_iframe})
