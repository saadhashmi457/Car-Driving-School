from django.shortcuts import render
from django.http import HttpResponse
from servicess.models import servicemodel
from contacts.models import contactsmodel

# Create your views here.


def signup_view(request):
    return render(request,"signup.html")
    # return HttpResponse('signuppppppppppppppppppp')

def login_view(request):
    # return HttpResponse('loginnnnnnnnnnnnnnnnnnnnnnnn')
    return render(request,"login.html")

def home_view(request):
    return render(request,"index.html")

def service_view(request):
    servicesdata=servicemodel.objects.all()
    
    if request.method=="GET":
        srch=request.GET.get('search')
        if srch!=None:
            servicesdata=servicemodel.objects.filter(Title__icontains=srch)
      
            
            
            
        
    
    data={
        'servicesdata': servicesdata
    }
    
    
    
    return render(request,"services.html",data)


def contacts_view(request):
    
    if request.method=="POST":
        value1=request.POST.get('name')
        value2=request.POST.get('email')
        value3=request.POST.get('message')
        vres=contactsmodel(Name=value1,Email=value2,Message=value3)
        vres.save()
        
    return render(request,"contacts.html")