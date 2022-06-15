# Solution - 4
# Problem Link - https://www.codingninjas.com/codestudio/problems/pascal-s-triangle_1089580?topList=striver-sde-sheet-problems&leftPanelTab=1
# Challege Start Date - 04.06.2022
# Date - 15.06.2022
row = int(input("Enter Row size - "))
matrix=[list(map(int,input().split())) for j in range(row)] #2D list input
n=len(matrix[0]) #cols
m=len(matrix) #rows
col0=1 # Using this to avoid 1st row elements getting false 0's
for i in range(m):
    if matrix[i][0]==0: col0=0 # If col0 is 0 only then col 0 will be 0 otherwise the 0th row will be marked 0
    for j in range(1,n):
        if matrix[i][j]==0:
            matrix[i][0]=0
            matrix[0][j]=0
for i in range(m-1,-1,-1): #Back Traversal
    for j in range(n-1,0,-1):
        if matrix[0][j]==0 or matrix[i][0]==0:
            matrix[i][j]=0
    if col0==0: matrix[i][0]=0
print(matrix)