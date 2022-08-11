# Solution - 73
# Problem Link - https://bit.ly/3rgb26U & https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
# Challege Start Date - 04.06.2022
# Date - 11.08.2022
# Day 66
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        vis=[0]*V
        queue = []
        queue.append(0) # For first Node
        front=0
        while front<len(queue): # Take element from queue untill its empty
            for node in adj[queue[front]]: # Take Nodes from adj list for connected to curr Node 
                if vis[node]!=1:
                    queue.append(node)
                    vis[node]=1
            front+=1
        return queue

#{ 
 # Driver Code Starts

V, E = map(int, input().split())
adj = [[] for i in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
ob = Solution()
ans = ob.bfsOfGraph(V, adj)
for i in range(len(ans)):
    print(ans[i], end = " ")
print()
# } Driver Code Ends