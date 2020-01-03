
from django.shortcuts import render, redirect
from inlog.models import Visitor
from .models import Visitor
from smtplib import SMTP
from twilio.rest import Client

def contact_view(request):
    # print(request.method)
    if request.method == "POST":
        visitor = Visitor()
        visitor.name = request.POST.get("name")
        visitor.email= request.POST.get("email")
        visitor.host = request.POST.get("message")
        visitor.save()
        name = visitor.name
        email = visitor.email
        host = visitor.host
        inTime = visitor.inTime
        
        content = '\nVisitor Details: \n'
        content += 'Name: '+str(name)+'\n'
        content += 'Email: '+str(email)+'\n'
        content += 'Host: '+str(host)+ '\n'
        content += 'Checkin Time: '+str(inTime)+'\n'
        
        mail = SMTP('smtp.gmail.com',587)
        mail.ehlo()

        # email = input("Enter a valid email to send mails from:")
        # password = input("Enter password:")

        mail.starttls()
        mail.login('dustingdown@gmail.com','Utkarsh1@')
        mail.sendmail('dustingdown@gmail.com',email,content)

        mail.close()


        # Download the helper library from https://www.twilio.com/docs/python/install



        # Your Account Sid and Auth Token from twilio.com/console
        # DANGER! This is insecure. See http://twil.io/secure
        # account_sid = 'AC458a3cd4e8904129335ecfb9af035468'
        # auth_token = '95b008f46f1950d1369ce5e28c396406'
        # client = Client(account_sid, auth_token)

        # message = client.messages \
        #                 .create(
        #                     body=content,
        #                     from_='+19564357088',
        #                     to='+916350041405'
        #                 )
        # client.sendMessage()
        # print(message.sid)


        # print(visitor.name,visitor.email,visitor.host)
        return render(request,"home.html")
        
    else:
        return render(request,"home.html")

def contact_view2(request):
    # print(request.method)
    if request.method == "POST":
        
        n = request.POST.get("name")
        details = Visitor.objects.get(name=n)
        print(details)
        mail = SMTP('smtp.gmail.com',587)
        mail.ehlo()
        
        # email = input("Enter a valid email to send mails from:")
        # password = input("Enter password:")

        name = details.name
        email = details.email
        host = details.host
        inTime = details.inTime

        content = '\nVisitor Details: \n'
        content += 'Name: '+str(name)+'\n'
        content += 'Email: '+str(email)+'\n'
        content += 'Host: '+str(host)+ '\n'
        content += 'Checkin Time: '+str(inTime)+'\n'
        

        mail.starttls()
        mail.login('dustingdown@gmail.com','Utkarsh1@')
        mail.sendmail('dustingdown@gmail.com',email,content)

        mail.close()
        Visitor.objects.get(name=n).delete()
        # print(visitor.name,visitor.email,visitor.host,file=sys.stderr)
        return render(request,"home.html")
    else:
        return render(request,"home.html")


def index_call(request):
    return render(request, "index.html")

def index2_call(request):
    return render(request, "index2.html")

def home(request):
    return render(request, "home.html")





def showthis(request):

    all_objects= Visitor.objects.all()
    
    context= {'all_objects': all_objects}
        
    return render(request, 'other.html', context)

