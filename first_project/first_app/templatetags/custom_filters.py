from django import template

register = template.Library()


@register.filter(name = 'add_custom_text')
def add_custom_text(value,custom_text):
    return value + ' ' + str(custom_text)