from django.urls import path
from .views import register_view, login_view, ProfileUpdateView

app_name = "users"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
]

