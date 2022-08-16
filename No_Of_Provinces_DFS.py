# Graph Practice - 1
# Problem Link - https://practice.geeksforgeeks.org/problems/number-of-provinces/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number_of_provinces
# Challege Start Date - 04.06.2022
# Date - 16.08.2022
# Day 71
class Solution:
    def dfs(self,start,vis,adj):
        vis[start]=1
        for i in range(len(adj[start])):
            if adj[start][i]==1:
                if vis[i]!=1:
                    self.dfs(i,vis,adj)
    def numProvinces(self, adj, V):
        # code here 
        count=0
        vis = [0]*V
        for i in range(V):
            if vis[i]!=1:
                self.dfs(i,vis,adj)
                count+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends

# Codestudio Approach
