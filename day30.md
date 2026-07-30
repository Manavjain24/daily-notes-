1)so why are static files stored seprately ??
-- static files are being stored seprately cause browser could save them in cache memory and then fetch by itself so it does not have to fetch it again and again so it save time and resources as well 
2) so why are forms being used ?
they take the information from the user and then it is being used to take the information as an input and also use to validate info and then send it to the view
Browser
    │
HTML Form
    │
POST Request
    │
Django View
    │
request.POST
    │
Database Check
    │
Response
this is the typical syntax of that loooks like 

3) from django import forms 

def LoginForm(forms.Form):
name = forms.CharField()
password = forms.CharField()

4) so forms acts to validate data views are being used to make the logic of the cod e true
nos the example is -- class LoginForm(forms.Form):
username = forms.CharField(required = true)
password = forms.Charfield(required = true)

5) so here we would be now talking about drf classes 
6) the main question is why is it even required to have drf classes?
so its very simple as react and the database cannot talk to each other directly as there are various security reason and as well as passwords leaks may occur in order to prevent that the django has an serializer model that act as a language converter for converting react(that is javascript) into django(python framework) both can communicate simuntaneously and vice versa so this class that 
example -- class ModelSerializer(Serializers.MODELSSERIALIZERS)
