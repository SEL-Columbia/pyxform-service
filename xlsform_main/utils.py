from pyxform.builder import create_survey_from_xls


def process_xlsform(filepath):
    with open(filepath) as f:
        survey = create_survey_from_xls(f)
        return survey
