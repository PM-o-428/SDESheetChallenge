# Solution - 19
# Problem Link - https://bit.ly/3Gs6wZu
# Challege Start Date - 04.06.2022
# Date - 30.06.2022
# Day 24

#XOR and Sum Soln available on Notes(CP)
#My Soln - O(nlogn)+O(n) || Space - O(1)

arr=[5,6,2,8,5,1,3,4]
n=len(arr)
i=0
arr.sort()
M=0
while i<n-1:
    if arr[i+1]-arr[i]==1:
        i+=1
        continue
    elif arr[i+1]-arr[i]>1:
        M=arr[i]+1
    elif arr[i+1]-arr[i]==0:
        R=arr[i]
    i+=1
if M==0:
    M=1 if 1 not in arr else arr[n-1]+1
print(M,R)