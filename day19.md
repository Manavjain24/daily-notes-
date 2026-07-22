1_ valide anagram 
2_number in sequence 

code of  1
def anagram(int self , str s , str t) -> bool 
freq ={}
freq1 = {}
for ch in s: 
freq[0] = freq.get(ch,0) + 1 
for ch in t: 
freq1[0] = freq.get(ch,0) + 1 
return freq1 == freq2:

so today the most important function i learned was enumerate function in this function we could get the index as well as access to number as well 
class Solution:
def twoSum(slef,nums: List[int],target:int)->List[int]:

hashmap{}

for i , num in emumerate(nums):
complement = target - num 

if complement in hashmap:
return [hashmap[complement],i]

hashmap[num] = i 

another problem in this we sould be using hashmaps again 

for word in words:
    freq = {}

    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1

    print(word)
    print("Length:", len(word))
    print("Frequency:", freq)

for n = 0 to word.len:
    if (len(word)==len(word+n) && freq(word) == freq(word+n))
    print()

