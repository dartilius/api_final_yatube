from django.shortcuts import get_object_or_404
from rest_framework import serializers
from posts.models import Comment, Post, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    author = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group')
        read_only_fields = ('author',)
        model = Post

    def get_author(self, obj):
        """Метод для получения имени автора."""
        return obj.author.username


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')
        model = Comment

    def get_author(self, obj):
        """Метод для получения имени автора."""
        return obj.author.username


class FollowSerializer(serializers.ModelSerializer):
    """Сериалайзер для подписок."""

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        read_only=False
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Нельзя подписаться дважды!'
            ),
        )

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError('Нельзя подписаться на себя!')
        return attrs

    def create(self, validated_data):
        user = User.objects.get(username=validated_data['user'])
        following = get_object_or_404(
            User,
            username=validated_data['following']
        )
        follow = Follow.objects.create(user=user, following=following)
        return follow
