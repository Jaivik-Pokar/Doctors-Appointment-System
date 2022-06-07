from django.db import models

# Create your models here
# makemigration - create changes and store in a file
# migrate - apply the pending changes created by makemigration
class Contact(models.Model):
    message_name=models.TextField()
    message_email=models.EmailField()
    message=models.TextField()
    # dateANDtiME= models.DateTimeField()
    
    def __str__(self):
        return self.message_name
    
class Bookapp(models.Model):
    name=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    schedule=models.TextField()
    experts=models.TextField()
    message=models.TextField()
    
    def __str__(self):
        return self.name