from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "Language",
                    "Preference",
                    "Favorite_Book_Genre",
                    "Favorite_Movie_Genre",
                )
            },
        ),
    )