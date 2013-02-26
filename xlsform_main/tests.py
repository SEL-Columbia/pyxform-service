import os
import codecs

from django.core.urlresolvers import reverse

from xlsform_main.utils import process_xlsform
from xlsform_main.views import consume_xlsform

from django.test import TestCase
from django.test.client import Client


class XLSFormTest(TestCase):

    this_directory = os.path.dirname(__file__)

    def test_process_xlsform(self):
        xls_file = os.path.join(
            self.this_directory, 'fixtures', 'transportation.xls')
        xml_file = os.path.join(
            self.this_directory, 'fixtures', 'transportation.xml')
        survey = process_xlsform(xls_file)
        self.maxDiff = None
        with codecs.open(xml_file, 'rb', encoding='utf-8') as f:
            self.assertMultiLineEqual(survey.to_xml(), f.read())

    def test_consume_xlsform_view(self):
        xls_file = os.path.join(
            self.this_directory, 'fixtures', 'transportation.xls')
        url = reverse(consume_xlsform)
        client = Client()
        with open(xls_file) as f:
            res = client.post(url, {'xlsform_file': f})
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res['Content-Type'], 'application/json')

    def test_consume_xlsform_bad_request(self):
        xls_file = os.path.join(
            self.this_directory, 'fixtures', 'transportation_bad.xls')
        url = reverse(consume_xlsform)
        client = Client()
        with open(xls_file) as f:
            res = client.post(url, {'xlsform_file': f})
            self.assertEqual(res.status_code, 400)
            self.assertEqual(res['Content-Type'], 'application/json')

