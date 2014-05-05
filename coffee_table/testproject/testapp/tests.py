"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command

from os.path import abspath, dirname, join
PROJECT_ROOT = abspath(dirname(__file__))

class SimpleTest(TestCase):

    def setUp(self):
        # load up the data

        call_command('loaddata', join(PROJECT_ROOT, 'fixtures/testapp.json'))
        # setup client
        self.client = Client()

    def test_basic_tag(self):
        """
        Tests the basic coffee_table tag
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        control = '''<div class="table-collapse" style="overflow:auto"> 
                     <table class="table"> <thead> <tr> <th> 
                     <a href="./?sort_by=name">Name</a> <sup> </sup> </th> 
                     <th> <a href="./?sort_by=medium">Medium</a> <sup> 
                     </sup> </th> <th>Extra Header</th> </tr> </thead> 
                     <tbody> <tr> <td>Star Wars</td> <td>Book</td> 
                     <td>Extra Column</td> </tr> <tr> <td>The Phantom 
                     Menice</td> <td>Film</td> <td>Extra Column</td> 
                     </tr> <tr> <td>Return of the Jedi</td> <td>Film</td> 
                     <td>Extra Column</td> </tr> <tr> <td>Caravan of 
                     Courage</td> <td>TV</td> <td>Extra Column</td> </tr> 
                     <tr> <td>The Clone Wars</td> <td>TV</td> <td>Extra 
                     Column</td> </tr> <tr> <td>Rebel Alliance</td> 
                     <td>Game</td> <td>Extra Column</td> </tr> <tr> 
                     <td>Empire At War</td> <td>Game</td> <td>Extra 
                     Column</td> </tr> </tbody> </table></div>'''
        self.assertHTMLEqual(response.rendered_content, control)
