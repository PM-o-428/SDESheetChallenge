mat = [[90]]
target = 90
m=1
n=1
def findTargetInMatrix(mat, m, n, target):
    for i in range(m):
        if mat[0][0]>target: return False
        elif mat[i][n-1]>=target:
            for j in range(n):
                if mat[i][j]==target: return True
            return False
    return False
if(findTargetInMatrix(mat,m,n,target)): print("True")
else: print("False")