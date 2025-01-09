from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

User = get_user_model()  # 获取自定义的用户模型

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="用户名")
    email = forms.EmailField(required=True, label="邮箱")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="密码")
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True, label="确认密码")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("用户名已存在")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("密码必须至少包含8个字符")
        return password

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError("两次密码输入不一致")
        return password_confirm

    def save(self):
        # 保存用户数据
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # 创建用户并加密密码
        user = User(username=username, email=email, password=make_password(password))
        user.save()
        return user
