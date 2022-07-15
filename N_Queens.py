# Solution - 44
# Problem Link - https://bit.ly/3zSZavC and https://leetcode.com/problems/n-queens/
# Challege Start Date - 04.06.2022
# Date - 15.07.2022
# Day 39
# Hard
def putqueens(n,ans,temp,leftRow,lowerD,upperD,col):
    if col==n:
        ans.append([])
        ans[len(ans)-1]=[0]*(n*n)
        for i in temp:
            ans[len(ans)-1][i]=1
        return
    for row in range(0,n):
        if leftRow[row]==0 and lowerD[row+col]==0 and upperD[n-1+col-row]==0:
            temp.append(row*n+col) # If the position is not getting attacked
            leftRow[row]=1      # Set Positions in attack by curr Queen
            lowerD[row+col]=1
            upperD[n-1+col-row]=1
            putqueens(n,ans,temp,leftRow,lowerD,upperD,col+1)
            temp.pop(len(temp)-1)
            leftRow[row]=0
            lowerD[row+col]=0
            upperD[n-1+col-row]=0
def solveNQueens(n):
    # Write your code here.
    ans=[]
    temp=[] # n values, storing index of ans which should be 1
    leftRow=[0]*n  # IF Queens in the same row at left is present - Check Hash
    lowerD=[0]*(2*n-1) # Check Hash in Lower diagonal
    upperD=[0]*(2*n-1) # Check Hash in Upper Diagonal
    putqueens(n,ans,temp,leftRow,lowerD,upperD,0)
    return (ans)

n=4
print(solveNQueens(n))