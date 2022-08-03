# Solution - 64
# Problem Link - https://bit.ly/3K6weoJ
# Challege Start Date - 04.06.2022
# Date - 03.08.2022
# Day 58

str1='notmwhvwrb'
str2='norwvhwmtb'

# Ez Soln
from collections import Counter
print(Counter(str1)==Counter(str2)) # Counter returns HashMap of the string with char frequency

# Naive HashMap Solution
def areAnagram(str1, str2):
    hashMap={}
    count=0
    if len(str1)!=len(str2): return False
    for i in str1:
        if i in hashMap:
            hashMap[i]+=1
        else:
            hashMap[i]=1
    for i in str2:
        if i in hashMap:
            hashMap[i]-=1
            if hashMap[i]<0: return False
            elif hashMap[i]==0:
                count+=1
        else:
            return False
    if count<len(hashMap): return False
    return True

print(areAnagram(str1,str2))