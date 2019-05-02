from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    firstname = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    lastname = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['firstname'],
                                        validated_data['lastname'], validated_data['email'],
                                        validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'firstname', 'lastname', 'email', 'password', 'description')
