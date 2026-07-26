so today also i would be talking about the same hashmap thing in this we would be talking about the number k  of time an element is occuring in the list 
in this 

class Solution:
def topkelement(self, nums:List[int], k:int)->List[int]
freq = {}
for num in nums:
freq[num] = freq.get(num,0)+1

sorted_freq = sorted(freq.items(), key = lambda x:x[1],reverse = true)

result = []

for i in the range(k):
result.append(sorted_freq[i][0])

return result 





