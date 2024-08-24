from django.contrib import admin

from notice_board.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели Ad.

    Этот класс определяет, как объявления будут отображаться в административной панели Django.
    В списке отображаются следующие поля:
    идентификатор (pk), название (title), цена (price), автор (author) и дата создания (created_at).
    """
    list_display = ('pk', 'title', 'price', 'author', 'created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели Comment.

    Этот класс определяет, как комментарии будут отображаться в административной панели Django.
    В списке отображаются следующие поля:
    идентификатор (pk), текст комментария (text), дата создания (created_at),
    связанное объявление (ad) и автор комментария (author).
    """
    list_display = ('pk', 'text', 'created_at', 'ad', 'author', )
