from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ Custom User Model """

    # Preference selection
    PREFERENCE_BOOK = "Books"
    PREFERENCE_MOVIE = "Movies"
    PREFERENCE_CHOICES = ((PREFERENCE_BOOK, "Books"), (PREFERENCE_MOVIE, "Movies"))

    # Language selection
    LANGUAGE_KR = "korean"
    LANGUAGE_EN = "english"
    LANGUAGE_CHOICES = ((LANGUAGE_KR, "Korean"), (LANGUAGE_EN, "English"))

    avatar = models.ImageField(null=True, blank=True)
    Preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)