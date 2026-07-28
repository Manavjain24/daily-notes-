class Author(models.Model):
    name = models.Charfield(max_len = 100)

class Book(models.Model):
titles = models.Charfield(max_length  = 100)
author = models.foreignkey(Author,on_delete = models.CASSCADE)

in this the work of the annotated field is to make the count of some of the fields required means it creates an extra field 
from django.db.models import count 
author = Author.objects.annotate(book_count = Count("book"))
author = Author.objects.annotate(book_count = Count("book"))

class based views 
from django.http import httpresponse
def home(request):
return httpResponse("Hello")

--so as we add multiple call features into the into the prm for various purposes like the get(), post() function so these are useless instead of these we would be using cbv

-- these are class based views in this we could create a class 
eg -- class homeview(view):
def get(sekf,request)
| Function-Based View           | Class-Based View                    |
| ----------------------------- | ----------------------------------- |
| Uses `def`                    | Uses `class`                        |
| One function handles requests | Separate method for GET, POST, etc. |
| Simple for small apps         | Better for medium & large apps      |
| Less reusable                 | Highly reusable through inheritance |

so what is the format of writing an fbv 
eg -- class name (view):
def get(self,request)
..
def post(Sekf,request)
..

so there is a file tyoe knowns as templates in django that is being used to fill dynamic data inside of it the thing is it is there in html so templated do keep repeating one by one so there is the use of that for example in the header tag like <h1>{{name}}<h1>
so here there are double brackets being used that symbolises that the data iis being variable 
Browser
   │
Request
   │
View
   │
Context
{name: "Manav"}
   │
Template
<h1>Hello {{ name }}</h1>
   │
Django Render
   │
<h1>Hello Manav</h1>
   │
Browser

{{ }} → Variable print karta hai.
{% %} → Logic/control statements ke liye hota hai (jaise for, if, block, etc.).



