from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_login(request):

    if request.method == "POST":
        
        if "register-submit" in request.POST:
            full_name = request.POST.get('fullname', None)
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)

            stored_email = CustomUser.objects.filter(email=email).exists()

            if stored_email:
                return render(request, "user/register-error.html", {'message':'email already exists'})


            else:
                user = CustomUser.objects.create(full_name=full_name, username= username, email=email)

                user.set_password(password)
                user.save()
            


        if "login-submit" in request.POST:
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            

            else:
                return render(request, "user/login-error.html", {'message':'incorrect email or password'})




    return render(request, "user/register-login.html")


def logout_user(request):
    logout(request)


