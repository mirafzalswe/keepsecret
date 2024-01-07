from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User





class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    user_avatar = models.ImageField(upload_to='uploads/', default='default/defaultmale.png')
    phone_number = models.CharField(max_length=15, blank=True, validators=[
        RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    ])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return f"@{self.user.username}"