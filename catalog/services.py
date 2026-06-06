from django.core.cache import cache
from catalog.models import Product


CACHE_TTL = 60 * 5  # 5 минут


def get_products_by_category(category_id):
    cache_key = f"category_{category_id}"

    products = cache.get(cache_key)
    if products is not None:
        return products

    products = list(
        Product.objects.filter(category_id=category_id).values(
            "id", "name", "price", "image"
        )
    )

    cache.set(cache_key, products, CACHE_TTL)

    return products
