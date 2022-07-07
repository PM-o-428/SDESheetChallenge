# Solution - 29
# Problem Link - https://bit.ly/31Usllh & https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Challege Start Date - 04.06.2022
# Date - 07.07.2022
# Day 31

# My Approach O(n)
arr=[1,1,1,5,6,7,7,9]
i=0
while i<len(arr)-1:
    if arr[i]==arr[i+1]:
        arr.remove(arr[i])
    else:
        i+=1
print(len(arr))

# Another Approach O(n)
i=0
j=1
while j<len(arr):
    if arr[i]!=arr[j]: # If distinct element found then i++ and add ele in arr[i] & j++
        i+=1
        arr[i]=arr[j]
    j+=1
print(i+1)