from django.urls import path,include
from testzwj.views import login_view,register,home

urlpatterns = [
    path("login/",login_view,name="login"),
    path("register/",register,name="register"),
    path("home/",home,name="home")
]