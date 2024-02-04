from django import template

register = template.Library()


@register.filter(name='times')
def times(num, minus_num):
    return range(num-minus_num)


@register.filter(name='call')
def call(list, num):
    return list[num-1][1]
