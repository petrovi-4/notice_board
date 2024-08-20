from django.db import models

from users.models import User


class Ad(models.Model):
    """
    Модель, представляющая объявления.
    """
    title = models.CharField(
        max_length=200,
        verbose_name='название товара',
        help_text= 'Заголовок объявления'
    )
    price = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='цена товара',
        help_text='Стоимость товара'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание товара',
        help_text='Подробное описание товара'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='владелец',
        related_name='advertisement',
        null=True,
        blank=True,
        help_text='Пользователь разместивший объявление'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания',
        help_text='Дата и время создания объявления'
    )
    image = models.ImageField(
        upload_to='ads/',
        null=True,
        blank=True,
        verbose_name='изображение'
    )

    def __str__(self):
        """
        Возвращает заголовок объявления как строковое представление объекта.
        """
        return self.title

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'


class Comment(models.Model):
    """
    Модель, представляющая комментарии к объявлению.
    """
    text = models.TextField(verbose_name='текст', help_text='Текст комментария')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='владелец',
        related_name='comments',
        null=True,
        blank=True,
        help_text='Пользователь, оставивший комментарий'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания',
        help_text='Дата и время создания комментария'
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        verbose_name='объявление',
        related_name='comments',
        null=True,
        blank=True,
        help_text='Объявление, к которому относится комментарий'
    )

    def __str__(self):
        """
        Возвращает текст комментария как строковое представление объекта.
        """
        return self.text

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
