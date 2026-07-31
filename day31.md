1)so this is now we would be talking about generic views as there are many repetative function inside of a specific function so we use generic views in order to make the things more and more neat and less repetetive this is being used
example - def UserAPIview(APIView)
def get(self)
def post(self)

so here as we can see get and post are being repetetively used 

instead of this class UserListCreateView(ListCreateAPIView):
queryset = user.object.all()
serializer_class = UserSerializer

Sirf list? → ListAPIView
Sirf create? → CreateAPIView
Dono? → ListCreateAPIView

these are the usecases for which these things are being used for 

DRF ne Generic Views ko Lego blocks ki tarah banaya hai.

APIView
      │
      ▼
GenericAPIView
      │
 ┌────┼────┐
 │    │    │
ListModelMixin
CreateModelMixin
RetrieveModelMixin
UpdateModelMixin
DestroyModelMixin


