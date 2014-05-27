=============================
django_coffee_table
=============================

.. image:: https://badge.fury.io/py/django_coffee_table.png
    :target: http://badge.fury.io/py/django_coffee_table

.. image:: https://travis-ci.org/alixedi/django_coffee_table.png?branch=master
        :target: https://travis-ci.org/alixedi/django_coffee_table

.. image:: https://pypip.in/d/django_coffee_table/badge.png
        :target: https://crate.io/packages/django_coffee_table?version=latest

.. image:: https://coveralls.io/repos/alixedi/django_coffee_table/badge.png?branch=master
  :target: https://coveralls.io/r/alixedi/django_coffee_table?branch=master


Control of html tables - paging, sorting, css, checkbox column, primary-key column, help text,  custom columns, model field columns, foreign key field columns etc. in templates with a beautiful declarative syntax.

If the above is not enough, Coffee Table will automatically optimize your query using select_related so that each page of the table will be rendered by a single SQL query.

Installation
------------

CoffeeTable is at the cheeseshop: ::

    pip install django_coffee_table

Usage
-----

To use coffee_table in your project:

1. Set up dependencies according to their respective documentation:

* `linaro-django-pagination <https://pypi.python.org/pypi/linaro-django-pagination/>`_
* `django-resort <https://pypi.python.org/pypi/django_resort/0.1.0>`_
* `django-tag-parser <https://pypi.python.org/pypi/django-tag-parser>`_

2. Include `django_coffee_table` in your `INSTALLED_APPS`.

3. Open your template and load up the coffee_table tags library::

    {% load coffee_table %}

4. Basic usage::

    {% coffee_table object_list %}

5. Advanced usage::

    {% coffee_table object_list field_accessors='name, content_type__app_label'
                                paginate_by='10'
                                table_class='table table-condensed'
                                checkbox_column=True
                                primary_key_column=True
                                help_text=True %}

Please see the included test project for more help.
