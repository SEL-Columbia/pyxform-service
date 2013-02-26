from django.utils import simplejson
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .utils import process_xlsform


@csrf_exempt
@require_POST
def consume_xlsform(request):
    xlsform_file = request.FILES.pop('xlsform_file', [])
    if xlsform_file:
        data = {'status': 'error'}
        response =  HttpResponse(mimetype='application/json')
        try:
            survey = process_xlsform(xlsform_file[0])
            xml_data = survey.to_xml()
        except Exception, e:
            data['status'] = 'error'
            data['message'] = unicode(e)
            response.status_code = 400
        else:
            data = {
                    'xml': xml_data,
                    'json': survey.to_json(),
                    'status': 'success'}
        response.content = simplejson.dumps(data)
        return response
    else:
        return HttpResponseBadRequest(
            simplejson.dumps(
                {'status': 'error', 'message': u"Missing xlsform file"}),
            mimetype='application/json')
