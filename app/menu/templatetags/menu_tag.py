from django.db.models import Prefetch, prefetch_related_objects
from django import template
from menu.models import Menu, MenuItem
from django.db.models import Q

register = template.Library()


@register.filter
def lookup(d, key):
    return d[key]


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(
    context: template.RequestContext,
    menu_name: str,
):
    try:
        menu_filter = filter(
            lambda m: m.name == menu_name, list(context["menus"])
        )
        menu = next(menu_filter)
        all_items = (
            MenuItem.objects.filter(
                Q(parent=None, menu__name=menu_name)
                | Q(parent__name__in=context["path"])
            )
            .select_related("parent")
            .select_related("menu")
        )

        grouped_items = [
            list(filter(lambda i: i.parent == None, list(all_items)))
        ] + [
            list(
                filter(
                    lambda i: i.parent and i.parent.name == name,
                    list(all_items),
                )
            )
            for name in context["path"]
        ]
        grouped_items = list(filter(lambda l: len(l) > 0, grouped_items))
        return {
            "items": grouped_items,
            "menu": menu,
            "index": 0,
            "path": context["path"],
        }
    except KeyError:
        return {
            "menu": Menu.objects.get(name=menu_name),
        }
