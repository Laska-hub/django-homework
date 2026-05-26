from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse, reverse_lazy

from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        obj.views_count += 1
        obj.save()

        if obj.views_count == 100:
            send_mail(
                subject="Поздравляем!",
                message=f'Статья "{obj.title}" набрала 100 просмотров!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )

        return obj


class BlogCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    model = Blog

    fields = [
        "title",
        "content",
        "preview",
        "is_published",
    ]

    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:list")

    def test_func(self):
        return self.request.user.groups.filter(
            name="Контент-менеджер"
        ).exists()


class BlogUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = Blog

    fields = [
        "title",
        "content",
        "preview",
        "is_published",
    ]

    template_name = "blog/blog_form.html"

    def test_func(self):
        return self.request.user.groups.filter(
            name="Контент-менеджер"
        ).exists()

    def get_success_url(self):
        return reverse("blog:detail", args=[self.object.pk])


class BlogDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:list")

    def test_func(self):
        return self.request.user.groups.filter(
            name="Контент-менеджер"
        ).exists()
