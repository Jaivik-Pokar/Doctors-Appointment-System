from django.contrib import admin
from website.models import Contact
from website.models import Bookapp
from django.contrib import admin

admin.site.register(Contact)
admin.site.register(Bookapp)


# admin.site.unregister(Contact)