=============================
django_coffee_table
=============================

..
	.. image:: https://badge.fury.io/py/django_coffee_table.png
	    :target: http://badge.fury.io/py/django_coffee_table
	    
	.. image:: https://travis-ci.org/alixedi/django_coffee_table.png?branch=master
	        :target: https://travis-ci.org/alixedi/django_coffee_table
	
	.. image:: https://pypip.in/d/django_coffee_table/badge.png
	        :target: https://crate.io/packages/django_coffee_table?version=latest


Control of tables in templates sans BS.

Installation
------------

we are at the cheeseshop: ::

	pip install django_coffee_table

Usage
-----

Read on: 

1. Set up dependencies according to the given docs:
	* `linaro-django-pagination <https://pypi.python.org/pypi/linaro-django-pagination/>`_
	* `django-sort <https://pypi.python.org/pypi/django-sort/0.1>`_ 

2. Include `django_coffee_table` in your `INSTALLED_APPS` settings.

3. Open your template and load up the coffee_table tags library::

	{% load coffee_table %}

4. Basic usage::

	{% coffee_table request object_list %}

5. Advanced usage::

	{% coffee_table request object_list 'name, content_type' %}
