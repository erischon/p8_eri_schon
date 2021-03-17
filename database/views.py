from django.shortcuts import render
from database.load import Load

def etl(request):
    loading = Load()
    # message = loading.load_nutriscore()
    message = loading.load_data()
    return render(request, 'database/etl.html', {'message': message})
