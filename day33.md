1) so to day we are doing the last topic i would say of permissions 
somee of the thingss like the api key should be 
DRF Built-in Permission Classes

Some common ones are:

Permission	Meaning
AllowAny	Anyone can access
IsAuthenticated	Only logged-in users
IsAdminUser	Only admin users
IsAuthenticatedOrReadOnly	Everyone can read, only authenticated users can modify
permiso_class - [isAuthenticated]

-------------------------------------------------------------------------------------------
so in this i would be talking about the two questions that i solved today -- estinamte time taken to solve and recall (4 hrs) also target(2 hrs)
1) products of array except itself
a) first we see wether the size of list is being calculated
b) seconf we intialise the elemnts of predecessor and successor elements as 1 only 
c) and then we see if the
for(i in the rage of 1 to n) 
predecessor[i] = predecessor[i+1] * ans [i+1]
d) and then if we see if the 
for (i in the range of -1,n-2,-1)
successor[i] = successor[i-1] * ans [i-1]
e) ans [i] = predecessor*successor

2) Valid palindrome along with spaces - in this we use two pointer approach 
a) in this we see that there the reverse of a string is equal to that string or not 
b) left = 0 
right = len(s) - 1
while left < right 
while left < right and not s[left].isalnum():
left += 1 
while left < right and not s[left].isalnum():
right -= 1 
if s[left].lower() != s[right].lower() 
return false 

left += 1
right -= 1 
return true


