from typing import Optional
from django.core.management import BaseCommand
from menu.models import Menu, MenuItem

import random


class Command(BaseCommand):
    menu_amount = 2
    max_depth = 4
    item_amount = 4

    def create_items(
        self,
        menu: Optional[Menu],
        parent: Optional[MenuItem] = None,
        depth: Optional[int] = 0,
    ):
        if depth == self.max_depth:
            if random.random() > 0.5:
                MenuItem.objects.create(
                    name=f"last item",
                    menu=menu,
                    parent=parent,
                    data="Some data",
                )
                return
            MenuItem.objects.create(
                name=f"last item",
                menu=menu,
                parent=parent,
                link="http://endless.horse/",
                data="Some link",
            )
            return

        for i in range(1, self.item_amount + 1):
            item = MenuItem.objects.create(
                name=f"{i}-item in {depth} depth",
                menu=menu,
                parent=parent,
            )
            self.create_items(menu=None, parent=item, depth=(depth + 1))

    def create_menus(self):
        for i in range(1, self.menu_amount + 1):
            name = f"Menu-{i}"
            menu = Menu.objects.create(name=name)
            self.create_items(
                menu=menu,
            )

    def handle(self, *args, **options) -> str | None:
        self.create_menus()
        return
