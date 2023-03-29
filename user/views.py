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
from .token import account_token






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

                subject = "Your ZollarTrade account was created successfully"

                message = render_to_string('user/new_account_message.html',{
                    'user':username,
                    'domain': request.get_host(),
                    # 'protocol': 'https' if request.is_secure() else 'http'
                }
                )

                emailmsg = EmailMessage(subject, message, to=[email])

                if emailmsg.send():
                    
                    return redirect('login-register')
            


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

                message = render_to_string('user/password_reset_message.html',{
                    'user':user,
                    'domain': request.get_host(),
                    # 'protocol': 'https' if request.is_secure() else 'http'
                }
                )

                emailmsg = EmailMessage(subject, message, to=[email])

                if emailmsg.send():
                    
                    return redirect('login-register')

                else:
                    return render(request, "user/password_reset.html", {'message':' problem sending email please check if you typed your email correctly. ', 'form':form})

            else:
                return render(request, "user/password_reset.html", {'message':'invalid email ', 'form':form})
                

    context = {
        'form':form
    }

    return render(request, 'user/password_reset.html', context)








def password_reset_request_done(request):



    return render(request, 'user/password_reset_done.html')




def password_reset_request_confirm(request, uidb64, token):

    
    try:
      uid = force_str(urlsafe_base64_decode(uidb64))
      user = CustomUser.objects.filter(pk=uid).first()
    except:
      user = None

    if user is not None and account_token.check_token(user, token):

        if request.method == "POST":
            password1 = request.POST.get('password')
            password2 = request.POST.get('confirmpassword')

            if password1 == password2:

                user.set_password(password1)
                user.save()

                subject = "Password Reset"

                message = render_to_string('user/password_changed_message.html',{
                    'user':user,
                    'domain': request.get_host(),
                    # 'protocol': 'https' if request.is_secure() else 'http'
                }
                )

                emailmsg = EmailMessage(subject, message, to=[user.email])


                if emailmsg.send():
                    return redirect('login-register')
            


            else:
                return render(request, 'user/password_reset_confirm.html', {'message_err':"passwords don't match" } )

                

        
    return render(request, 'user/password_reset_confirm.html' )



    


