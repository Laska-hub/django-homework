from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Create user groups"


    def handle(self, *args, **options):

        moderator_group, created = Group.objects.get_or_create(
            name="Модератор продуктов"
        )

        content_manager_group, created = Group.objects.get_or_create(
            name="Контент-менеджер"
        )

        can_unpublish = Permission.objects.get(
            codename="can_unpublish_product"
        )

        delete_product = Permission.objects.get(
            codename="delete_product"
        )

        moderator_group.permissions.add(can_unpublish)
        moderator_group.permissions.add(delete_product)

        self.stdout.write(
            self.style.SUCCESS("Groups created successfully")
        )
