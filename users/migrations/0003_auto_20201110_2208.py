# Generated by Django 3.1.3 on 2020-11-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Preference',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
