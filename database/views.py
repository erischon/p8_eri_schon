from django.shortcuts import render

from database.extract import Extract
from database.transform import Transform
from database.load import Load

def etl(request):
    return render(request, 'database/etl.html')

def etl_extract(request):
    extract = Extract()
    message = extract.extract()
    return render(request, 'database/etl.html', {'message_extract': message})

def etl_transform(request):
    transform = Transform()
    message = transform.transform_basic()
    return render(request, 'database/etl.html', {'message_transform': message})

def etl_load(request):
    loading = Load()
    # message = loading.load_nutriscore()
    message = loading.load_data()
    return render(request, 'database/etl.html', {'message_load': message})

