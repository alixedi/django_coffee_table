========
Usage
========

To use django_coffee_table in a project::

1. Set up dependencies according to the given docs:
	* `linaro-django-pagination <https://pypi.python.org/pypi/linaro-django-pagination/>`_
	* `django-sort <https://pypi.python.org/pypi/django-sort/0.1>`_ 
	* `django-tag-parser <https://pypi.python.org/pypi/django-tag-parser>`_ 

2. Include `django_coffee_table` in your `INSTALLED_APPS` settings.

3. Open your template and load up the coffee_table tags library::

	{% load coffee_table %}

4. Basic usage::

	{% coffee_table object_list %}

5. Advanced usage::

	{% coffee_table object_list field_names='name, content_type' 
			    				paginate_by='10' 
							    table_class='table table-condensed' 
							    checkbox_column=True 
							    primary_key_column=True 
							    help_text=True %}
