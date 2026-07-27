now as par todays goal we would be studying about django so this is a 
1)a high level python framework used to make high level oython application 
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
10)