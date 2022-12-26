from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    form=TopicForm()
    d={'form':form}

    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()

            return HttpResponse('topic moddel from is created by using Modelform')


    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    form=WebpadeForm()
    d={'form':form}
    if request.method=='POST':
        form_data=WebpadeForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('webpage moddel from is created by using Modelform')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    form=AccessRecordsForm()
    d={'form':form}
    if request.method=='POST':
        form_data=AccessRecordsForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('AccessRecords moddel from is created by using Modelform')
    return render(request,'insert_access.html',d)