# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def primer_nombre(value):
    if value:
        return value.split(" ")[0]
    return value

@register.filter
def primer_apellido(value):
    if value:
        return value.split(" ")[0]
    return value
