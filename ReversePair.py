# Solution - 21
# Problem Link - https://bit.ly/3tm5PgF & https://leetcode.com/problems/reverse-pairs/
# Challege Start Date - 04.06.2022
# Date - 01.07.2022
# Day 25
def merge(arr,low,mid,high):
    count=0
    i=low
    j=mid+1
    temp=[]
    while i<=mid:
        while j<=high and arr[i]>2*arr[j]:
            j+=1
        count+=j-mid-1
        i+=1
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for k in range(low,high+1):
        arr[k]=temp[k-low]
    return count
def inversion_divide(arr,n,low,high):
    inv_count=0
    if low>=high:
        return 0
    mid=(low+high)//2
    inv_count+=inversion_divide(arr,n,low,mid)
    inv_count+=inversion_divide(arr,n,mid+1,high)
    inv_count+=merge(arr,low,mid,high)
    return inv_count
def reversePairs(arr, n):
    # Write your code here.
    low=0
    high=n-1
    count=inversion_divide(arr,n,low,high)
    return count

arr=[9, 4, 9, 3, 1, 5, 3, 2, 1, 2]
n=len(arr)
print(reversePairs(arr,n))