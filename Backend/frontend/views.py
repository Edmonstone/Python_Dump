from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def landingpage(request):
    print("Hey")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'streamlit.html') 
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'home.html', {'error_message': error_message})
    
    return render(request, 'home.html')  


