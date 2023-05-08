from django.db import models
from django_countries.fields import CountryField
from account.models import Account


# Create your models here.
class Profile(models.Model):
    gender_choices=[
        ('male','male'),
        ('female','female')
    ]
    image=models.ImageField(upload_to='uploads')
    birthday=models.DateField()
    country=CountryField()
    gender=models.CharField(max_length=255 ,
                            choices=gender_choices)
    bio=models.TextField()
    user=models.OneToOneField(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username