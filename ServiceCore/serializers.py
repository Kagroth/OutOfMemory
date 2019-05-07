from rest_framework import serializers, status
from ServiceCore.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from ServiceCore.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

#class SnippetSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#    code = serializers.CharField(style={'base_template': 'textarea.html'})
#    linenos = serializers.BooleanField(required=False)
#    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#    def create(self, validated_data):
#        """
#        Create and return a new `Snippet` instance, given the validated data.
#        """
#        return Snippet.objects.create(**validated_data)

#    def update(self, instance, validated_data):
#        """
#        Update and return an existing `Snippet` instance, given the validated data.
#        """
#        instance.title = validated_data.get('title', instance.title)
#        instance.code = validated_data.get('code', instance.code)
#        instance.linenos = validated_data.get('linenos', instance.linenos)
#        instance.language = validated_data.get('language', instance.language)
#        instance.style = validated_data.get('style', instance.style)
#        instance.save()
#        return instance

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


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
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

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


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = ('author', 'title', 'postField', 'viewsCount', 'tags', 'createdAt', 'comments')
