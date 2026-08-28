from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager


class User(AbstractUser):
    # Override email to make it unique (required for email login)
    email = models.EmailField(unique=True)

    # Add your custom fields here
    phone = models.CharField(max_length=20, blank=True)

    objects = CustomUserManager()

    # Use email for login instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Fields prompted during createsuperuser

    class Meta:
        db_table = 'users'  # Cleaner table name than 'accounts_user'

    def __str__(self):
        return self.email
