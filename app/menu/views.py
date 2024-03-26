from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Menu


# Create your views here.
def index(request):
    return render(
        request, "menu/base.html", context={"menus": Menu.objects.all()}
    )


def draw_menu(request, path):
    _path = path.split("/")
    context = {
        "menus": Menu.objects.all(),
        "menu_name": _path[0],
        "path": _path,
    }
    if context["menu_name"] not in [menu.name for menu in context["menus"]]:
        return HttpResponseNotFound()

    return render(
        request,
        "menu/base.html",
        context=context,
    )
