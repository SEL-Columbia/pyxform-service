import os
import codecs

from xlsform_main.utils import process_xlsform

from django.test import TestCase


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

