now as par todays goal we would be studying about django so this is a 
1)a high level python framework used to make high level python application 
and this provides various features naturally like authentication , login 
2) also there are two types of things one is that there are two things the django app and there is django project so in this the django project consist of all the files and the app cosnist of
all the specific work being required 
3)models is the database representation in python 
so we can start the project by having the command -- django project startproject --project_name-- 
4) so settings.py has configuration of the whole application 
5) some important variables being used -- 1- secret key , 2- debug = true 
6)  some points regarding installed apps 
a) django sirf unhi apps ke models ko load karta hai jo installed apps , 
b) vo makemigration migration banayega hi nahi kyuki vo installed  apps mein nahi hai 
c)django ke admin mein jab hi dikhega jab installed apps mein ho aur admin.py mein bhi 

7) URL ROUTING -- so how does django knows what could be the code working in this it does not make 
the response it sends the response at the correct place as well 

form django.contrib import admin 
from django.urls import path 
from . import views 

urlpatterns = {
    path("admin/",admin.site.urls)
    path("products/",views.products)
}
 the flow of the thing is 
 URL
   ↓
View↓
HTML / JSON / Redirect / Error

8)  if the name or the page is being present in the url then only it would be shown in the page opened in the browser rest it would be changing the page 404 not found 

9) Now lets see what are views -- views are being used to receive a request make processing and also returns response 
from django.http return httpResonse

def home(request):
return HttpResponse("hello django")

10) views ko url se connect karna 
from django.urls import path 
from . import views

11) so now we would be talking about reuqest so request is being used to make request for various operation like the url,method,headers

12) so this is what the flow is of how does this work 
Browser
    │
    ▼
HTTP Request
    │
    ▼
Django Server
    │
    ▼
urls.py
    │
Find Matching URL
    │
    ▼
views.products(request)
    │
Business Logic
    │
    ▼
HttpResponse("Protein Powder")
    │
    ▼
Browser

 13) so request is an very important function that is being used to take care of all the information that is set by the client , including the http method , url parameters ,headers , cookies session data 

 14) so what is need of database in django ? 
 the answere is if django is not being used then the data would be store in ram that would be highly inconsistent because the data could be retrieved wrong again and again and also to prevent this on refreshing the website this is being used 
 ex - class visitor(models.Model):
 count = models.IntegerField(default = 0)
 Browser
   │
HTTP Request
   │
urls.py
   │
View
   │
Business Logic
   │
Database (if needed)
   │
HttpResponse
   │
Browser

15) so this is how the django looks to import http 
ex - from django.http import HttpResponse 
def Products (request):
return HttpResponse("Products")

16) this is how the diffrence in between get ad post the get function is being used to get the 
function by typing request.get i this the functio is being used to extract the information and
post is being used to request.post is being used to post the information 

17)Browser
    │
HTTP Request (GET / POST)
    │
    ▼
manage.py
    │
    ▼
settings.py
    │
    ▼
urls.py
    │
Find Matching URL
    │
    ▼
View (Function-Based View)
    │
Read request object
    │
Business Logici
    │
(Optional) Database
    │
    ▼
HttpResponse
    │
    ▼
Browser

18) so waht is an orm an  orm is like an language converter in which we can write the code in python and then it gets converted into sql language in this the thing is it connects to database and when the database is closed then the data would not be extracted 

19) so in this the thing is makemigration is being used to make the blueprint of how things are and migration is being used to blueprint executed and also database being made

20)example -- class Product(models.Model){
    name = models.CharField(max_length=100)
    price = models.IntegerField()

}
python manage.py makemigrations 
python manage.py migrate

21) django admin is one of the most powerful features of django according to which there are various changes being made in the django without any frontend with the given dashboard 

22) how to enable admin
example -- 1)class Product(models.Model):
name = models.CharField(max_length = 100)
price = models.IntegerField()
2)from django.contrib import admin 
from .models import product 
admin.site.register(Product)
admin.site.register(Product)
Product Model
      │
      ▼
admin.site.register(Product)
      │
      ▼
Admin Panel
      │
      ▼
CRUD Operations
      │
      ▼
ORM
      │
      ▼
Database


