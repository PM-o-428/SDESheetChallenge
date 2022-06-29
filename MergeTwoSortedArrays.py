# Solution - 18
# Problem Link - https://bit.ly/33umm7e
# Challege Start Date - 04.06.2022
# Date - 29.06.2022
# Day 23

#Python Easy Soln
'''def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    arr1=arr1+arr2
    arr1.sort()
    i=0
    while(arr1[i]==0):
        arr1.pop(i)
    return arr1'''

#Optimal (GAP Method) (O(nlogn))

def swap(arr1,i,j):
    temp=arr1[i]
    arr1[i]=arr1[j]
    arr1[j]=temp

arr1=[2, 3, 4,5,20,0, 0,0, 0]
arr2=[3, 5,10,22]
arr1=arr1+arr2
n=len(arr1)
gap = n//2 if n%2==0 else n//2 +1

while gap>=1:
    p1=0
    p2=p1+gap
    while p2<n:
        if arr1[p1]>arr1[p2]:
            swap(arr1,p1,p2)
            p1+=1
            p2+=1
        else:
            p1+=1
            p2+=1
    
    gap=gap//2 if gap%2==0 or gap//2==0 else gap//2 +1
i=0
while(arr1[i]==0):
    arr1.pop(i)
print(arr1)