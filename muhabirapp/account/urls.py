from django.urls import path
from . import views

##Sıralama önemli.
urlpatterns = [
    path("login", views.user_login, name="user_login"),
    path("logout", views.user_logout, name="user_logout"),
    path("change-password", views.change_password, name="change_password"),
    path("register", views.user_register, name="user_register"),
]
