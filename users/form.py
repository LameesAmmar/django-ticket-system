from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from users.models import User


class RegisterCustomerForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #username = None

    class Meta:  # Corrected from Mete to Meta

        model = User
        fields=['email','username','password1', 'password2']