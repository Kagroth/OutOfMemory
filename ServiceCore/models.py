from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# klasa Profile polaczona 1 do 1 z klasa User 
# aby rozszerzyc informacje dotyczace uzytkownika
# Pola username, password i email z klasy User sa required
# pola first_name, last_name domyslnie nie sa required - ale sa wymagane przez nasz ERD
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media', blank=True)
    description = models.CharField(name='description', max_length=500)

    def __str__(self):
        return self.user.username + " - profil"

# Klasa CV reprezentujaca CV usera
class CV(models.Model):
    cvID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name="cv", on_delete=models.CASCADE)
    skills = models.CharField(max_length=1000)
    experience = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username + " - CV"

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

    def __str__(self):
        return self.tagName

class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    postField = models.CharField(max_length=2048)
    tags = models.ManyToManyField(Tag)
    viewsCount = models.IntegerField() # liczba wyswietlen
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.postField) > 30:
            return self.postField[0:30] + "..."
        else:
            return self.postField

class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    commentField = models.CharField(max_length=2048)    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.commentField) > 30:
            return self.commentField[0:30] + "..."
        else:
            return self.commentField

# Klasa trzymajaca info czy dany uzytkownik ocenil dany komentarz
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="rates", on_delete=models.CASCADE)
    ratingValue = models.IntegerField(default=0)