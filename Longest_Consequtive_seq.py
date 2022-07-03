# Solution - 23
# Problem Link - https://bit.ly/34EoAS0 & https://leetcode.com/problems/longest-consecutive-sequence/
# Challege Start Date - 04.06.2022
# Date - 02.07.2022
# Day 26
arr=list(map(int,input().split()))
max_count=0
temp=set(arr)
for i in arr:
    count=0
    if i-1 not in temp:
        curr_num=i
        count+=1
        while i+1 in temp:
            count+=1
            i+=1
        max_count=max(max_count,count)
print(max_count)