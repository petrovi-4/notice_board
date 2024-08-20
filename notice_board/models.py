from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name='название товара')
    price = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='цена товара'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание товара'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='владелец',
        related_name='advertisement',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    image = models.ImageField(
        upload_to='ads/',
        null=True,
        blank=True,
        verbose_name='изображение'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'


class Comment(models.Model):
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='владелец',
        related_name='comments',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        verbose_name='объявление',
        related_name='comments',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

