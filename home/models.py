from django.db import models


# Create your models here.

class user_contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    sno=models.AutoField(primary_key=True)
    

    def __str__(self):
        return "New contact from "+self.name+","+self.phone

