# Solution - 12
# Problem Link - https://www.codingninjas.com/codestudio/problems/maximum-subarray-sum_630526?topList=striver-sde-sheet-problems&leftPanelTab=1
# Challege Start Date - 04.06.2022
# Date - 23.06.2022
# Day 17
arr=[-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10]
sum=0
max_sum=arr[0] if arr[0]>0 else 0
for i in arr:
    sum+=i
    if sum<0:
        sum=0
    elif sum>max_sum:
        max_sum=sum
print(max_sum)