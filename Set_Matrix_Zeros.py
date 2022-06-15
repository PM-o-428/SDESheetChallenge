# Solution - 4
# Problem Link - https://www.codingninjas.com/codestudio/problems/pascal-s-triangle_1089580?topList=striver-sde-sheet-problems&leftPanelTab=1
# Challege Start Date - 04.06.2022
# Date - 15.06.2022
matrix=[[7,19,3],[4,21,0]]
n=len(matrix[0]) #col
m=len(matrix) #rows
temp=[]
for i in range(m):
    for j in range(n):
        if matrix[i][j]==0:
            for k in range(n):
                if matrix[i][k]!=0:
                    matrix[i][k]=-1
            for k in range(m):
                if matrix[k][j]!=0:
                    matrix[k][j]=-1
for i in range(m):
    for j in range(n):
        if matrix[i][j]==-1: matrix[i][j]=0
print(matrix)