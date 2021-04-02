from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from database.extract import Extract
from database.transform import Transform
from database.load import Load
from database.manage import DBManage

@login_required
def etl(request):
    return render(request, 'database/etl.html')

@login_required
def etl_extract(request):
    extract = Extract()
    message = extract.extract()
    return render(request, 'database/etl.html', {'message_extract': message})

@login_required
def etl_transform(request):
    transform = Transform()
    message = transform.transform_basic()
    return render(request, 'database/etl.html', {'message_transform': message})

@login_required
def etl_load(request):
    loading = Load()
    message = loading.load_data()
    return render(request, 'database/etl.html', {'message_load': message})

def etl_manage_nutriscore(request):
    managing = DBManage()
    message = managing.load_nutriscore()
    return render(request, 'database/etl.html', {'message_manage_nutriscore': message})

@login_required
def etl_manage_delete(request):
    managing = DBManage()
    message = managing.delete_tables()
    return render(request, 'database/etl.html', {'message_manage_delete': message})