from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
import re
from django.contrib.auth.hashers import make_password
def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one letter and one digit
    if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
        return False

    # Check for similarity to personal information
    if re.search(r'(?i)password|123456|qwerty', password):
        return False

    # Check if password is entirely numeric
    if password.isdigit():
        return False

    return True

def singUp(request):
    msg=None
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pswd']
        confirmPass = request.POST['cpswd']
        if password == confirmPass:
            if is_valid_password(password):
                password = make_password(password)
                saveData = User(username = name, email = email, password = password)
                saveData.save()
            else :
                 msg = 'Password must contain at least 8 characters, including one letter and one digit, and cannot be too similar to personal information.'    
        else:
            return HttpResponse("password and conf password are differnt")  
    if msg != None:
        alert_message = msg
        js_script = f"<script>alert('{alert_message}');</script>"
        response = HttpResponse(render(request, 'singUpLogin.html'))
        response.content += js_script.encode('utf-8')
        return response
    else:
        return render(request,'singUpLogin.html')    
def logIn(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['pswd']
        user = authenticate(username = username ,password = password)
        auth_login(request,user)
        return redirect('/')
    else:
        return redirect('/')   

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/account/singUp/')