from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def RegisterView(request):
    
    #connecting the front-end to back-end
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        #Error Reg controll
        registeration_has_error = False
        
        #Check if user input email aready exists
        if User.objects.filter(email=email).exists():
            registeration_has_error = True
            messages.error(request, "Email already exists")
        
        #Check if user input Username aready exists   
        if User.objects.filter(username=username).exists():
            registeration_has_error = True
            messages.error(request, "Username already taken or exists!")
            
        #Check if user input Telephone aready exists
        if User.objects.filter(telephone=telephone).exists():
            registeration_has_error = True
            messages.error(request, "Phone number already exist or used!")
            
        #Checks if password and confirm password matchs
        if password != confirm_password:
            registeration_has_error = True
            messages.error(request, "Your Password do not match!, Try again")
            
        #Validates if password is !< 6
        if len(password) < 8:
            registeration_has_error = True
            messages.error(request, "Password must not be less than 8 Numbers or Charecter")
            
        #register redirect
        if registeration_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            # new_user.save()
            messages.success("Account has been created, Login now")
            return redirect('login')
            
    return render(request, 'accounts/register.html')

def LoginView(request):
    
    if request.method == "POST":
        # username = request.POST['username']
        username = request.POST.get('username')
        password = request.POST.get('password')
        # password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'accounts/login.html')
