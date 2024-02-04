from django import template

from ..models import MenuItem

register = template.Library()


def add_to_menu(menu, parental, parent, n):
    menu.append((parent, n))
    if parent.pk in parental.keys():
        for item in parental[parent.pk]:
            menu = add_to_menu(menu, parental, item, n+1)
    return menu


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name)
    parental = {}
    for item in menu_items:
        if item.parent_item in parental:
            parental[item.parent_item].append(item)
        else:
            parental[item.parent_item] = [item]
    menu = []
    for item in parental[0]:
        menu = add_to_menu(menu, parental, item, 0)
    context = {
        'path': context.request.path[1:],
        'menu_items': menu,
        'menu_name': menu_name,
    }
    return context
