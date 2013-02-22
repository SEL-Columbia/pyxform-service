from django.utils import simplejson
from django.http import HttpResponse

from .utils import process_xlsform


@require_POST
def consume_xlsform(request):
    xlsform_file = request.FILES.pop('xlsform_file', [])
    if xlsform_file:
        survey = process_xlsform(xlsform_file[0])
        data = {'xml': survey.to_xml(), 'json': survey.to_json()}
        return HttpResponse(
            simplejson.dumps(data), mimetype='application/json')
