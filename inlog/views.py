
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
        return render(request,"index2.html")

def contact_view2(request):
    # print(request.method)
    if request.method == "POST":
        
        n = request.POST.get("name")
        Visitor.objects.get(name=n).delete()
        # print(visitor.name,visitor.email,visitor.host,file=sys.stderr)
        return render(request,"home.html")
    else:
        return render(request,"home.html")



def home(request):
    return render(request, "home.html")

def chick(request):
    
    all_objects= Visitor.objects.all()
    
    context = {
            'all_objects': all_objects
        }
    print(context)    
    return render(request,'datab.html',context)
    # return render(request, "datab.html")




def showthis(request):

    all_objects= Visitor.objects.all()
    
    context= {'all_objects': all_objects}
        
    return render(request, 'other.html', context)

