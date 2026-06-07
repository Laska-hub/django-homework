from django.urls import path
from .views import (
    home,
    contacts,
    product_detail,
    category_products
)
from django.conf import settings
from django.conf.urls.static import static

app_name = "catalog"

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('category/<int:category_id>/', category_products, name='category_products'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)