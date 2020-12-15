from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def log_in(request):
    error = None
    if request.method == "POST":
        
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user == None:
            error = "Username or password is incorrect"
        else:
            login(request, user)
            return redirect('users:dashboard')

    return render(request, 'users/login.html', {'error': error})



def signup(request):
    error = None
    if request.method == "POST":
        form = request.POST
        firstname = form['firstname']
        lastname = form['lastname']
        username = form['username']
        email = form['email']
        password = form['password']
        password2 = form['password2']

        if User.objects.filter(username=username).exists():
            error = "Username is taken!"
        elif User.objects.filter(email=email).exists():
            error = "That email is already in use!"
        elif password2 != password:
            error = "Passwords do not match!"
        else:
            user = User.objects.create_user(
                username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user.save()
            return redirect('users:login')

    return render(request, 'users/signup.html', {'error': error})


@login_required
def dashboard(request):

    return render(request, 'users/dashboard.html')


@login_required
def logoutUser(request):
    logout(request)
    return redirect('index')