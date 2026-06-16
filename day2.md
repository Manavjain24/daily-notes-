#day 2 -- decorators 
#decorator functions 
so these are the (decorators take another functions as input) and then functions that are used to decorate the base class function with their own input so it is basically a function that adds on to another function (that is the base function ) to add more value 
to the base class function without making any changes to the base function 
 ** we discussed the use of it but how is it important as the use of it is that it extends that the use of the base 
 function with adding more value to it in such an manner that it does look more systamatic.
 example - 
 def pizza(func):
    def wrapper():
        print("There is cheese added to it")
        func()
    return wrapper

@pizza
def makepizza():
    print("Here is the tomato being added")

makepizza()

why are these important 
1 helps in login 
2 authentication 
3 helps in access controlling 

questions in mind 
1 what is git 
 ans -- so the answere to this question is very simple it is like an "version control system " this sounds like a very 
 heavy word all in all but it is not so a version control system is the one which helps in tracking all the changes are being made 
 by the peole who are contributing into the project and so to ensure the complete history of git and also the safe experinmentation also helps 

#day 2 -- context managers




