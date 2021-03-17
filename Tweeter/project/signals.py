from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# Upon new registration, create a profile for the user to be saved
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwarges):
    if created:
        Profile.objects.create(user=instance)


# Save the new profile to the database
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwarges):
    instance.profile.save()