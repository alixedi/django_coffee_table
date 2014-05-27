from django.test.client import Client
from django.core.management import call_command
from django.core.urlresolvers import reverse

# Very important - sexy css selectors to test template output
# All we have here is templaets so this was a life-saver!
# Please star: https://github.com/johnpaulett/django-with-asserts
from with_asserts.case import TestCase

from os.path import abspath, dirname, join
PROJECT_ROOT = abspath(dirname(__file__))


class CoffeeTableTest(TestCase):

    def setUp(self):
        call_command('loaddata', join(PROJECT_ROOT, 'fixtures/testapp.json'))
        self.client = Client()

    def test_basic(self):
        """
        Tests the basic coffee_table tag - sans frills.
        """
        response = self.client.get(reverse('basic') + '?sort_by=name')
        self.assertEqual(response.status_code, 200)

        # so the number of rows should be equal to the objects in our db
        with self.assertHTML(response, 'tr') as rows:
            self.assertEqual(8, len(rows))

        # sorted by Name column, first entry will be "Caravan.."
        with self.assertHTML(response,
                             'tr:nth-child(1) > td:nth-child(1)') as (td,):
            self.assertHTMLEqual('Caravan of Courage', td.text)

        # of course it should have all the fields in our db
        with self.assertHTML(response, 'th > a') as thas:
            self.assertHTMLEqual('Name', thas[0].text)
            self.assertHTMLEqual('Medium', thas[1].text)

        # and the last column should be the customizable extra column that comes
        # with coffee table
        with self.assertHTML(response, 'th:nth-child(3)') as (th,):
            self.assertHTMLEqual('My Header', th.text)

    def test_paging(self):
        """
        Tests the paging feature
        """
        # page 1
        response = self.client.get(reverse('paging'))
        self.assertEqual(response.status_code, 200)

        # for page-length equals 5, number of rows will be 5 + header row
        with self.assertHTML(response, 'tr') as rows:
            self.assertEqual(6, len(rows))

        # a pagination div should be present
        with self.assertHTML(response, '.pagination') as divs:
            self.assertEqual(1, len(divs))

        # as well as links for pages "1" and "2"
        with self.assertHTML(response, '.page') as pages:
            self.assertEqual(2, len(pages))

        # and finally a link for next
        with self.assertHTML(response, 'a.page') as nxt:
            self.assertEqual(1, len(nxt))

        # page 2
        response = self.client.get(reverse('paging') + '?page_object_list=2')
        self.assertEqual(response.status_code, 200)

        # should have a couple of entries +  header row
        with self.assertHTML(response, 'tr') as rows:
            self.assertEqual(3, len(rows))

        # a pagination div as before
        with self.assertHTML(response, '.pagination') as divs:
            self.assertEqual(1, len(divs))

        # links for pages "1" and "2"
        with self.assertHTML(response, '.page') as pages:
            self.assertEqual(2, len(pages))

        # and a link for prev
        with self.assertHTML(response, 'a.page') as nxt:
            self.assertEqual(1, len(nxt))

    def test_help(self):
        """
        Tests the help feature
        """
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)

        # so help means a tooltip with text pulled from model's help_text
        with self.assertHTML(response, 'a[data-toggle="tooltip"]') as tips:
            self.assertEqual(2, len(tips))
            self.assertEqual('Name of Release', tips[0].attrib['title'])
            self.assertEqual('Medium of Release', tips[1].attrib['title'])

    def test_check(self):
        """
        Tests the checkbox feature
        """
        response = self.client.get(reverse('check'))
        self.assertEqual(response.status_code, 200)

        # checkbox puts a colomn of checkboxes - standard web
        with self.assertHTML(response, 'input[type="checkbox"]') as checks:
            self.assertEqual(8, len(checks))

    def test_css(self):
        """
        Tests the css table class feature
        """
        response = self.client.get(reverse('css'))
        self.assertEqual(response.status_code, 200)

        # here, the table should have a custom class - table-condensed
        with self.assertHTML(response, 'table') as (table,):
            self.assertEqual("table table-condensed", table.attrib['class'])

    def test_pkcol(self):
        """
        Tests the primary key column feature
        """
        response = self.client.get(reverse('pkcol'))
        self.assertEqual(response.status_code, 200)

        # check for the presence of primary_key column - here its id
        with self.assertHTML(response, 'th:nth-child(1) > a') as pk:
            self.assertEqual(1, len(pk))
            self.assertHTMLEqual("Id", pk[0].text)

    def test_full(self):
        """
        Tests the full features
        """
        response = self.client.get(reverse('full') + '?sort_by=name')
        self.assertEqual(response.status_code, 200)

        # test sorting
        with self.assertHTML(response,
                             'tr:nth-child(1) > td:nth-child(2)') as (td,):
           self.assertHTMLEqual('Caravan of Courage', td.text)

        # columns - here we are using the __ notation to access deep columns
        with self.assertHTML(response, 'th > a') as thas:
            self.assertHTMLEqual('Name', thas[0].text)
            self.assertHTMLEqual('Name', thas[1].text)

        # check custom column
        with self.assertHTML(response, 'th:nth-child(4)') as (th,):
            self.assertHTMLEqual('My Header', th.text)

        # check paging - 6 rows instead of 8
        with self.assertHTML(response, 'tr') as rows:
            self.assertEqual(6, len(rows))

        # check pagination div
        with self.assertHTML(response, '.pagination') as divs:
            self.assertEqual(1, len(divs))

        # check page links
        with self.assertHTML(response, '.page') as pages:
            self.assertEqual(2, len(pages))

        # check next link
        with self.assertHTML(response, 'a.page') as nxt:
            self.assertEqual(1, len(nxt))

        # check tooltip
        with self.assertHTML(response, 'a[data-toggle="tooltip"]') as tips:
            self.assertEqual(2, len(tips))
            self.assertEqual('Name of Release', tips[0].attrib['title'])
            self.assertEqual('Name of Medium', tips[1].attrib['title'])

        # check for checkbox column
        with self.assertHTML(response, 'input[type="checkbox"]') as checks:
            self.assertEqual(6, len(checks))

        # check for the table having table-condensed class
        with self.assertHTML(response, 'table') as (table,):
            self.assertEqual("table table-condensed", table.attrib['class'])
