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
#methods used to make generators could be from for loop or from the next() function that are being used so it makes 
the result iterate one after another 


next thing we would be talking about is itertools 
in this the itertools is a library that is being made in pyython in which the collection of fast memory effecient functions for 
working with iterators . 
some type of iterators are as follows
1) infinite iterators 
-- the functions generate infinite loops that lasts forever and the condition is being required them to stop 
-- example - counter = count(start = 10 , step = 2)
2)terminating iterators
these functions take existing iterables and process them into finite , optimised streams 
