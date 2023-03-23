from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account
from user.models import CustomUser, Profile
import os



def with_img(request):

    profile = Profile.objects.filter(user = request.user).first()

    profile.user.full_name = request.POST.get('fullname', None)
    profile.user.username = request.POST.get('username', None)
    profile.user.email = request.POST.get('email', None)
    profile.phone_number = request.POST.get('phone', None)
    profile.address = request.POST.get('address', None)
    profile.country = request.POST.get('country', None)
    profile.BTC_Wallet_Address = request.POST.get('btc', None)
    profile.Ethereum_Bep20_Address = request.POST.get('ethereum', None)
    profile.Tether_USDT_TRC20 = request.POST.get('usdt', None)



    

    profile.image = request.FILES.get('profilepic', None)
    profile.save()

    return redirect('profile')





@login_required(login_url='login-register', redirect_field_name='dashboard')
def dashboard(request):

    # print(request.user.account_set)

    user = request.user

    account = Account.objects.filter(user=user).first()
    print(user.username)

    context = {
        'user': user,
        'account': account
    }

    return render(request, 'main_account/dashboard.html', context)




@login_required(redirect_field_name='profile', login_url='login-register')
def profile(request):

    if request.method == "POST":

        if request.FILES.get('profilepic', None) is not None:
            
            with_img(request)

        else:

        # user_pic = request.user.profile.image
            profile = Profile.objects.filter(user = request.user).first()

            profile.user.full_name = request.POST.get('fullname', None)
            profile.user.username = request.POST.get('username', None)
            profile.user.email = request.POST.get('email', None)
            profile.phone_number = request.POST.get('phone', None)
            profile.address = request.POST.get('address', None)
            profile.country = request.POST.get('country', None)
            profile.BTC_Wallet_Address = request.POST.get('btc', None)
            profile.Ethereum_Bep20_Address = request.POST.get('ethereum', None)
            profile.Tether_USDT_TRC20 = request.POST.get('usdt', None)
        
            profile.save()

        

    

    context = {
        'user' : request.user,
        'profile': Profile.objects.filter(user = request.user).first(),
        'number': Profile.objects.filter(user = request.user).first().phone_number
    }
    return render(request, 'main_account/profile.html', context)





@login_required(redirect_field_name='profile', login_url='login-register')
def change_password(request):

    if request.method == "POST":

        old_password = request.POST.get('oldpassword')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        if not request.user.check_password(old_password):
            msg = "invalid passord"
            success = False
            return render(request, 'main_account/change_password.html', {"message": msg, "success":success})

        else:
            
            if password == confirm_password:
                
                user = CustomUser.objects.filter(email=request.user.email).first()
                user.set_password(password)
                user.save()

                return render(request, 'main_account/change_password.html', {"message": 'Password Updated', "success":True})


            else:
                return render(request, 'main_account/change_password.html', {"message": 'Passwords don`t match', "success":False})

        print(old_password)
        print(password)
        print(confirm_password)


    return render(request, 'main_account/base.html')



@login_required(redirect_field_name='profile', login_url='login-register')
def support(request):

    return render(request, 'main_account/support.html')




@login_required(redirect_field_name='profile', login_url='login-register')
def invest(request):
    
    return render(request, 'main_account/invest.html')



@login_required(redirect_field_name='profile', login_url='login-register')
def terms(request):
    
    return render(request, 'main_account/term.html')
