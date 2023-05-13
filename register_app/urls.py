from django.urls import path
from .import views

urlpatterns = [
    path("",views.register,name="Home"),
    path("login/",views.signin,name="Login"),
    path("logout/",views.signout,name="Logout")
]
