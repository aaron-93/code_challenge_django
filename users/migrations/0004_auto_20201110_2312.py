# Generated by Django 3.1.3 on 2020-11-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201110_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='Favorite_Book_Genre',
            field=models.CharField(blank=True, choices=[('문학/Literature', '문학/Literature'), ('인문/Humanities', '인문/Humanities'), ('사회/Society', '사회/Society'), ('비즈니스/Business', '비즈니스/Business'), ('과학/Science', '과학/Science'), ('예술/Art', '예술/Art'), ('기타/Etc', '기타/Etc')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Favorite_Movie_Genre',
            field=models.CharField(blank=True, choices=[('액션/Action', '액션/Action'), ('드라마/Drama', '드라마/Drama'), ('스릴러/Thriller', '스릴러/Thriller'), ('공상과학/Sci-Fi', '공상과학/Sci-Fi'), ('판타지/Fantasy', '판타지/Fantasy'), ('느와르/Noir', '느와르/Noir'), ('기타/Etc', '기타/Etc')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Language',
            field=models.CharField(blank=True, choices=[('korean', 'Korean'), ('english', 'English')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Preference',
            field=models.CharField(blank=True, choices=[('Books', 'Books'), ('Movies', 'Movies')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
    ]
