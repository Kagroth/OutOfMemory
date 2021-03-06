# OutOfMemory
Projekt portalu społecznościowego dla programistów

## Uruchomienie interfejsu: 
W folderze clientapp uruchomic polecenie:
```
npm run dev
```
Jeżeli polecenie nie zadziała, w folderze clientapp użyj polecenia:
```
npm install
```
a następnie polecenia run dev.

## Uruchomienie serwisu:
```
python manage.py runserver
```
## Python libraries

* django-rest-framework
* django-cors-headers

## URL's

+ /myprofile/ - GET (wyświetlenie profilu - aktualny zalogowany user)
+ /user/ - POST (dodanie nowego usera) 
+ /user/<username>/ - GET, PUT (pobranie i edycja konkretnego usera) 
+ /user/<username>/post/ - GET (pobranie postów konkretnego usera) 
+ /user/<username>/comment/ - GET (pobranie komentarzy napisanych przez usera) 
+ /post/ - POST (dodanie nowego postu) 
+ /post/<post>/ - GET, PUT (pobranie konkretnego postu) 
+ /post/<post>/comment/ - GET, POST (pobranie komentarzy postu oraz dodanie komentarza pod postem) 
+ /post/<post>/comment/id/- GET, PUT (pobranie i edycja konkretnego komentarza pod postem) 
+ /job/ - GET, POST, PUT 
+ /job/applications/ - GET, POST
+ /tag/ - GET (pobranie postów z konkretnym tagiem) 
