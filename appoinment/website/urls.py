from django.urls import path
from . import views
from django.core.mail import send_mail
from django.conf import settings

urlpatterns = [
    path('', views.Home, name="Home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('pricing.html', views.pricing, name="pricing"),
    path('blog.html', views.blog, name="blog"),
    path('blogdetails.html', views.blogdetails, name="blogdetails"),
    path('bookapp',views.bookapp,name="bookapp"),
    path('send_mail/',send_mail,name="send_mail")


]
