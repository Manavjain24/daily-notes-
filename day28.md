from django.contrib import admin
from .models import Product

admin.site.register(Product)

python manage.py runserver

1) query in this we would be discussing about the querysets in here the it is the collection of objects that are being fetched from the database 
ex -- products.object.all()
[
 Product(Mouse),
 Product(Keyboard),
 Product(Monitor)
]

Product.objects.get(id=100)
specific product of id 100 
and also there is empty set so no information would be displayed 


2) filter query Product.objects.filter(price__gt=1000) this is being used to filter out the things and only show the stuff that is bwing required or asked to show
.all()
↓
Everything
↓
QuerySet

.filter()
↓
Matching records
↓
QuerySet

.get()
↓
Exactly ONE record
↓
Single Object

why filter and get both are being present in python ?
because .get() expect karta hai exactly one object and if there are more than one record of same name then filter is being use 

3) Product.objects.exclude(price__lt=1000) -- is being used to make the things more precise and easier sp this also return query set 

4)select_related -- this is being used to see all the related terms in both of the tables that are being present in such a way that it is as follows class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

5) also We use select_related() to reduce the number of database queries when following ForeignKey or OneToOne relationships. It fetches related objects in a single SQL JOIN, avoiding the N+1 query problem.

.

🧠 Memory Trick (Exam + Interview)
Relationship	Method
ForeignKey	✅ select_related()
OneToOneField	✅ select_related()
ManyToManyField	✅ prefetch_related()
Yaad rakhne ka shortcut:
select = "Ek hi related object" (FK / OneToOne)
prefetch = "Bahut saare related objects" (ManyToMany)