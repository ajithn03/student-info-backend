import requests
import json

base_url='http://127.0.0.1:8000/'
endpoint='api/'
def get_resources(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    response=requests.get(base_url+endpoint,data=json.dumps(data))
    print(response.status_code)
    print(response.json())
get_resources(100)

def create_resource():
    new_std={
    'name':'ajith',
    'rollno':502,
    'marks':99,
    'location':'kolkata'
    }
    response=requests.post(base_url+endpoint,data=json.dumps(new_std))
    print(response.status_code)
    print(response.json())
# create_resource()

def update_resource(id):
    new_data={
    'id':id,
    'marks':80,
    'location':'chennai'
    }
    response=requests.put(base_url+endpoint,data=json.dumps(new_data))
    print(response.status_code)
    print(response.json())
# update_resource(4)

def delete_resource(id):
    data={
    'id':id,
    }
    response=requests.delete(base_url+endpoint,data=json.dumps(data))
    print(response.status_code)
    print(response.json())
# delete_resource(12)
