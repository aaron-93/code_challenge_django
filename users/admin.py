from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = (
        "username",
        "Language",
        "Preference",
        "Favorite_Book_Genre",
        "Favorite_Movie_Genre",
    )
