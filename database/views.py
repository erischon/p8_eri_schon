from django.shortcuts import render
from database.load import Load

def etl(request):
    loading = Load()
    message = loading.load_nutriscore()
    return render(request, 'database/etl.html', {'message': message})
