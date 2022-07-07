# Solution - 30
# Problem Link - https://www.codingninjas.com/codestudio/problems/maximum-consecutive-ones_892994?topList=striver-sde-sheet-problems
# Challege Start Date - 04.06.2022
# Date - 07.07.2022
# Day 31
# O(2N)

arr=[1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
n=len(arr)
k=6
start=0
end=0
max_len=0
zeroes=0
while end<n:
    if arr[end]==0:
        zeroes+=1
        if zeroes<=k:
            max_len=max(max_len,end-start+1)
        else:
            while arr[start]!=0: # IF extra zeroes found then decrease zeroes by
                start+=1         # shorting the window by moving start to the right till zero is found
            start+=1
            max_len=max(max_len,end-start+1)
            zeroes-=1
    else:
        max_len=max(max_len,end-start+1)
    end+=1
print(max_len)