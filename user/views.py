from django.shortcuts import render
from .models import CustomUser


def register_login(request):

    if request.method == "POST":
        
        if "register-submit" in request.POST:
            full_name = request.POST.get('fullname', None)
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            password2 = request.POST.get('password2', None)

            stored_user = CustomUser.objects.filter(username=username).exists()

            if stored_user:
                print ('user already exist')

            else:
                print('new uaser')
            
        
            # user, created = CustomUser.objects.get_or_create()
            

            # if created:

            #     print('user created')


        if "login-submit" in request.POST:
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            

    return render(request, "user/register-login.html")


