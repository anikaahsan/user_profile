from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,AbstractUser
from django.utils import timezone

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('user need to have a email address')
        if not username:
            raise ValueError('user need to have a username')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password):
        user=self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            username=username,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superadmin=True
        user.is_active=True
        user.save()
        return user







class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)



    date_joined=models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(default=timezone.now)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superadmin=models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username']

    objects=AccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True
    

    

