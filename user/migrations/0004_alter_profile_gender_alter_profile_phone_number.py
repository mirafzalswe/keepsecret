# Generated by Django 5.0.1 on 2024-01-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
    ]
