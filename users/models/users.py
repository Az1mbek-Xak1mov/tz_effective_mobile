from django.contrib.auth.models import AbstractUser
from django.db.models import  TextChoices
from django.db.models.fields import EmailField

from users.models import UUIDBaseModel, CustomUserManager


class User(AbstractUser, UUIDBaseModel):
    username = None
    email = EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    @property
    def fullname(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
