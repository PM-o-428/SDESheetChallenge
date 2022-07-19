# Solution - 48
# Problem Link - https://bit.ly/33AHZTz
# Challege Start Date - 04.06.2022
# Date - 18.07.2022
# Day 42
# Hash Table solution - O((n*m)log(n*m))+O(n*m)
def getMedian(matrix):
    # Write your code here.
    temp=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp.append(matrix[i][j])
    temp.sort()
    return temp[len(temp)//2]


# Binary Search Solution

def countSmallerEqNums(matrix,i,search):
    l=0
    r=len(matrix[i])-1
    while(l<=r):
        mid=(l+r)//2
        if matrix[i][mid]<=search:
            l=mid+1
        else:
            r=mid-1
    return l

def getMedian1(matrix):
    low=0
    high=int(1e9)
    
    elements_before_mid=(len(matrix)*len(matrix[0]))//2

    while low<=high:
        mid=(low+high)//2
        count=0
        for i in range(len(matrix)):
            count+=countSmallerEqNums(matrix,i,mid)
        if count<=elements_before_mid: # How many elements should be there left to mid is less
            low=mid+1 # Shift low to right
        else:
            high=mid-1 # Shift high to left
    return low # Where low becomes > high, that element is the actual mid

# Driver Code
matrix=[[2, 6, 9], [1, 5, 11], [3, 7, 8]]
print(getMedian1(matrix))
print(getMedian(matrix))

