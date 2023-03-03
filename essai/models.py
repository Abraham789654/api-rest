from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model) :

     # standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now= True)


class profil(BaseModel):
    user = models.ForeignKey(User, related_name = 'profil', on_delete= models.CASCADE)
    dateNaissance = models.CharField(max_length=200)
    pp = models.ImageField(upload_to= 'image')
    document = models.FileField(upload_to='docs')


    def __str__(self) :
        return self.user
    

class Voyage (BaseModel):
    ticket = models.CharField(max_length= 200)
    depart = models.CharField(max_length= 250)
    arrive = models.CharField(max_length= 250)
    date_voyage = models.DateTimeField()
    prix_siege = models.CharField(max_length= 250)   




