from rest_framework import serializers

from notice_board.models import Ad, Comment


class AdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Ad, представляющий краткую информацию о товаре.
    """
    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description',)


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детального представления объявления с дополнительной информацией об авторе.
    """
    author_first_name = serializers.CharField(
        read_only=True,
        source='author.first_name'
    )
    author_last_name = serializers.CharField(
        read_only=True,
        source='author.last_name'
    )
    phone = serializers.CharField(
        read_only=True,
        source='author.phone'
    )

    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'phone', 'description',
                  'author_first_name', 'author_last_name', 'author_id',)


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(
        read_only=True,
        source='author.first_name'
    )
    author_last_name = serializers.CharField(
        read_only=True,
        source='author.last_name'
    )
    author_image = serializers.ImageField(
        read_only=True,
        source='author.avatar',
        allow_null=True
    )

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'author_id', 'created_at', 'author_first_name',
                  'author_last_name', 'ad_id', 'author_image',)
