from django.views.generic import ListView
from .models import Column
from article.models import ArticlePost
class CourseIndex(ListView):
    template_name = 'course/index.html'
    queryset = Column.objects.all()
    context_object_name = 'columns'


class CourseDetail(ListView):
    model = ArticlePost
    template_name = 'article/index.html'

    def get_object(self):
        name = self.kwargs.get('name')
        return Column.objects.get(title=name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        column = self.get_object()
        articles = column.articles.all() 
        context['articles'] = articles
        return context

