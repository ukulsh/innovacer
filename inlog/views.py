
from django.shortcuts import render, redirect
from inlog.models import Visitor
from .models import Visitor

def contact_view(request):
    # print(request.method)
    if request.method == "POST":
        visitor = Visitor()
        visitor.name = request.POST.get("name")
        visitor.email= request.POST.get("email")
        visitor.host = request.POST.get("message")
        visitor.save()
        # print(visitor.name,visitor.email,visitor.host,file=sys.stderr)
        return render(request,"index.html")
    else:
        return render(request,"index.html")


def home(request):
    return render(request, "other.html",{})

def chick(request):
    return render(request, "datab.html",{})




def showthis(request):

    all_objects= Visitor.objects.all()
    
    context= {'all_objects': all_objects}
        
    return render(request, 'other.html', context)

