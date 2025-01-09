from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ArticlePost,Comment
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(ListView):
    template_name = 'article/index.html'
    queryset = ArticlePost.objects.all()
    paginate_by = 5
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created')
        query = self.request.GET.get('search')
        if query:
                    queryset = queryset.filter(
            Q(title__icontains=query) | Q(body__icontains=query) | Q(author__username__icontains=query)
        )

        
        return queryset

class ArticleDetail(DetailView):
    template_name = 'article/detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')  
        return ArticlePost.objects.get(pk=pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        comments = article.comments.all()  
        context['comments'] = comments
        return context
    

 
    def post(self, request, *args, **kwargs):
        article = self.get_object()  # 获取当前文章对象
        content = request.POST.get('content')  # 获取评论内容
        if not request.user.is_authenticated:
             return redirect('user:login')
        if content:
            comment = Comment(
                article=article,
                content=content,
                author=request.user  # 关联当前登录用户
                )
            comment.save()  # 保存评论
        return redirect('article:detail', pk=article.pk)  # 重定向回文章详情页面


class ArticleCreate(LoginRequiredMixin, CreateView):
    template_name = 'article/create.html'
    model = ArticlePost
    fields = ['title', 'body']
    success_url = '/'
    login_url = '/user/login/'

    def form_valid(self, form):
        # 自动将当前用户设置为作者
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'article/update.html'
    model = ArticlePost
    fields = ['title', 'body']
    success_url = '/'
    login_url = '/user/login/'

    def get_object(self, queryset=None):
        # 获取当前对象
        obj = super().get_object(queryset)
        # 确保当前用户是作者
        if obj.author != self.request.user:
            raise PermissionDenied("You do not have permission to edit this article.")
        return obj

class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = ArticlePost
    success_url = '/'
    login_url = '/user/login/'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author!= self.request.user:
            raise PermissionDenied("You do not have permission to delete this article.")
        return obj
