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
    LANGUAGE_KR = "한국어"
    LANGUAGE_EN = "english"
    LANGUAGE_CHOICES = ((LANGUAGE_KR, "한국어"), (LANGUAGE_EN, "English"))

    # Favourite Book Genre
    BOOK_LIT = "문학/Literature"
    BOOK_HUM = "인문/Humanities"
    BOOK_SOC = "사회/Society"
    BOOK_BIS = "비즈니스/Business"
    BOOK_SCI = "과학/Science"
    BOOK_ART = "예술/Art"
    BOOK_ETC = "기타/Etc"

    BOOK_CHOICES = (
        (BOOK_LIT, "문학/Literature"),
        (BOOK_HUM, "인문/Humanities"),
        (BOOK_SOC, "사회/Society"),
        (BOOK_BIS, "비즈니스/Business"),
        (BOOK_SCI, "과학/Science"),
        (BOOK_ART, "예술/Art"),
        (BOOK_ETC, "기타/Etc"),
    )

    # Favourite Movie Genre
    MOVIE_ACT = "액션/Action"
    MOVIE_DRA = "드라마/Drama"
    MOVIE_THR = "스릴러/Thriller"
    MOVIE_SCI = "공상과학/Sci-Fi"
    MOVIE_FNT = "판타지/Fantasy"
    MOVIE_NOR = "느와르/Noir"
    MOVIE_ETC = "기타/Etc"

    MOVIE_CHOICES = (
        (MOVIE_ACT, "액션/Action"),
        (MOVIE_DRA, "드라마/Drama"),
        (MOVIE_THR, "스릴러/Thriller"),
        (MOVIE_SCI, "공상과학/Sci-Fi"),
        (MOVIE_FNT, "판타지/Fantasy"),
        (MOVIE_NOR, "느와르/Noir"),
        (MOVIE_ETC, "기타/Etc"),
    )
    bio = models.TextField(default="", blank=True)
    Language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True
    )
    Preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=10, null=True, blank=True
    )
    Favorite_Book_Genre = models.CharField(
        choices=BOOK_CHOICES, max_length=20, null=True, blank=True
    )
    Favorite_Movie_Genre = models.CharField(
        choices=MOVIE_CHOICES, max_length=20, null=True, blank=True
    )
