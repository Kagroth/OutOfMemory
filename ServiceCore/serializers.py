from rest_framework import serializers
from ServiceCore.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    """
    A  profile serializer to return the user details
    """
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user', 'description',)

    def create(self, validated_data):
        
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user,
                            description=validated_data.pop('description'))
        return profile


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tagName', )

class PostPreviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = TagSerializer(many=True)
    commentsCount = serializers.SerializerMethodField('get_comment_count')

    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'viewsCount', 'tags', 'createdAt', 'commentsCount')

    def get_comment_count(self, postObj):
        return postObj.comments.all().count()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    rate = serializers.SerializerMethodField('calculate_rate')
    class Meta:
        model = Comment
        fields = ('pk', 'author', 'createdAt', 'commentField', 'rate')

    def calculate_rate(self, commentObj):
        pluses = commentObj.rates.filter(ratingValue=1).count()
        minuses = commentObj.rates.filter(ratingValue=-1).count()

        return pluses + minuses * (-1)

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'postField', 'viewsCount', 'tags', 'createdAt', 'comments')

class UserWholeDataSerializer(serializers.ModelSerializer):
    posts = PostPreviewSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'posts', 'comments')

class ProfileSerializerExtended(serializers.ModelSerializer):
    """
    A  profile serializer to return the user details
    """
    user = UserWholeDataSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user', 'description',)
