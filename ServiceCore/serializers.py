from rest_framework import serializers
from ServiceCore.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.db.models.query import QuerySet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tagName',)


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

        return pluses - minuses


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('pk', 'author', 'title', 'postField', 'viewsCount', 'tags', 'createdAt', 'comments')


class JobOffersSerializer(serializers.ModelSerializer):
    """
    A Job offer serializer to return all fields
    """
    user = serializers.StringRelatedField()
    numberOfApplications = serializers.SerializerMethodField('getNumberOfApplications')

    class Meta:
        model = JobOffer
        fields = ('pk', 'viewsCount', 'user', 'title', 'salaryMin', 'salaryMax', 'description', 'requirements', 'numberOfApplications','companyName', 'companyLocation', 'createdAt')

    def getNumberOfApplications(self, offer):
        return offer.applications.all().count()

class ApplicationSerializer(serializers.ModelSerializer):
    job = JobOffersSerializer()
    class Meta:
        model = Application
        fields = ('pk', 'job')

class CVRawSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = CV
        fields = ('user', 'skills', 'experience')

class ApplicationCVSerializer(serializers.ModelSerializer):
    cv = CVRawSerializer()
    class Meta:
        model = Application
        fields = ('pk', 'cv')

class JobOfferWithApplicationsSerializer(serializers.ModelSerializer):
    applications = ApplicationCVSerializer(many=True)
    class Meta:
        model = JobOffer
        fields = ('pk', 'viewsCount', 'user', 'title', 'salaryMin', 'salaryMax', 'description', 'requirements', 'companyName', 'companyLocation', 'createdAt', 'applications')


class CVSerializer(serializers.ModelSerializer):
    appliedFor = ApplicationSerializer(many=True)
    class Meta:
        model = CV
        fields = ('user', 'skills', 'experience', 'appliedFor')

class UserViewSerializer(serializers.ModelSerializer):
    posts = PostPreviewSerializer(many=True)
    comments = CommentSerializer(many=True)
    jobOffers = JobOffersSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'posts', 'comments', 'jobOffers')

class UserWholeDataSerializer(serializers.ModelSerializer):
    posts = PostPreviewSerializer(many=True)
    comments = CommentSerializer(many=True)
    cv = CVSerializer()
    jobOffers = JobOffersSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'posts', 'comments', 'cv', 'jobOffers')

class ProfileSerializer(serializers.ModelSerializer):
    """
    A  profile serializer to return the user details
    """
    user = UserViewSerializer(required=True)
    # https://www.youtube.com/watch?v=sD-Bi9QyoH0
    avatar = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Profile
        fields = ('user', 'description', 'avatar')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user,
                                                            description=validated_data.pop('description'))
        return profile

class ProfileSerializerExtended(serializers.ModelSerializer):
    """
    A  profile serializer to return the user details
    """
    user = UserWholeDataSerializer(required=True)
    # https://www.youtube.com/watch?v=sD-Bi9QyoH0
    avatar = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Profile
        fields = ('user', 'description', 'avatar')



