from django.shortcuts import render


def register_login(request):

    return render(request, "user/register-login.html")
