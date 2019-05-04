from django.db import models
from django.contrib.auth.models import User

#test imports
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

# klasa Profile polaczona 1 do 1 z klasa User 
# aby rozszerzyc informacje dotyczace uzytkownika
# Pola Username, password i email z klasy User sa required
# pola first_name, last_name domyslnie nie sa required - ale sa wymagane przez nasz ERD
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(name='description', max_length=500)

# Klasa CV reprezentujaca CV usera
class CV(models.Model):
    cvID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=1000)
    experience = models.CharField(max_length=1000)

# Oferta pracy
class JobOffer(models.Model):
    jobOfferID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    salaryMin = models.IntegerField()
    salaryMax = models.IntegerField()
    description = models.CharField(max_length=2048)
    requirements = models.CharField(max_length=2048)

# Klasa przechowuje info jaki uzytkownik zaaplikowal na jakie stanowisko
class Application(models.Model):
    applicationID = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)

class Tag(models.Model):
    tagID = models.AutoField(primary_key=True)
    tagName = models.CharField(max_length=32)

class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    postField = models.CharField(max_length=2048)
    tags = models.ManyToManyField(Tag)
    viewsCount = models.IntegerField() # liczba wyswietlen
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    commentField = models.CharField(max_length=2048)    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

# Klasa trzymajaca info czy dany uzytkownik ocenil dany komentarz
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    ratingValue = models.BooleanField(default=True)

#serializers test ==========================================================================================================================

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
