in this  day we would be learning about generators 
#generators are used to give the loop in which it return back the loops according to which the function allows you to iterate over
a sequence of values once at a time 
example -- 
def countdown(n)
while n>0 
yield n 
n -= 1
counter = countdown(3)
print(next(counter))
# methods used to make generators could be from for loop or from the next() function that are being used so it makes 
the result iterate one after another 