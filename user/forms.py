from django.contrib.auth.forms import PasswordResetForm

from django import forms




class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={
        'class': 'input',
        'type': 'email',
        'name': 'email',
        'id': 'id_email',
        'autocomplete':"email",
        'maxLength':"254"
        }))

