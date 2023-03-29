from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account, Transaction
from user.models import CustomUser, Profile
from django.conf import settings
from django.core.mail import  EmailMessage
from django.db.models import Sum
import string
import random


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

    transactions = Transaction.objects.filter(user=user)

    withdrawal = Transaction.objects.filter(user=user, status="Approved", transaction="Withdrawals").aggregate(Sum("amount"))
    investment = Transaction.objects.filter(user=user, status="Pending", transaction="Investment").aggregate(Sum("amount"))


    account = Account.objects.filter(user=user).first()
    print(withdrawal['amount__sum'])

    context = {
        'user': user,
        'account': account,
        'transactions': transactions,
        'withdraw': withdrawal['amount__sum'],
        'investment': investment['amount__sum']

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





@login_required(redirect_field_name='changepassword', login_url='login-register')
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

        # print(old_password)
        # print(password)
        # print(confirm_password)


    return render(request, 'main_account/base.html')






def home(request):

    return render(request, 'main_account/index.html')





@login_required(redirect_field_name='contact', login_url='login-register')
def contact(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')

        email_msg = EmailMessage(
            subject= "Contact Customer support",
            body= message,
            to=[settings.ADMIN_EMAIL_CUSTOM]

        )


        email_msg.send()
  
        return redirect('contact_done')
        

        # print(message, username, email)


    return render(request, 'main_account/contact.html')



@login_required(redirect_field_name='contact', login_url='login-register')
def contact_done(request):

    return render(request, 'main_account/contact_done.html')


def refrence_id():
   ref = ''.join([random.choice(string.ascii_uppercase + string.digits) for i in range(26)])
   return ref




def plan(amount):
    
    plan = 'STARTER'

    amount = int(amount)

    if amount >= 50 and amount <= 2999:
        plan = 'STARTER'

    elif amount >= 3000 and amount <= 9999:
        plan = 'STANDARD'

    elif amount >= 10000 and amount <= 29999:
        plan = 'GOLDEN'

    elif amount >= 30000 :
        plan = 'PREMIUM'

    return plan






@login_required(redirect_field_name='invest', login_url='login-register')
def invest(request):

    if request.method == "POST":

        amount = request.POST.get('amount')
        ref = request.POST.get('ref')


        tran = Transaction.objects.create(user=request.user, status='Pending', transaction='Investment',
                                          invest_from='Wallet Address', plan=plan(amount), amount=amount, refrence_id=ref)
        tran.save()

        print(amount, ref)

        return redirect(f"/account/invest-check/{ref}/{amount}/")  
    
    account = Account.objects.filter(user=request.user).first()

    return render(request, 'main_account/invest.html', {'ref':refrence_id(), 'account':account})






@login_required(redirect_field_name='invest', login_url='login-register')
def invest_approved(request, ref, amount):


    context = {
        'ref':ref,
        'amount': amount,
        'email': request.user.email,
        'plan': plan(amount)
    }

    return render(request, 'main_account/invest_approved.html', context)




@login_required(redirect_field_name='transaction', login_url='login-register')
def transactions(request):

    user = request.user

    transactions = Transaction.objects.filter(user=user)
    
    return render(request, 'main_account/transaction_history.html', {'transactions':transactions})




@login_required(redirect_field_name='withdraw', login_url='login-register')
def withdraw(request):
    
    return render(request, 'main_account/withdraw.html')









@login_required(redirect_field_name='withdraw', login_url='login-register')
def referral(request):
    
    return render(request, 'main_account/referral.html')










@login_required(redirect_field_name='dashboard', login_url='login-register')
def redeem(request):
    
    user = request.user

    transactions = Transaction.objects.filter(user=user)

    account = Account.objects.filter(user=user).first()
    print(transactions)

    context = {
        'user': user,
        'account': account,
        'transactions': transactions
    }

    return render(request, 'main_account/dashboard.html', context)













@login_required(redirect_field_name='term', login_url='login-register')
def terms(request):
    
    return render(request, 'main_account/term.html')
