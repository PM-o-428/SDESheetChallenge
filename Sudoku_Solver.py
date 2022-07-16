# Solution - 45
# Problem Link - https://bit.ly/31Z5Iwe and https://leetcode.com/problems/sudoku-solver/
# Challege Start Date - 04.06.2022
# Date - 16.07.2022
# Day 40
def isvalid(matrix,k,row,col):
    for i in range(0,9):
        if matrix[row][i]==k:
            return False
        elif matrix[i][col]==k:
            return False
        elif matrix[3*(row//3) + i//3][3*(col//3) + i%3]==k: # Each 3*3 grid has 3col 3row 
            return False
    return True
def getsolution(matrix):
    n=len(matrix)
    for i in range(0,n): # Traversing all matrix elements
        for j in range(0,n):
            if matrix[i][j]==0: # If empty spot found
                for k in range(1,10): # Try to fill with 1-9
                    if isvalid(matrix,k,i,j): # Fill if possible
                        matrix[i][j]=k
                        if getsolution(matrix): # Goto next element if that returns true it return true
                            return True
                        else:
                            matrix[i][j]=0 # Else remove added element and try other numbers
                return False     
    return True
def isItSudoku(matrix):

    # Write your code here.
    return(getsolution(matrix))

matrix=[[3, 7, 4, 8, 0, 1, 5, 0, 2],[5, 0, 2, 6, 7, 9, 0, 0, 8],[0,0, 0, 4, 0, 2,0, 6, 0],[7, 0, 0, 1, 0, 6, 0, 8, 4],[8, 6, 0, 0, 0, 0, 2, 9],[4, 1, 0, 0, 5, 3, 0, 0, 0],[1, 4, 9, 0, 3, 8, 0, 0, 0],[0, 2, 0, 0, 0, 7, 3, 0, 0 ],[0, 0, 0, 0, 0, 0, 6, 0, 0]]
print('Yes' if isItSudoku(matrix) else 'No')