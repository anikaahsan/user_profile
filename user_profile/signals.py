from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Account
from .models import Profile


@receiver(post_save,sender=Account)
def create_profile(sender,instance,created,**kwargs):
    if created:
        user=Profile.objects.create(user=instance)
        user.save()





