from django.shortcuts import render
from django.views.generic import View
from infoapp.utils import is_json
from infoapp.mixins import HttpResponseMixin,SerializeMixin,GetObjectById
import json
from infoapp.models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from infoapp.forms import StudentForm

@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUD(HttpResponseMixin,SerializeMixin,GetObjectById,View):
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_http_response(json.dumps({'msg':'please provide valid json data'}),status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            std=self.get_object_by_id(id)
            if std is None:
                return self.render_http_response(json.dumps({'msg':'not matched record found with given id'}),status=400)
            json_data=self.serialize([std,])
            return self.render_http_response(json_data)
        qs=Student.objects.all()
        json_data=self.serialize(qs)
        return self.render_http_response(json_data)
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_http_response(json.dumps({'msg':'please provide valid json data'}),status=400)
        std_data=json.loads(data)
        form=StudentForm(std_data)
        if form.is_valid():
            form.save(commit=True)
            return self.render_http_response(json.dumps({'msg':'Resource created successfully'}))
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_http_response(json_data,status=400)
    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_http_response(json.dumps({'msg':'please provide valid json data'}),status=400)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            return self.render_http_response(json.dumps({'msg':'To perfrom updation id is mandatory'}),status=400)
        std=self.get_object_by_id(id)
        if std is None:
                return self.render_http_response(json.dumps({'msg':'No matched record found with the given id'}),status=400)
        original_date={
        'name':std.name,
        'rollno':std.rollno,
        'marks':std.marks,
        'location':std.location,
        }
        original_date.update(provided_data)
        form=StudentForm(original_date,instance=std)
        if form.is_valid():
            form.save(commit=True)
            return self.render_http_response(json.dumps({'msg':'Resources updated successfully'}))
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_http_response(json_data,status=400)
    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_http_response(json.dumps({'msg':'Please provide valid json data'}),status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is None:
            return self.render_http_response(json.dumps({'msg':'To deletion id is mandatory please provide'}),status=400)
        std=self.get_object_by_id(id)
        if std is None:
            return self.render_http_response(json.dumps({'msg':'No matched record found with the given id'}),status=400)
        status,deleted_item=std.delete()
        if status==1:
            json_data=json.dumps({'msg':'Resource Deleted successfully'})
            return self.render_http_response(json_data)
        json_data=json.dumps({'msg':'unable to delte.. plzz try again'})
        return self.render_http_response(json_data,status=500)
