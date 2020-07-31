from django.shortcuts import render,HttpResponse
from home.models import Contact 
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    #return HttpResponse("Home page")
    contex = {
        'variable1' : 'Dev' ,
        'variable2': 'Vora'
    }
    messages.success(request,'success msg')
    return render(request,'index.html',contex)

def about(request):
    return render(request,'aboutus.html')

def services(request):
    return render(request,"service.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        cno = request.POST.get('cno')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,cno=cno,desc=desc,date= datetime.today())
        contact.save()
        messages.success(request,"Message sended successfully!")
    return render(request,"contact.html")