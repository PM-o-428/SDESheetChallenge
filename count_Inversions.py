# Solution - 20
# Problem Link - https://bit.ly/339fFb7
# Challege Start Date - 04.06.2022
# Date - 30.06.2022
# Day 24
from os import *
from sys import *
from collections import *
from math import *
def merge_sort(arr,temp,low,mid,high): #Merging Process
    
    i=low #Left array starting index
    j=mid #Right array starting index
    count_=0
    k=low #Temp array starting index
    while i<=mid-1 and j<=high:
        if arr[i]<=arr[j]: #If element in first array is <= ele in 2nd array
            temp[k]=arr[i] #Add smaller one to temp
            k+=1
            i+=1
            
        else:
            temp[k]=arr[j] # Add smaller one in Temp
            k+=1
            j+=1
            count_+=mid-i # count all pairs because all ele after ith index is greater than arr[i] as its sorted
    while i<=mid-1: # Add remaining big elements from 1st array
        temp[k]=arr[i] 
        k+=1
        i+=1
    while j<=high: #Add remaining big elements from 2nd array
        temp[k]=arr[j]
        k+=1
        j+=1
    for k in range(low,high+1): #Update arr
        arr[k]=temp[k]
    return count_

def getInversions(arr,temp, n,low,high) :
    # Write your code here.
    
    count=0
    if low<high:
        mid = (low+high)//2
        count+=getInversions(arr,temp,n,low,mid) # Dividing from mid(1st halves)
        count+=getInversions(arr,temp,n,mid+1,high) #2nd halves
        count+=merge_sort(arr,temp,low,mid+1,high) #Merging after all divides
    return count

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
low=0
high=n-1
temp=[0]*n
print(getInversions(arr,temp, n,low,high))