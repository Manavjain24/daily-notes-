1)so in this we would be talking about the why routers are being used 
2)so routers are being used so that the django could produce the url automatically so that the 
code that is beinf repetatively generated is not being done and instead of that we could make the 
singles line of code such as -> router.register("products",ProductViewSet)
so in this the endpoinst being created are as follows 
GET      /products/
POST     /products/
GET      /products/{id}/
PUT      /products/{id}/
PATCH    /products/{id}/
DELETE   /products/{id}/
 so in this the django creates the urls automatically 

 3) okay so the thing is router creates all the operations that are being required to used by the following things in order for it to work if certain kind of operations like that of the delete operations are being removed then router does not create the files of that thign it only does make the 

 | Component  | Responsibility             |
| ---------- | -------------------------- |
| Router     | URL Mapping                |
| ViewSet    | Business Logic             |
| Serializer | Validation + Python ↔ JSON |
| ORM        | Python → SQL               |
| Database   | Data Storage               |
---------------------------------------------------------------------------------------------------

4)Pagination - so in this we can split the larger document into smaller pieces so only some number reaches the api response 
so we do not have any as such logic for pagination but we can specify what do we want from 
oagination in the form of like 
a) page number pagination -- /products/?page=3
b) LimitOffsetPagination -- /products/?limit=20&offset=40
c) cursorpagination -- Used for very large datasets like Instagram, Twitter, LinkedIn feeds.
so in cursorpagination the data gets regularly being updated and also the data is being retreived on the latest basis 
----------------------------------------------------------------------------------------------------
5) Filtering 