from django.db import models
from django_countries.fields import CountryField
from account.models import Account


# Create your models here.
class Profile(models.Model):
    gender_choices=[
        ('male','male'),
        ('female','female')
    ]
    image=models.ImageField(upload_to='uploads',null=True,
                            blank=True)
    birthday=models.DateField(null=True,
                              blank=True)
    country=CountryField(null=True,
                         blank=True)
    gender=models.CharField(max_length=255 ,
                            choices=gender_choices,
                            null=True,
                            blank=True)
    bio=models.TextField(null=True,
                         blank=True)
    phone_number=models.CharField(max_length=11,
                                  null=True,
                                  blank=True)
    user=models.OneToOneField(Account,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username