from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login,get_user_model
from django.shortcuts import redirect,render
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import User

User = get_user_model()

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user/update.html'
    fields = ['username','avatar', 'bio']
    success_url = '/user/profile/'  # 更新成功后跳转的页面

    def get_object(self):
        # 返回当前登录用户
        return self.request.user

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'thisuser'

    def get_object(self):
        pk = self.kwargs.get('pk')
        # 如果没有提供 pk 参数，返回当前登录用户
        if pk is None:
            return self.request.user
        # 返回指定 pk 的用户
        return User.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        articles = user.articlepost_set.all()  # 获取该用户的文章
        # 将文章添加到上下文
        context['articles'] = articles
        return context


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        errors = {}

        # 检查用户名是否已存在
        if User.objects.filter(username=username).exists():
            errors['username'] = '用户名已存在。'

        # 检查邮箱是否已存在
        if User.objects.filter(email=email).exists():
            errors['email'] = '该邮箱已被注册。'

        # 检查两次密码是否一致
        if password1 != password2:
            errors['password2'] = '两次输入的密码不一致。'

        # 如果有错误，重新渲染模板并显示错误
        if errors:
            print(errors)
            return render(request, 'user/register.html', {'errors': errors,})

        # 创建用户
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)  # 自动登录新用户
        
        return redirect('/')



class UserLoginView(LoginView):
    template_name = 'user/login.html'
    def get_success_url(self):
        # 优先返回 `next` 参数指定的路径
        return self.request.GET.get('next') or '/'




class UserLogoutView(LogoutView):
    next_page = '/'  # 退出后跳转的页面
