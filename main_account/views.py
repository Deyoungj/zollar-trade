from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Account
from user.models import CustomUser


@login_required(login_url='login-register', redirect_field_name='dashboard')
def dashboard(request):

    # print(request.user.account_set)

    user = request.user

    account = Account.objects.filter(user=user)
    print(account)

    context = {
        'user': user,
        'account': account
    }

    return render(request, 'main_account/dashboard.html', context)