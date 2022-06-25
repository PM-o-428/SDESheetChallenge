# Solution - 13
# Problem Link - https://www.codingninjas.com/codestudio/problems/next-permutaion_893046?topList=striver-sde-sheet-problems&leftPanelTab=1
# Challege Start Date - 04.06.2022
# Date - 25.06.2022
# Day 19
permutation=[2,3,1,4,5]
n=len(permutation)
def swap(permutation,i,j):
    temp=permutation[i]
    permutation[i]=permutation[j]
    permutation[j]=temp
def reversing(permutation,i,j):
    while(i<j):
        swap(permutation,i,j)
        i+=1
        j-=1
def nextPermutation(permutation, n):
    # Write your code here.
    i=n-2 
    
    while i>=0 and permutation[i]>=permutation[i+1]: # Iterate till a small element is found
        i-=1    #elements after small element found, is in decreasing order
    
    if i>=0:
        j=n-1
        while permutation[i]>=permutation[j]: j-=1 #Find just greater element in the Decreasing subarray as its back interation
        swap(permutation,i,j)
    reversing(permutation,i+1,n-1)
    return permutation
print(nextPermutation(permutation,n))