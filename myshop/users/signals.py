from django.db.models.signals import post_save
from .models import CustomProfile, CustomUser
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CustomProfile.objects.create(user= instance)
