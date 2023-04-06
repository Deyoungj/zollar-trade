from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account, Transaction
from user.models import CustomUser, Profile
from django.conf import settings
from django.core.mail import  EmailMessage
from django.template.loader import render_to_string
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

    transactions = Transaction.objects.filter(user=user).order_by("-date")

    withdrawal = Transaction.objects.filter(user=user, status="Approved", transaction="Withdrawals").aggregate(Sum("amount"))
    investment = Transaction.objects.filter(user=user, status="Approved", transaction="Investment").aggregate(Sum("amount"))


    account = Account.objects.filter(user=user).first()
    print(transactions[0])

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

    return render(request, 'main_account/home/index.html')


def home_about(request):

    return render(request, 'main_account/home/about.html')


def home_contact(request):

    if request.method == "POST":

        fullname = request.POST.get('fullname', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        message = request.POST.get('message', None)

        msg = f"fullname: {fullname} \n"

        msg += f"email: {email} \n \n"
        msg += f"email: {phone} \n "
        msg += f"{message}"

        email_msg = EmailMessage(
            subject= "Contact Customer support",
            body= msg,
            to=[settings.ADMIN_EMAIL_CUSTOM]

        )


        email_msg.send()
  
        return redirect('home')
        

    return render(request, 'main_account/home/contact.html')

def home_faq(request):

    return render(request, 'main_account/home/faq.html')






@login_required(redirect_field_name='contact', login_url='login-register')
def contact(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')

        msg = f"username: {username} \n"

        msg += f"email: {email} \n \n"
        msg += f"{message}"

        email_msg = EmailMessage(
            subject= "Contact Customer support",
            body= msg,
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

        subject = "Investment Request"

        message = render_to_string('main_account/message/invest_message.html',{
            'user':request.user,
            'plan': plan(amount),
            'amount': amount,
            'ref': ref,
            'status': 'Pending'
            # 'domain': request.get_host(),
            # 'protocol': 'https' if request.is_secure() else 'http'
        }
        )

        emailmsg = EmailMessage(subject, message, to=[request.user.email])

        if emailmsg.send():

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

    transactions = Transaction.objects.filter(user=user).order_by("-date")
    
    return render(request, 'main_account/transaction_history.html', {'transactions':transactions})






def send_to_admin(user, plan, amount, wallet, ref):

    subject_m = "Withdrawal Request from user"

    message_m = render_to_string('main_account/message/withdraw_message.html',{
        'user':user,
        'plan': plan,
        'amount': amount,
        'wallet_address': wallet,
        'ref': ref,
        'status': 'Pending'
        # 'domain': request.get_host(),
        # 'protocol': 'https' if request.is_secure() else 'http'
    }
    )

    emailmsg_m = EmailMessage(subject_m, message_m, to=[settings.ADMIN_EMAIL_CUSTOM])

    emailmsg_m.send()








@login_required(redirect_field_name='withdraw', login_url='login-register')
def withdraw(request):

    p_wallet = Profile.objects.filter(user=request.user).first()
    if request.method == "POST":

        wallet_address = ''
        w_type = ''
        ref = refrence_id()
        wallet = request.POST.get("address")
        amount = request.POST.get("customAmount")

        if wallet == 'btc':
            wallet_address = p_wallet.BTC_Wallet_Address
            w_type = 'btc'

        
        if wallet == 'eth':
            wallet_address = p_wallet.Ethereum_Bep20_Address
            w_type = 'eth'

        
        if wallet == 'teth':
            wallet_address = p_wallet.Tether_USDT_TRC20

            w_type = 'teth'

        t = Transaction.objects.filter(user=request.user).order_by("-date").first()




        tran = Transaction.objects.create(user=request.user, status='Pending', transaction='Withdrawal',
                                          invest_from='Wallet Address', plan=t.plan, amount=amount, refrence_id=ref)
        
        tran.save()

       

        



        subject = "Withdrawal Request"

        message = render_to_string('main_account/message/withdraw_message.html',{
            'user':request.user,
            'plan': t.plan,
            'amount': amount,
            'w_type': w_type,
            'wallet_address': wallet_address,
            'ref': ref,
            'status': 'Pending'
            # 'domain': request.get_host(),
            # 'protocol': 'https' if request.is_secure() else 'http'
        }
        )
        
        emailmsg = EmailMessage(subject, message, to=[request.user.email])



        if emailmsg.send():

            return redirect('withdraw-done')  


        

        # print(t.plan)
        # print(amount)


    bal = Account.objects.filter(user=request.user).first()

    wallet = Profile.objects.filter(user=request.user).first()

    
    
    context = {
        'bal':bal,
        'wallet': wallet
    }
    return render(request, 'main_account/withdraw.html', context)








@login_required(redirect_field_name='withdraw', login_url='login-register')
def withdrawal_approved(request):


    return render(request, 'main_account/withdraw_done.html', )





def refrence_code():
   ref = ''.join([random.choice(string.ascii_uppercase ) for i in range(10)])
   return ref


@login_required(redirect_field_name='referral', login_url='login-register')
def referral(request):

    ref = f"{request.get_host()}/user/referral-signup/{refrence_code()}/"
    
    return render(request, 'main_account/referral.html', {'ref':ref})











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
