from crispy_forms.helper import FormHelper
from django import forms
from home.models import CustomUser
from django.contrib.auth import get_user_model, password_validation, authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    userEmail = forms.CharField(label='', max_length=255,
                                widget=forms.EmailInput(attrs={'class': 'form-control',
                                                               'placeholder': 'johndoe@email.com'}))
    first_name = forms.CharField(label='', max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'John'}))
    last_name = forms.CharField(label='', max_length=255,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Doe'}))
    password1 = forms.CharField(label='', strip=False,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': 'password1',
                                                                  'placeholder': '****'}))
    password2 = forms.CharField(label='', strip=False,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'id': 'password2',
                                                                  'placeholder': '****',
                                                                  'onchange': 'checkPasswordMatch();'}))
    help_text = password_validation.password_validators_help_text_html()


    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('userEmail', 'first_name', 'last_name')


class LoginForm(forms.Form):
    userEmail = forms.CharField(label='', max_length=255,
                                widget=forms.EmailInput(attrs={'class': 'form-control',
                                                               'placeholder': 'johndoe@email.com'}), required=True)
    password1 = forms.CharField(label='', strip=False,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': '****'}), required=True)

    # def clean(self):
    #     userEmail = self.cleaned_data.get('userEmail')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(username=userEmail, password=password)
    #     if not user or not user.is_active:
    #         raise forms.ValidationError("Invalid Password or Email Address")
    #     return self.cleaned_data
    #
    # def login(self, request):
    #     userEmail = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(username=userEmail, password=password)
    #     return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = UserChangeForm.Meta.fields
