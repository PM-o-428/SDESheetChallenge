# Solution - 27
# Problem Link - https://bit.ly/33wlWxk & https://leetcode.com/problems/3sum/
# Challege Start Date - 04.06.2022
# Date - 05.07.2022
# Day 29
arr=[209, -240, 125, 25, 24, 12, 12, -300, 246, 11, 10, 1, -180, 7]
n=len(arr)
k=-30
arr.sort()
ans=[]
m=0
i=0
while i<n:
    left=i+1
    right=n-1
    target=k-arr[i]
    while left<right:
        temp=arr[left]+arr[right]
        if temp==target:
            ans.append([])
            ans[m].append(arr[i])
            ans[m].append(arr[left])
            ans[m].append(arr[right])
            while left<right and arr[left]==ans[m][1]: left+=1
            while right>left and arr[right]==ans[m][2]: right-=1
            m+=1
        elif temp<target:
            left+=1
        else: 
            right-=1
    while i<n-1 and arr[i]==arr[i+1]: i+=1
    i+=1

print(ans)