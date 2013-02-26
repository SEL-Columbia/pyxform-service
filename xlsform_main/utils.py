from django.core.files.base import File

from pyxform.builder import create_survey_from_xls


def process_xlsform(filepath):

    '''Genrates a pyxform survey object from a filepath or file object'''

    survey = None
    if isinstance(filepath, File):
        survey = create_survey_from_xls(filepath)
    else:
        with open(filepath) as f:
            survey = create_survey_from_xls(f)
    return survey
