# Solution - 74
# Problem Link - https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find_the_number_of_islands
# Challege Start Date - 04.06.2022
# Date - 27.09.2022
# Day 113
class Solution:
    def bfs(self,row,col,grid,vis): # BFS in a Matrix
        rows = len(grid)
        cols = len(grid[0])
        vis[row][col] = 1
        dict = []
        dict.append([row,col]) # Append current node location
        
        while len(dict): # Iterate all stored nodes by poping one by one
            row = dict[0][0]
            col = dict[0][1]
            dict.pop(0)

            # Logic to find all neighbor nodes
            for delrow in [-1,0,1]:
                for delcol in [-1,0,1]:
                    nrow = row + delrow
                    ncol = col + delcol
                    # If not visited and Land found
                    if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols and vis[nrow][ncol]==0 and grid[nrow][ncol]==1:
                        vis[nrow][ncol]=1 # Mark visited
                        dict.append([nrow,ncol]) # Append location for next level search
                        
    def numIslands(self,grid):
        #code here
        islands=0
        rows = len(grid)
        cols = len(grid[0])
        vis = [[0 for _ in range(cols)] for _ in range(rows)] # Visited Matrix with all 0 elements
        for row in range(rows):
            for col in range(cols):
                if vis[row][col]!=1 and grid[row][col]==1: # If not visited and land found
                    self.bfs(row,col,grid,vis) # BFS will traverse all connected Nodes
                    islands+=1
        return islands

n,m = map(int, input().split())
grid = []
for i in range(n):
    grid.append([int(j) for j in input().split()])
obj = Solution()
print(obj.numIslands(grid))