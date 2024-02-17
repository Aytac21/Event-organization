from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from phonenumber_field.formfields import PhoneNumberField
from django.utils import timezone
import datetime

from django.db import models

USER_TYPE = (
    ("eventuser", "eventuser"),
    ("organizer", "organizer")
)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone = PhoneNumberField()
    user_type = models.CharField(max_length=12, choices=USER_TYPE)

    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.first_name

    @property
    def is_eventuser(self):
        return self.user_type == "eventuser"

    @property
    def is_organizer(self):
        return self.user_type == "organizer"


class EventUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='eventuser')

    def __str__(self):
        return self.user.first_name
    def save(self, *args, **kwargs):
        self.user.is_eventuser = True
        self.user.save()
        super(EventUser, self).save(*args, **kwargs)



class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='organizer')

    def __str__(self):
        return self.user.first_name
    def save(self, *args, **kwargs):
        self.user.is_parent = True
        self.user.save()
        super(Organizer, self).save(*args, **kwargs)