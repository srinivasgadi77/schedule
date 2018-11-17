from django.shortcuts import render
from django.http import HttpResponse
import csv,io
from django.contrib import messages
from .models import Shiftrotainfo

def home(request):
    return HttpResponse('<h1>Shift Rota</h1>')

def upload_rota(request):
    template = "shiftrota/rota_upload.html"
    prompt = {
        'order':'order of the CSV name followed by week shift details'
    }
    if request.method == "GET":
        return render(request,template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
       messages.error(request,'This is not a CSV file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _,created = Shiftrotainfo.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            whichShift=column[2]

        )
    context ={}
    return render(request, template, context)
