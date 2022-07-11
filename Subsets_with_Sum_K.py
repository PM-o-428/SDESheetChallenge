# Solution - 38
# Problem Link - https://bit.ly/3qpmDS1 & https://leetcode.com/problems/combination-sum/
# Challege Start Date - 04.06.2022
# Date - 11.07.2022
# Day 35
# No Repeating(COding Ninjas)
# Repeating allowed(LeetCode)
def func(arr,index,ans,temp,k):
    if k==0:
        ans.append([])
        for j in temp:
            ans[len(ans)-1].append(j)
    if index>=len(arr):
        return
    # Pick
    for i in range(index,len(arr)):   
        temp.append(arr[i])     #Append Curr element
        func(arr,i+1,ans,temp,k-arr[i])  # Start Recursion for updating ans & adding next elements in the next subset
        temp.pop(len(temp)-1)

arr=[0,0,0,0,0,0,0,0]
#arr.sort() Order doesn't matter
ans=[]
temp=[]
k=6
func(arr,0,ans,temp,k)
print(ans)