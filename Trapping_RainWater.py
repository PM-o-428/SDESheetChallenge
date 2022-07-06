# Solution - 28
# Problem Link - https://bit.ly/3KcxExJ & https://leetcode.com/problems/trapping-rain-water/
# Challege Start Date - 04.06.2022
# Date - 06.07.2022
# Day 30
arr=[2, 5, 1, 2, 5, 1, 2, 5, 1]
n=len(arr)
suffix=[]
prefix=[]
water=0
temp_max1=0
temp_max2=0
j=n-1
for i in range(n):
    if arr[i]>temp_max1:
        temp_max1=arr[i]
    prefix.append(temp_max1)
    if arr[j]>temp_max2:
        temp_max2=arr[j]
    suffix.append(temp_max2)
    j-=1
suffix.reverse()
for i in range(n):
    temp=(min(prefix[i],suffix[i])-arr[i])
    water+=temp if temp>0 else 0
print(water)