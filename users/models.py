from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
        USERNAME_FIELD = 'username'
        is_customer = models.BooleanField(default=False)
is_engineer = models.BooleanField(default=False)

def __str__(self):
        return self.username


    # Modify related_name to avoid conflicts
groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
