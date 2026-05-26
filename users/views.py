from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from .forms import RegisterForm

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
                phone=form.cleaned_data.get("phone"),
                country=form.cleaned_data.get("country"),
                avatar=form.cleaned_data.get("avatar"),
            )

            send_mail(
                subject="Добро пожаловать!",
                message="Вы успешно зарегистрировались.",
                from_email="test@example.com",
                recipient_list=[user.email],
                fail_silently=True,
            )

            login(request, user)
            return redirect("catalog:product_list")

    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    error = None

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect("catalog:product_list")
        else:
            error = "Неверный email или пароль"

    return render(request, "users/login.html", {"error": error})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["phone", "country", "avatar"]
    template_name = "users/profile.html"

    def get_object(self):
        return self.request.user
