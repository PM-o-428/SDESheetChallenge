# Solution - 50
# Problem Link - https://bit.ly/3nnxGcm & https://leetcode.com/problems/search-in-rotated-sorted-array/
# Challege Start Date - 04.06.2022
# Date - 20.07.2022
# Day 44
arr=[4,5,6,7,0,1,2]
target=3
low =0
high = len(arr)-1
while(low<=high):
    mid = (low+high)//2
    if target==arr[mid]: # Print if target is found at mid
        print(mid)
        break
    if arr[mid]>=arr[low]: # Left Part is sorted
        if target>=arr[low] and target<=arr[mid]: # Target Belongs to the left part
            high=mid-1  # Set new search area: low to mid-1
        else:
            low=mid+1   # Target Not in left part so make new search area: mid+1 to high
    else: # Right Part is Sorted
        if target>=arr[mid] and target<=arr[high]: # If target in right part
            low=mid+1  # Set new search area: mid+1 to high
        else: # Target in Left Part
            high=mid-1 # Set new search area: low to mid-1
if low>high: # If Target not found print -1
    print(-1)