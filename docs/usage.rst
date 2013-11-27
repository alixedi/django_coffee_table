========
Usage
========

To use django_coffee_table in a project::

1. Set up dependencies according to the given docs:

	1. `linaro-django-pagination <https://pypi.python.org/pypi/linaro-django-pagination/>`_
	2. `django-sort <https://pypi.python.org/pypi/django-sort/0.1>`_ 

2. Include `django_coffee_table` in your `INSTALLED_APPS` settings.
3. Open your template and load up the coffee_table tags library::
	{% load coffee_table %}
4. Basic usage::
	{% coffee_table request object_list %}
5. Advanced usage::
	{% coffee_table request object_list	 'name, content_type' %}
