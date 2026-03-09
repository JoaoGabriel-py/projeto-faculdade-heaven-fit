from django import template
register = template.Library()


@register.filter
def celular_formato(value):
    if len(value) == 11: # Celular: (XX) 9XXXX-XXXX
        return f"({value[:2]}) {value[2:7]}-{value[7:]}"
    elif len(value) == 10: # Fixo: (XX) XXXX-XXXX
        return f"({value[:2]}) {value[2:6]}-{value[6:]}"
    return value
