from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

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

    return redirect("home")



def password_reset_request(request):

    form = CustomPasswordResetForm()

    if request.method == "POST":

        form = CustomPasswordResetForm(request.POST)
        
        if form.is_valid():

            email = form.cleaned_data['email']

            user = CustomUser.objects.filter(email=email).first()
            # print(user)

            if user:
                
                subject = "Password Reset Request"

                message = render_to_string('user/passwordrd_reset.html',{
                    'user':user,
                    'domain': request.get_host(),
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': ''
                }
                )

            else:
                # return render(request, "user/password_reset.html", {'message':'incorrect email ', 'form':form})
                print(request.get_host())

    context = {
        'form':form
    }

    return render(request, 'user/password_reset.html', context)





def password_reset_request_done(request):

    form = CustomPasswordResetForm()

    context = {
        'form':form
    }

    return render(request, 'user/password_reset.html', context)

