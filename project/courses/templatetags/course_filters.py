from django import template

register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None


@register.filter
def addclass(field, class_attr):
    return field.as_widget(attrs={'class': class_attr})
