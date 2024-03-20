from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm( request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('https://www.baidu.com/')  
            else:
                return redirect('https://www.baidu.com/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # 将用户保存到数据库中
            # 可以在注册成功后执行其他操作，例如重定向到登录页面或主页
            return redirect('login')  # 注册成功后重定向到登录页面
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request,"home.html")