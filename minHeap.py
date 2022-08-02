# Solution - 63
# Problem Link - https://www.codingninjas.com/codestudio/problems/min-heap_4691801?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
# Challege Start Date - 04.06.2022
# Date - 02.08.2022
# Day 57

# Implement MinHeap
  
class MinHeap:
  
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * maxsize
        self.FRONT = 1
  
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2
  
    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos
  
    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
  
    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return pos*2 > self.size
  
    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
  
    # Function to heapify the node at pos
    def minHeapify(self, pos):
  
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):
  
                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
  
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
  
    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
  
        current = self.size
  
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
  
  
    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
  
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
  
    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
  
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped
def minHeap(Q):

    # Write your code from here.
    ans=[]
    minHeap = MinHeap(10**5)
    for i in Q:
        if i[0]==0:
            minHeap.insert(i[1])
        elif i[0]==1:
            ans.append(minHeap.remove())
    return ans

# '1'->Remove the root and return
# '0 X' -> Insert 'X' in the Heap in appropriate place
Q=[[0,6],[0,9],[0,8],[1],[0,5],[0,6],[1],[0,78],[0,65],[0,85],[1]]
print(minHeap(Q))