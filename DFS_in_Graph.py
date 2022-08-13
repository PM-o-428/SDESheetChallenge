# Solution - 75
# Problem Link - https://bit.ly/33BcXeg & https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
# Challege Start Date - 04.06.2022
# Date - 13.08.2022
# Day 68

# DFS using adjacency list and Recursion
class Solution:
    def dfs(self,node,adj,vis,dfs_path):
        vis[node]=1
        dfs_path.append(node)
        for i in adj[node]:
            if vis[i]!=1:
                self.dfs(i,adj,vis,dfs_path)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        start=0
        vis=[0]*V
        dfs_path=[]
        self.dfs(start,adj,vis,dfs_path)
        return dfs_path


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends

# DFS after converting given path Matrix to adj list
from collections import defaultdict

def graphImplementation(edges):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph
def dfs(node,graph,lis,visited): # Recursion to traverse in Depth
    lis.append(node)
    visited[node] = 1
    for vertex in graph[node]:
        if visited[vertex] != 1:
            dfs(vertex,graph,lis,visited)

def depthFirstSearch(V, E, edges):
    graph = graphImplementation(edges)
    dfs_path = []
    visited = [0 for i in range(V)] # CHecking Each Node as it is disconnected Graph
    for i in range(V):
        lis = []
        if visited[i] != 1:
            dfs(i,graph,lis,visited)
            dfs_path.append(sorted(lis))
    return dfs_path