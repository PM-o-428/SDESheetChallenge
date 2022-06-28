# Solution - 16
# Problem Link - https://bit.ly/3rhVUWx
# Challege Start Date - 04.06.2022
# Date - 28.06.2022
# Day 22
def swap(mat,temp,i,j):
    temp_=temp
    temp=mat[i][j]
    mat[i][j]=temp_
    return temp
    
def rotateMatrix(mat, n, m):

    # Write your code here
    iupper=0
    ilower=n-1
    jleft=0
    jright=m-1
    while jleft<jright and iupper<ilower:
        temp=mat[iupper][jleft]
        for j in range(jleft+1,jright+1):
            temp=swap(mat,temp,iupper,j)
        for i in range(iupper+1,ilower+1):
            temp=swap(mat,temp,i,jright)
        for j in range(jright-1,jleft-1,-1):
            temp=swap(mat,temp,ilower,j)
        for i in range(ilower-1,iupper-1,-1):
            temp=swap(mat,temp,i,jleft)
        iupper+=1
        jleft+=1
        jright-=1
        ilower-=1
    print(mat)

n=4
m=4
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(mat)
rotateMatrix(mat,n,m)