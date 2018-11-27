from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv,io
from django.contrib import messages
from .models import Shiftrotainfo
from django.core.exceptions import ValidationError
from shiftrota.forms import HomeForm

def home(request):
    return render(request,'shiftrota/home.html')

def upload_rota(request):
    template = 'shiftrota/rota_upload.html'
    prompt = {
        'order':'Uploder only CSV format file and data must be name and followed by week shift details.'
    }
    if request.method == "GET":
        return render(request,template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        return HttpResponse("<br><h3>The file should be CSV only</h3>")

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    csv_data={}
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        csv_data["first_name"]=column[0]
        csv_data["last_name"]=column[1]
        csv_data["whichShift"]=column[2]

        _,created = Shiftrotainfo.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            whichShift=column[2]
        )
    print(csv_data)
    return render(request, 'shiftrota/preview.html', csv_data)

def plan_new_v(request):
    if request.method == "POST":
        form = HomeForm(request.POST) 
        print("form :%s" %form)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('plan_new_v')  
    else:    
        form = HomeForm()

    args = {'form':form}    
    return render(request,'shiftrota/plan.html',args)