from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import UserProfile


# When user signs up; creates an entry in UserProfile model
@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    UserProfile.objects.create(user=user)