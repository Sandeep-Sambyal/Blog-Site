from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class blogpost(models.Model):
    id=models.AutoField(primary_key=True)
    author=models.CharField(max_length=70)
    title=models.CharField(max_length=500)
    views=models.IntegerField(default=0)
    desc=models.TextField()
    pub_date=models.DateField()
    slug=models.CharField(max_length=130)



class Blogcomment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(blogpost,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(default=now)

    # def __str__(self):
    #     return "Comment No: "+str(self.sno)+" Post: "+str(self.post)
    