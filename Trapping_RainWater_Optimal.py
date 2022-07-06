# Solution - 28
# Problem Link - https://bit.ly/3KcxExJ & https://leetcode.com/problems/trapping-rain-water/
# Challege Start Date - 04.06.2022
# Date - 06.07.2022
# Day 30
arr=[2, 5, 1, 2, 5, 1, 2, 5, 1]
n=len(arr)
left_max=0
right_max=arr[n-1]
left=0
right=n-2
water=0
while left<=right:
    if arr[left]<=right_max:
        if arr[left]>=left_max:
            left_max=arr[left]
        else:
            water+=left_max-arr[left]
        left+=1
    else:
        if arr[right]>=right_max:
            right_max=arr[right]
        else:
            water+=right_max-arr[right]
        right-=1
print(water)