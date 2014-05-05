#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_coffee_table
------------

Tests for `django_coffee_table` modules module.
"""

import os
import shutil
import unittest

from django.db import models

class StarWar(models.Model):
	part = models.CharField(max_length=3, primary_key=True)
	name = models.CharField(max_length=32)
	medium = models.CharField(max_length=8, 
				choices=(('TV', 'TV'), ('Film', 'Film')))

	def __unicode__(self):
		return self.name

records = [{'part': 'I', 'name': 'The Phantom Menace', 'medium': 'Film'},
		   {'part': 'II', 'name': 'Attack of the Clones', 'medium': 'Film'}]

class TestCoffeeTable(unittest.TestCase):

    def setUp(self):
    	for record in records:
    		StarWar.objects.create(**record)


    def test_something(self):
    	print StarWar.objects.all()

    def tearDown(self):
        pass