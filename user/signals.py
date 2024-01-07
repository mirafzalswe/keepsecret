from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
from django.db.models import signals

@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance).save()


@receiver(signals.post_save, sender=Profile)
def set_default_avatar(sender, instance, created, **kwargs):
    if created:
        if instance.gender == 'Male':
            instance.user_avatar = 'default/defaultmale.png'
        elif instance.gender == 'Female':
            instance.user_avatar = 'default/defaultfemale.png'
        instance.save()