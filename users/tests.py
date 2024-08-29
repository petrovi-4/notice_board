import pytest
from django.contrib.auth import get_user_model

# Получаем модель пользователя
User = get_user_model()


@pytest.mark.django_db
class TestUserManager:
    def test_create_user(self):
        # Тестирование создания обычного пользователя
        # Создаём пользователя с корректным email и паролем
        user = User.objects.create_user(email='testuser@example.com', password='testpassword123')

        # Проверяем, что пользователь был создан
        assert user.email == 'testuser@example.com'
        assert user.check_password('testpassword123')  # Проверяем пароль
        assert user.is_superuser is False  # Проверяем, что пользователь не является суперпользователем
        assert user.is_staff is False  # Проверяем, что пользователь не является администратором

    def test_create_user_without_email(self):
        # Тестирование создания пользователя без email

        with pytest.raises(ValueError, match='Email must be provided'):
            User.objects.create_user(email='', password='testpassword123')

    def test_create_superuser_without_is_staff(self):
        # Тестируем создание суперпользователя без флага is_staff

        with pytest.raises(ValueError, match='Superuser must have is_staff=True'):
            User.objects.create_superuser(email='superuser@example.com', password='superpassword123', is_staff=False)

    def test_create_superuser_without_is_superuser(self):
        # Тестируем создание суперпользователя без флага is_superuser

        with pytest.raises(ValueError, match='Superuser must have is_superuser=True'):
            User.objects.create_superuser(email='superuser@example.com', password='superpassword123', is_superuser=False)
