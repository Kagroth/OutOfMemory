from django.shortcuts import render
import json

from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser, FileUploadParser

from ServiceCore.serializers import *
from ServiceCore.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import generics, status
from rest_framework import mixins
from PIL import Image


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
            (newCV, created) = CV.objects.get_or_create(user=request.user)
            newCV.skills = requestedData['skills']
            newCV.experience = requestedData['experience']
            newCV.save()
        except:
            return Response({"message": "Nie udalo sie utworzyc CV"})

        return Response({"message": "CV zostlao utworzone"})

    def delete(self, request):
        try:
            cvToDelete = CV.objects.get(user=request.user)
            cvToDelete.delete()
        except:
            return Response({"message": "Nie udalo sie usunac CV"})

        return Response({"message": "Usunieto CV"})


class UserCVView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, username):
        user = None

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            cv = CV.objects.get(user=user)

            serializer = CVRawSerializer(cv)

            return Response(serializer.data)

class TagView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Tag.objects.all().order_by("tagName")
    serializer_class = TagSerializer


# pobranie profilu zalogowanego uzytkownika, tworzenie uzytkownika
class ProfileRecordView(APIView):
    permission_classes = (AllowAny,)

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
            print("Uzytkownik zarejestrowany")

            return Response({"message": "Użytkownik zostal zarejestrowany"})
        except Exception as e:
            print(str(e))

            return Response({"message": "Nie udalo sie zarejestrowac uzytkownika"})

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

    # edycja opisu profilu użytkownika
    def put(self, request):

        requestedData = JSONParser().parse(request)

        print(requestedData)

        profile = Profile.objects.get(user=request.user)
        profile.description = requestedData['newDescription']
        profile.save()

        return Response({"message": "Edytowano opis profilu"})


class ProfileView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, username):
        userToShow = User.objects.filter(username=username)
        if userToShow.exists() and userToShow.count() == 1:
            profile = Profile.objects.get(user=User.objects.get(username=username))
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        else:
            return Response({"message": "Uzytkownik o takim nicku nie istnieje"}, status=status.HTTP_404_NOT_FOUND)

