from django.template import Context
from django.template.loader import get_template
from django import template


register = template.Library()

@register.simple_tag
def coffee_table(request, object_list, field_names=None):
    """Render a table from given queryset"""
    all_fields = object_list.model._meta.fields
    if field_names is None:
        field_names = [field.name for field in all_fields]
    else:
        field_names = field_names.split(',')
    fields = []
    for field_name in field_names:
        field_name = field_name.strip()
        for field in all_fields:
            if field.name == field_name:
                fields.append(field)
    return get_template("coffee_table/coffee_table.html").render(
        Context({
            'request': request,
            'object_list': object_list,
            'fields': fields
        }))

@register.filter
def get_field_type(field):
    """
    Returns type for the given field. Fields here refer to 
    field of object. To be used in 
    ListView.
    """
    type_str = str(type(field))
    type_str = type_str.lstrip('\'<')
    type_str = type_str.rstrip('\'>')
    return type_str.split('.')[-1]

@register.filter
def get_field_value(obj, field_name):
    """
    Returns value for the given field for a given object.
    Fields here refer to field of object. To be used in 
    ListView.
    """
    related_names = field_name.split('__')
    for related_name in related_names:
        obj = getattr(obj, related_name, None)
    return obj