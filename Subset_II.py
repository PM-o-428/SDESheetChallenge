# Solution - 37
# Problem Link - https://bit.ly/3qnaLjq & https://leetcode.com/problems/subsets-ii/
# Challege Start Date - 04.06.2022
# Date - 11.07.2022
# Day 35
def func(arr,index,ans,temp):
    if index>0:
        ans.append([])
        for j in temp:
            ans[len(ans)-1].append(j)
          
    # Pick
    for i in range(index,len(arr)):
        if i!=index and arr[i]==arr[i-1]: # Check for duplicate element
            continue
        temp.append(arr[i])     #Append Curr element
        func(arr,i+1,ans,temp)  # Start Recursion for updating ans & adding next elements in the next subset
        temp.pop(len(temp)-1)

arr=[4,4,4,1,4]
arr.sort()
ans=[]
ans.append([])
temp=[]
func(arr,0,ans,temp)
print(ans)