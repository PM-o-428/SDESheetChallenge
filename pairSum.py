# Solution - 10
# Problem Link - https://www.codingninjas.com/codestudio/problems/pair-sum_697295?topList=striver-sde-sheet-problems&leftPanelTab=1
# Challege Start Date - 04.06.2022
# Date - 21.06.2022
# Day 15
arr=list(map(int,input().split()))
s=int(input())
arr.sort()
ans=[]
k=0
n=len(arr)
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==s:
            ans.append([])
            ans[k].append(arr[i])
            ans[k].append(arr[j])
            k+=1
print(ans)