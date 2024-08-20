from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Кастомный менеджер для модели пользователя, где email
    используется как уникальный идентификатор.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет обычного пользователя
        с переданным email и паролем.
        Args:
            email: str, обязательный аргумент, содержащий email пользователя
            password: str, обязательный аргумент, содержащий пароль пользователя
            extra_fields: dict, необязательный аргумент, содержащий дополнительные поля
        Returns:
            user: Созданный пользователь
        Raises:
            ValueError: Если email не указан.
        """
        if not email:
            raise ValueError(_('Email must be provided'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создает и сохраняет суперпользователя
        с переданным email и паролем.
        Args:
            email: str, обязательный аргумент, содержащий email суперпользователя
            password: str, обязательный аргумент, содержащий пароль суперпользователя
            extra_fields: dict, необязательный аргумент, содержащий дополнительные поля
        Returns:
            user: Созданный суперпользователь
        Raises:
            ValueError: Если 'is_staff' или 'is_superuser' не равны True.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
