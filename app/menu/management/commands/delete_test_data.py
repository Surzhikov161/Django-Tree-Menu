from django.core.management import BaseCommand
from menu.models import Menu, MenuItem


class Command(BaseCommand):

    def handle(self, *args, **options):
        Menu.objects.all().delete()
        MenuItem.objects.all().delete()
        return