class ProfileAvatarUpload(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        profile = Profile.objects.get(user=request.user)
        file_obj = request.FILES['file']
        # https://goodcode.io/articles/django-rest-framework-file-upload/
        try:
            img = Image.open(file_obj)
            img.verify()
        except:
            raise ParseError("Unsupported image type")
        profile.avatar.save(filename, file_obj, save=True)
        # do some stuff with uploaded file
        return Response(status=204)


# wszystkie posty w formie skroconej (bez komentarzy i tresci)
class PostPreviewView(ListAPIView):
    permission_classes = (AllowAny,)
    #queryset = Post.objects.all().order_by("-createdAt")
    serializer_class = PostPreviewSerializer

    def get_queryset(self):
        return Post.objects.all().order_by("-createdAt")


# wszystkie posty
class PostView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostPreviewSerializer

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


# posty o okreslonym tagu
class PostPreviewByTagFilterView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostPreviewSerializer

    def get_queryset(self):
        searchParam = self.kwargs['tag']
        print(searchParam)
        postsFiltered = Post.objects.filter(tags__tagName=searchParam).order_by('-createdAt')

        return postsFiltered


# tworzenie posta
class PostCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # u = (request.user)
        print(request.user)
        requestedData = JSONParser().parse(request)
        newPostData = requestedData['params']

        postToAdd = None
        tag = None
        tagsToAdd = []
        print(newPostData)

        for tagToAdd in newPostData['tags']:
            try:
                tag = Tag.objects.get(tagName=tagToAdd['tagName'])
            except Exception as e:
                print(tag)
                print(e)
                return Response({"message": "Brak podanego tagu"})

            tagsToAdd.append(tag)

        try:
            post = Post.objects.create(author=request.user, viewsCount=0, title=newPostData['title'],
                                       postField=newPostData['postField'])
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


# przeglądanie ofert pracy
class JobOffersPreviewView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # queryset = JobOffer.objects.all()
    serializer_class = JobOffersSerializer

    def get_queryset(self):
        return JobOffer.objects.all().order_by("-createdAt")

class JobOfferFilterView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = JobOffersSerializer

    def get_queryset(self):
        searchParam = self.request.query_params.get('param', None)
        searchParam = searchParam.lower()
        print(searchParam)
        offers = JobOffer.objects.all().order_by('-createdAt')
        print(type(offers))
        offersFiltered = list()

        for offer in offers:
            if searchParam in offer.title.lower() or \
               searchParam in offer.companyName.lower() or \
               searchParam in offer.companyName.lower() or \
               searchParam in offer.companyLocation.lower():
                offersFiltered.append(offer)

        return offersFiltered


# tworzenie oferty pracy
class JobOfferCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = JobOffersSerializer

    # tworzenie ofery pracy
    def post(self, request):
        requestedData = JSONParser().parse(request)
        newJobData = requestedData['params']

        try:
            job = JobOffer.objects.create(user=request.user, title=newJobData['title'],
                                          salaryMin=newJobData['salaryMin'],
                                          salaryMax=newJobData['salaryMax'],
                                          description=newJobData['description'],
                                          requirements=newJobData['requirements'],
                                          companyName=newJobData['companyName'],
                                          companyLocation=newJobData['companyLocation'])
            job.save()
        except:
            return Response({"message": "Nie udalo sie utworzyc oferty pracy"})
        return Response({"message": "Pomyślnie utworzono ofertę pracy"})


#   Edycja oferty pracy
class JobOfferEditView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = JobOffersSerializer

    def put(self, request):
        requestedData = JSONParser().parse(request)
        newJobData = requestedData['params']
        print(requestedData)
        try:
            job = JobOffer.objects.get(jobOfferID=newJobData['pk'])
            if job.user == request.user:
                job.title = newJobData['title']
                job.salaryMin = newJobData['salaryMin']
                job.salaryMax = newJobData['salaryMax']
                job.description = newJobData['description']
                job.requirements = newJobData['requirements']
                job.companyName = newJobData['companyName']
                job.companyLocation = newJobData['companyLocation']
                job.save()
            else:
                print("Próbujesz edytować cudzą ofertę pracy")
                Response({"message": "Próbujesz edytować cudzą ofertę pracy"})
        except Exception as e:
            print("error : " + e)
            print("nie udało sie edytować oferty pracy")
            return Response({"message": "Nie udalo sie edytowac oferty pracy"})
        print("pomyślnie edytowano ofertę pracy")
        return Response({"message": "Pomyślnie edytowano ofertę pracy"})


# pobranie konkretnej oferty pracy
class JobOfferDetailsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        offerToShow = None

        try:
            offerToShow = JobOffer.objects.get(pk=pk)
            offerToShow.viewsCount += 1
            offerToShow.save()
        except:
            return Response({"message": "Nie ma takiej oferty pracy"})

        serializedOffer = JobOffersSerializer(offerToShow)

        return Response(serializedOffer.data)


class ApplicationView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        try:    
            targetJob = JobOffer.objects.get(pk=pk)

            serializerApps = JobOfferWithApplicationsSerializer(targetJob)

            return Response(serializerApps.data)
        except Exception as e:
            print(e)
            return Response({"message": "Nie udalo sie pobrac aplikacji na ta oferte"})

    def post(self, request, pk):
        cv = request.user.cv
        targetJob = None

        try:
            targetJob = JobOffer.objects.get(pk=pk)
        except Exception as e:
            print(e)
            return Response({"message": "Taka oferta pracy nieistnieje"}, status=status.HTTP_404_NOT_FOUND)
        
        print(request.user)
        print(targetJob.user.username)
        #print(str(request.user) == str(targetJob.user.username))
        if targetJob.user.username == request.user.username:
            return Response({"message": "probojesz aplikować na swoją ofertę pracy!"})

        try:
            if Application.objects.filter(job=targetJob, cv=cv).exists():
                return Response({"message": "Juz aplikowales na te oferte"}, status=status.HTTP_200_OK)

            app = Application.objects.create(job=targetJob,
                                             cv=cv)
            #app.save()

        except Exception as e:
            print(e)
            return Response({"message": "Nie udalo sie utworzyc aplikacji na oferte pracy"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Aplikacja na oferte zostala zapisana"})
