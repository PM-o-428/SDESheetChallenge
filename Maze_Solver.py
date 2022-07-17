# Solution - 46
# Problem Link - https://bit.ly/3fmwP7t
# Challege Start Date - 04.06.2022
# Date - 17.07.2022
# Day 41
def findways(maze,flag,ans,temp,row,col,dR,dC):
    if row==n-1 and col==n-1:
        if maze[row][col]!=0:
            ans.append([])
            ans[len(ans)-1]=[0]*(n*n)
            ans[len(ans)-1][0]=1
            for i in temp:
                ans[len(ans)-1][i[0]*n + i[1]]=1
            return
        else:
            return
    for i in range(4): # 4 Directions
        next_row=row+dR[i]
        next_col=col+dC[i]
        if next_row<n and next_row>=0 and next_col<n and next_col>=0 and maze[next_row][next_col]==1 and flag[row][col]==0:
            temp.append([])
            flag[row][col]=1
            temp[len(temp)-1].append(next_row)
            temp[len(temp)-1].append(next_col)
            findways(maze,flag,ans,temp,next_row,next_col,dR,dC)
            temp.pop(len(temp)-1)
            flag[row][col]=0
    return
def ratInAMaze(maze, n):
    # Write your code here.
    ans=[]
    temp=[]
    flag=[]
    dR=[0,1,-1,0] # dR[0] dC[0] = move RIGHT dR[2] dC[2] = move UP
    dC=[1,0,0,-1]
    for i in range(n):
        flag.append([])
        flag[i]=[0]*n
    findways(maze,flag,ans,temp,0,0,dR,dC)
    # Printing ans 2-D list as string
    s=''
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            s=s+' '+str(ans[i][j])
        print(s.lstrip())
        s=''
    return

# Main.
n = int(input())
maze = n*[0]

for i in range(0 , n):
    maze[i]=input().split()
    maze[i]=[int(j) for j in maze[i]]
    
ratInAMaze(maze,n)