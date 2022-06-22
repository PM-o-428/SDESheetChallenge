# Solution - 11
# Problem Link - https://www.codingninjas.com/codestudio/problems/longest-subset-zero-sum_920321?topList=striver-sde-sheet-problems
# Challege Start Date - 04.06.2022
# Date - 22.06.2022
# Day 16
arr=[21, 57, -21, 41, -57, -31, -70, 60, 2, -2, 0, 0]
max_count=0 #(ans) Max subarray with sum of 0
sum=0
HashMap={} # Storing sum and the index i where that sum has been found
for i in range(len(arr)):
    sum+=arr[i]
    if sum==0:
        max_count=i+1 # If sum is 0 found that means that whole subarray from start to i will be the subarray with max length till then
    else:
        if sum in HashMap:
            max_count=max(max_count,i-HashMap[sum]) # comparing with the length of subarray (index difference where last time that sum has been found)
        else:
            HashMap.update({sum:i}) #Adding sum and the index if not exists in HashMap
print(max_count)