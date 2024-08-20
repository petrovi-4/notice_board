from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class UserRoles(models.TextChoices):
    """
    Перечисление возможных ролей пользователя.
    """
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class User(AbstractUser):
    """
    Кастомная модель пользователя,
    где email используется как уникальный
    идентификатор для аутентификации.
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices,
                            default=UserRoles.USER, verbose_name='Роль',
                            help_text='Роль пользователя в системе')
    image = models.ImageField(
        upload_to='users/',
        null=True,
        blank=True,
        verbose_name='Аватар',
        help_text='Аватар пользователя'
    )
    phone = models.CharField(
        max_length=35,
        verbose_name='Телефон',
        blank=True,
        null=True,
        help_text='Номер телефона пользователя'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    def __str__(self):
        """
        Возвращает email пользователя
        как строковое представление объекта.
        """
        return self.email
