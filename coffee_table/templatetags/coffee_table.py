from django.template.loader import get_template
from django.template import Library
from django.db import models

from tag_parser.basetags import BaseNode
from tag_parser import template_tag

register = Library()

@template_tag(register, 'coffee_table')
class CoffeeTableNode(BaseNode):
    """Given a queryset and a good many optional configurations,
    renders the HTML for a table""" 
    max_args = 1
    allowed_kwargs = ('field_accessors', 'paginate_by', 'table_class', 
                      'checkbox_column', 'primary_key_column', 'help_text')

    def get_field(self, model, field_accessor):
        """Given the field_accessor and model, returns the field object. Follow
        ForeignKey relations specified using the __ notation."""
        rmodel = model
        field = None
        for token in field_accessor.split('__'):
            model = rmodel
            field = model._meta.get_field(token)
            if isinstance(field.rel, models.ManyToOneRel) or \
               isinstance(field.rel, models.OneToOneRel):
                rmodel = field.rel.to
        return field

    def render_tag(self, context, *tag_args, **tag_kwargs):
        """Method for rendering the table HTML"""
        (object_list,) = tag_args
        try:
            fields = []
            for field_accessor in tag_kwargs['field_accessors'].split(','):
                field_accessor = field_accessor.strip()
                field = self.get_field(object_list.model, field_accessor)
                fields.append((field_accessor, field))
        except:
            fields = []
            for field in object_list.model._meta.fields:
                fields.append((field.name, field))
        finally:
            context['fields'] = fields
        # optimize the object_list - queryset using select_related
        object_list = object_list.select_related(*[f for f,_ in fields])
        context['object_list'] = object_list
        context.update(tag_kwargs)
        return get_template("coffee_table/coffee_table.html").render(context)

@register.filter
def get_field_type(field):
    """Returns type for the given field"""
    type_str = str(type(field))
    type_str = type_str.lstrip('\'<')
    type_str = type_str.rstrip('\'>')
    return type_str.split('.')[-1]

@register.filter
def get_field_value(obj, field_accessor):
    """Returns value for the given field for a given object. Follow ForeignKey
    relations specified by the __ notation."""
    for token in field_accessor.split('__'):
        obj = getattr(obj, token.strip())
    return obj
