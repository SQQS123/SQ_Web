"""
to check whether the form is legal
"""
from django import forms
from .models import Users


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20, min_length=6, label="账号",
                               help_text="最小6位，最长20位")
    password = forms.CharField(max_length=12, min_length=6, label="密码",
                               widget=forms.PasswordInput(),
                               help_text="最小6位，最长12位")
    portrait = forms.ImageField(label="头像", required=False)

    class Meta:
        model = Users
        fields = ['username', 'password', 'portrait']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=6, label="账号",
                               help_text="最小6位，最长20位")
    password = forms.CharField(max_length=12, min_length=6, label="密码",
                               widget=forms.PasswordInput(),
                               help_text="最小6位，最长12位")
