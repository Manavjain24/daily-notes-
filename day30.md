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

4)