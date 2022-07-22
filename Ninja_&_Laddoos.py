# Solution - 52
# Problem Link - https://bit.ly/3qm0cgu & https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
# Challege Start Date - 04.06.2022
# Date - 22.07.2022
# Day 46
# My Approach: tWO Pointer Approach - O(N)
def ninjaAndLadoos(row1, row2, m, n, k):
    # Write your code here.
    i=0
    j=0
    while i<n and j<m:
        if k==1:
            return min(row1[i],row2[j])
        if row1[i]<=row2[j]:
            i+=1
            k-=1
        else:
            j+=1
            k-=1
        if i==n:
            return row2[j+k-1]
        if j==m:
            return row1[i+k-1]
    return 0

# Binary Search -> O(log(min(m*n)))
def ninjaAndLadoos1(row1, row2, m, n, k):
    # Write your code here.
    # M -> ROW1 n->row2
    if m>n:
        return ninjaAndLadoos(row2,row1,n,m,k)
    low=max(0,k-n) # If the largest row2 length is smaller than K then we can't take 0 ele from row1
    high= min(m,k) # We can take max elements of row1 if K is > len(row1)
    while(low<=high):
        cut1=(low+high)//2 # Take these many numbers from row1
        cut2=k-cut1 # Take remaining numbers from row2
        l1=row1[cut1-1] if cut1>0 else -1000000001
        l2=row2[cut2-1] if cut2>0 else -1000000001
        r1=row1[cut1] if cut1<m else 1000000001
        r2=row2[cut2] if cut2<n else 1000000001
        if l1<=r2 and l2<=r1: # If max ele of row1 1st half <= min of right half of row2 and vice-versa
            return max(l1,l2)
        elif l1>r2:
            high=cut1-1 # Take less elements from row1
        else:
            low=cut1+1 # Take more elements from row1
    return 1
row1=[2, 3, 9, 9, 10, 11]
row2=[1, 1, 2, 4, 5, 6, 7, 8, 8, 9, 9, 13]
n=len(row1)
m=len(row2)
k=18
print(ninjaAndLadoos(row1,row2,m,n,k))
print(ninjaAndLadoos1(row1,row2,m,n,k))