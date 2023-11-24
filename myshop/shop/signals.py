from django.db.models.signals import post_save, pre_save
from .models import Review
from django.dispatch import receiver


@receiver(pre_save, sender= Review)
def create_review_user_full_email(sender, instance, **kwargs):
    if not instance.user_name or not instance.user_email:
        instance.user_name= instance.user.get_full_name()
        instance.user_email= instance.user.email
