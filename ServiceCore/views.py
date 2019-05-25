from django.shortcuts import render
import json

from rest_framework.parsers import JSONParser

from ServiceCore.serializers import *
from ServiceCore.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView 
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework import mixins

class CVView(APIView):
    permission_classes = (IsAuthenticated,)
    
    # pobranie CV z bazy
    def get(self, request):
        cv = CV.objects.get(user=request.user)

        cvSerializer = CVSerializer(cv)
    
        return Response(cvSerializer.data)

    # zapis CV do bazy
    def post(self, request):
        requestedData = JSONParser().parse(request)
        print(requestedData)
        if requestedData['skills'] is None or requestedData['experience'] is None:
            return Response({"message": "Nie podano wszystkich danych"})
        try:            
            newCV = CV.objects.create(user=request.user,
                                      skills=requestedData['skills'],
                                      experience=requestedData['experience'])
            newCV.save()
        except:
            return Response({"message": "Nie udalo sie utworzyc CV"})

        return Response({"message": "CV zostlao utworzone"})

# pobranie wszystkich profili uzytkownikow, tworzenie uzytkownika
class ProfileRecordView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        """
        Get user profile
        """
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializerExtended(profile)
        return Response(serializer.data)

    # Tworzenie nowego uzytkownika - rejestracja
    def post(self, request):
        requestedData = JSONParser().parse(request)
        print(requestedData)

        isUserExist = None
        user = None
        
        try:
            isUserExist = User.objects.get(username=requestedData['username'])
            print("Uzytkowniko podanym nicku istnieje!")
        except:
            isUserExist = False
            print("Username wolny, jest ok")

        if isUserExist == False:
            user = User.objects.create_user(first_name=requestedData['first_name'],
                                       last_name=requestedData['last_name'],
                                       username=requestedData['username'],
                                       email=requestedData['email'],
                                       password=requestedData['password'])
        else:
            return Response({"message": "Użytkownik o podanym nicku juz istnieje"})

        try:
            user.save()
            profile = Profile.objects.create(user=user, description="")
            profile.save()
            print("Uzytkownik zarejestrowany!")
            
            return Response({"userData": requestedData, "message": "Użytkownik zostal zarejestrowany"})
        except Exception as e:
            print(str(e))      

            return Response({"userData": requestedData, "message": "Nie udalo sie zarejestrowac uzytkownika"})

        """
        Create a profile record

        requestedData = JSONParser().parse(request)

        serializer = UserSerializer(data=requestedData)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=requestedData)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
        """
    
    #edycja opisu profilu użytkownika
    def put(self, request):
       
        requestedData = JSONParser().parse(request)

        print(requestedData)

        profile = Profile.objects.get(user=request.user)
        profile.description = requestedData['newDescription']
        profile.save()

        return Response({"message": "Edytowano opis profilu"})

# wszystkie posty w formie skroconej (bez komentarzy i tresci)
class PostPreviewView(ListAPIView):    
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all().order_by("-createdAt")
    serializer_class = PostPreviewSerializer

# wszystkie posty
class PostView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all().order_by("-createdAt")
    serializer_class = PostSerializer

# szzczegoly posta
class PostDetailsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        postToShow = None

        try:
            postToShow = Post.objects.get(pk=pk)
            postToShow.viewsCount += 1
            postToShow.save()
        except:
            return Response({"message": "Nie ma takiego posta!"})
        
        serializedPost = PostSerializer(postToShow)

        return Response(serializedPost.data)
    

# filtrowanie/wyszukiwanie postow
class PostViewFilter(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = PostSerializer

    def get_queryset(self):
        searchParam = self.request.query_params.get('param', None)
        print(searchParam)
        posts = Post.objects.all().order_by('-createdAt')
        print(type(posts))
        postsFiltered = list()

        for post in posts:
            if searchParam in post.title or searchParam in post.postField:
                postsFiltered.append(post)

        return postsFiltered

# tworzenie posta
class PostCreate(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        #u = (request.user)
        print(request.user)
        requestedData = JSONParser().parse(request)
        newPostData = requestedData['params']

        postToAdd = None
        tag = None
        tagsToAdd = []

        for tagToAdd in newPostData['tags']:
            try: 
                tag = Tag.objects.get(tagName=tagToAdd)
            except: 
                tag = Tag.objects.create(tagName=tagToAdd)
                print(tag)
            tagsToAdd.append(tag)

        try:
            post = Post.objects.create(author=request.user, viewsCount=0, title=newPostData['title'], postField=newPostData['postField'])
        except:
            return Response({"message": "Nie udalo sie utworzyc posta"})

        for tag in tagsToAdd:
            try:                
                post.tags.add(tag)
            except Exception as e:
                print(str(e))
                return Response({"message": "Nie udalo sie dodac wszystkich tagow"})
        
        post.save()

        return Response({"message": "Post zostal utworzony"})

# tworzenie komentarza
class CommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        requestedData = JSONParser().parse(request)

        if requestedData['params'] is None:
            print("Brak obiektu params - brak danych")
            return Response({"message": "Brak danych"})
        
        newCommentData = requestedData['params']
        print(newCommentData)

        post = None

        try:
            if newCommentData['postPk'] is None:
                print("Brak podanego klucza glownego")
                return Response({"message": "Nie podano id posta"})
            
            post = Post.objects.get(pk=newCommentData['postPk'])
        except:
            print("Post o podanym kluczu nie istnieje")
            return Response({"message": "Post o podanym kluczu nie istnieje"})
        
        if newCommentData['comment'] is None:
            print("Brak podanego pola komentarza")
            return Response({"message": "Brak podanego pola komentarza"})

        try:            
            newComment = Comment.objects.create(commentField=newCommentData['comment'],
                                            author=request.user,
                                            post=post)
            newComment.save()
            return Response({"message": "Komentarz dodany"})
        except:
            return Response({"message": "Nie udalo sie dodac komentarza"})

# dodawanie oceny do komentarza
class RateCommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        requestedData = JSONParser().parse(request)
        newRate = requestedData['rate']
        comment = None
        try:
            comment = Comment.objects.get(pk=pk)
            (rate, created) = Rating.objects.get_or_create(user=request.user, comment=comment)
            rate.ratingValue = newRate
            rate.save()
        except Exception as e:
            print(e)
            print("Nie udalo sie dodac oceny")
            return Response({"message": "nie udalo sie dodac oceny"})

        currentComment = CommentSerializer(comment)

        return Response(currentComment.data)