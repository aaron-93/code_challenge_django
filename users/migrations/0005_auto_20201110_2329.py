# Generated by Django 3.1.3 on 2020-11-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201110_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Language',
            field=models.CharField(blank=True, choices=[('한국어', '한국어'), ('english', 'English')], max_length=10, null=True),
        ),
    ]