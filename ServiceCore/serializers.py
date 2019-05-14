from rest_framework import serializers
from ServiceCore.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    '''
    first_name = serializers.CharField(
        required=True,
    )
    last_name = serializers.CharField(
        required=True,
    )

    username = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        style={'input_type': 'password'},
        min_length=8
    )
    '''

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

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = TagSerializer(many=True)
    comments = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Post
        fields = ('author', 'title', 'postField', 'viewsCount', 'tags', 'createdAt', 'comments')
