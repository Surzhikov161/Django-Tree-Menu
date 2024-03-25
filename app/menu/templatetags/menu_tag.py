from django.db.models import Prefetch, prefetch_related_objects
from django import template
from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(
    context: template.RequestContext,
    menu_name: str,
):
    try:
        prefetch = [
            ("items" + "__items" * i) for i in range(context["depth"] + 1)
        ]

        prefetch_setup = [
            Prefetch(
                i,
                queryset=(
                    MenuItem.objects.filter(parent=None)
                    if i == "items"
                    else MenuItem.objects.filter(parent__name=j)
                ),
            )
            for i, j in zip(prefetch, context["path"])
        ]

        menu_filter = filter(
            lambda m: m.name == menu_name, list(context["menus"])
        )
        menu = next(menu_filter)
        prefetch_related_objects(
            [menu],
            *prefetch_setup,
        )

        return {
            "menu": menu,
            "path": context["path"],
        }
    except KeyError:
        return {
            "menu": Menu.objects.get(name=menu_name),
        }
