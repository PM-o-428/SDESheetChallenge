# Solution - 49
# Problem Link - https://bit.ly/3rng2qC & https://leetcode.com/problems/single-element-in-a-sorted-array/
# Challege Start Date - 04.06.2022
# Date - 19.07.2022
# Day 43
arr=[1,1,5,5,6,6,9,10,10]
n=len(arr)
low=0
high=n-2 # High points to prev last element
while low<=high:
    mid=(low+high)//2
    if arr[mid]==arr[mid^1]:
        low=mid+1
    else:
        high=mid-1
print(arr[low])