from django.http import HttpResponse
from django.core.serializers import serialize
from infoapp.models import Student
import json



class HttpResponseMixin(object):
    def render_http_response(self,data,status=200):
        return HttpResponse(data,content_type='application/json',status=status)

class SerializeMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs)
        p_dict=json.loads(json_data)
        final_list=[]
        for obj in p_dict:
            final_list.append(obj['fields'])
        json_data=json.dumps(final_list)
        return json_data

class GetObjectById(object):
    def get_object_by_id(self,id):
        try:
            s=Student.objects.get(id=id)
        except Student.DoesNotExist:
            s=None
        return s
