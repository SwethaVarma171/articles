from django.shortcuts import render
from .models import Articles
def index(request):
    data=Articles.objects.all()
    context={
        'data':data
    }
    return render(request,'index.html',context)

def details(request,pk):
    data1=Articles.objects.get(id=pk)
    context={
        'data1':data1
                }
    return render(request,'single_details.html',context)

