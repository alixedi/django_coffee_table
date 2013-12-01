from django.template.loader import get_template
from django.template import Library
from tag_parser.basetags import BaseNode
from tag_parser import template_tag

register = Library()

@template_tag(register, 'coffee_table2')
class CoffeeTableNode(BaseNode):
    """Given a queryset and a good many optional configurations,
    renders the HTML for a table""" 
    max_args = 1
    allowed_kwargs = ('field_names', 'paginate_by', 'table_class', 
                      'checkbox_column', 'primary_key_column', 'help_text')

    def render_tag(self, context, *tag_args, **tag_kwargs):
        """Method for rendering the table HTML"""
        (object_list,) = tag_args
        context['object_list'] = object_list
        meta = object_list.model._meta
        try:
            fns = tag_kwargs['field_names'].split(',')
            fs = [meta.get_field_by_name(fn.strip())[0] for fn in fns]
            context['fields'] = fs
        except:
            print meta
            context['fields'] = meta.fields
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
def get_field_value(obj, field_name):
    """Returns value for the given field for a given object"""
    return getattr(obj, field_name, None)
