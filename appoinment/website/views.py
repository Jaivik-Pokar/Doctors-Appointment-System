from email import message
import email
from email.headerregistry import Address
from http.client import HTTPResponse
from django.shortcuts import render
from django.core.mail import send_mail
from datetime import datetime
from django.utils import timezone
#from appoinment.appoinment.settings import EMAIL_HOST_USER
#from appoinment.website.models import Contact
from django.core.mail import EmailMessage
from website.models import Contact
from website.models import Bookapp
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
#import pywhatkit as kit
#from django.http import httpResponseRedirect
from django.http import HttpResponseRedirect

#from django.http import HTTPResponseRedirect

# Create your views here.

def Home(request):
	return render(request, 'Home.html', {})


def bookapp(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        schedule = request.POST['scheldule']
        experts = request.POST['experts']
        message = request.POST['message']
        bookapp = Bookapp.objects.get_or_create(name = name,phone = phone,email = email,address = address,schedule = schedule,experts = experts,message = message)  
        print(name,phone,email,address,schedule,experts,message)
        
        
        send_mail(
            name,
            "Your Appointment has been Booked for Morning at 11AM to 12PM",
            'dr.appointment.system@gmail.com',
            [email],
            fail_silently=False,
            
        )
        messages.success(request,'Your Appointment has been Booked!')
        #return HttpResponseRedirect('Home')
        return render(request, 'Home.html', {})
        
        
    #else:
        #return HTTPResponse("Invalid request")
        
        
        
        

     
    

def contact(request):
    if request.method == "POST":
        name = request.POST['message_name']
        email = request.POST['message_email']
        message = request.POST['message']
        contact = Contact.objects.get_or_create(message_name = name,message_email= email, message = message)
        messages.success(request,'Your Message has been sent!')
        return render(request, 'contact.html',{'mytext':name})


    #messages.success(request, "This is a Test Message")        
    return render(request, 'contact.html')


def about(request):
	return render(request, 'about.html', {})


def service(request):
	return render(request, 'service.html', {})


def pricing(request):
	return render(request, 'pricing.html', {})


def blog(request):
	return render(request, 'blog.html', {})

def blogdetails(request):
	return render(request, 'blogdetails.html', {})