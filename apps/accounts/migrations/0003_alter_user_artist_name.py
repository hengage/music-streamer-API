# Generated by Django 3.2.6 on 2021-10-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='artist_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
