from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index, name="home"),
    path("profile/", views.profile_view, name="profile"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("add/", views.add, name="add"),
    path("check/<int:todo_id>", views.check, name="check"),
    path("uncheck/<int:todo_id>", views.uncheck, name="uncheck"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
]