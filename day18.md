this is the daily practise that i have been putting in the work in so in this i want to tell 
u that the coe i just solved was so easy i took lot of time to solve 
this is like the following 
def duplicate_element(list nums[int] , self ) -> bool 
freq = {}
for num in nums:
if (num in freq):
return true 
freq[num] = 1 
return false 

class Solution :
def valid_Anagram(self , s:str,t:str) ->bool:
freq1 ={}
freq2 = {}
for ch in s : 
freq1[ch] = freq1.get(ch,0) +1 
for ch in t : 
freq2[ch] = freq2.get(ch,0) +1 
return freq1 == freq2 

so i forgot to state the problem statment that is valid anagram is being solved in python 