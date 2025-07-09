from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    if isinstance(d, dict):
        return d.get(key, '')

@register.filter
def pretty_area_name(value):
    nombres = {
        'historia': 'Historia',
        'bellas_artes': 'Bellas Artes',
        'antropologia': 'Antropología'
    }
    return nombres.get(value.lower(), value.capitalize())

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, "")

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})