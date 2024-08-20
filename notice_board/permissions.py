from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsAuthor(BasePermission):
    """
    Класс разрешений, проверяющий, является ли текущий пользователь автором объекта.
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверяет, является ли пользователь автором объекта.

        Args:
            request: Текущий запрос.
            view: Представление, из которого был сделан запрос.
            obj: Объект, к которому пытается получить доступ пользователь.

        Returns:
            bool: True, если пользователь является автором объекта, иначе False.
        """
        if request.user == obj.author:
            return True
        return False


class IsAdmin(BasePermission):
    """
    Класс разрешений, проверяющий, является ли текущий пользователь администратором.
    """

    def has_permission(self, request, view):
        """
        Проверяет, имеет ли пользователь административные права.

        Args:
            request: Текущий запрос.
            view: Представление, из которого был сделан запрос.

        Returns:
            bool: True, если пользователь имеет роль администратора, иначе False.
        """
        if request.user.role == UserRoles.ADMIN:
            return True
        return False
