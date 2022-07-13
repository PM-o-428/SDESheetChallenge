# Solution - 41
# Problem Link - https://bit.ly/3KcCP0D & https://leetcode.com/problems/permutation-sequence/
# Challege Start Date - 04.06.2022
# Date - 13.07.2022
# Day 37
n=int(input())
k=int(input())
fact=1
seq=[] # Storing the sequence 1-N
for i in range(1,n):
    fact*=i         # Storing (n-1)!   because one element will be stored at first so n-1 left
    seq.append(i)
seq.append(n)
ans=''
k-=1
while True:
    index=k//fact 
    ans=ans+str(seq[index]) # checking and storing in which series the K belongs
    seq.pop(index) # Poping the stored element then the rest elements are the 1st seq among them
    if len(seq)==0: break
    k=k%fact # Reducing K to find next series starting number
    fact=fact//len(seq) # Decreasing Fact as elementas are popped out
print(ans)
