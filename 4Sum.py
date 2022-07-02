# Solution - 22
# Problem Link - https://bit.ly/3qpfEsj & https://leetcode.com/problems/4sum/
# Challege Start Date - 04.06.2022
# Date - 01.07.2022
# Day 25
nums=[2,2,2,2,2]
target=8
nums.sort()
n=len(nums)
ans=[]
k=0
i=0
while i<n:
    j=i+1
    while j<n:
        target_2=target-nums[i]-nums[j]
        left=j+1
        right=n-1

        while left<right:
            sum2=nums[left]+nums[right]
            if sum2<target_2:
                left+=1
            elif sum2>target_2:
                right-=1
            else:
                ans.append([])
                ans[k].append(nums[i])
                ans[k].append(nums[j])
                ans[k].append(nums[left])
                ans[k].append(nums[right])
                k+=1
                
                while left<right and nums[left]==ans[k-1][2]: left+=1
                while right>left and nums[right]==ans[k-1][3]: right-=1
        while j+1<n and nums[j+1]==nums[j]: j+=1
        j+=1
    while i+1<n and nums[i+1]==nums[i]: i+=1
    i+=1

print(ans)