from django.urls import path
from .views import *
app_name = 'article'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article'),
    path('article/create/', ArticleCreate.as_view(), name='create'),
    path('article/detail/<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name='update'),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name='delete'),
]