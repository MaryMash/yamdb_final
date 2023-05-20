from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self,
                    username,
                    email,
                    bio,
                    role,
                    password=None):
        if not username:
            raise ValueError(("The Username must be set"))
        if not email:
            raise ValueError(("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          bio=bio,
                          role=role)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,
                         username,
                         email,
                         password,
                         bio,
                         role):
        if password is None:
            raise ValueError('Password must be set')

        user = self.create_user(username=username,
                                email=email,
                                password=password,
                                bio=bio,
                                role=role)
        user.role = 'admin'
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    ROLES = [
        ('user', 'user'),
        ('admin', 'admin'),
        ('moderator', 'moderator'),
    ]

    email = models.EmailField(
        max_length=254,
        verbose_name='email',
        unique=True
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
    )
    role = models.TextField(
        verbose_name='Роль',
        choices=ROLES,
        default='user'
    )
    password = models.CharField(
        max_length=150,
        blank=True
    )

    REQUIRED_FIELDS = ['email', 'bio', 'role']

    objects = UserManager()

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    class Meta:
        ordering = ['id']
