# Solution - 17
# Problem Link - https://bit.ly/3rj9LvO
# Challege Start Date - 04.06.2022
# Date - 29.06.2022
# Day 23
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    # Write your code here.
    n=len(intervals)
    i=0
    if n==1: return intervals
    while i<n:
        if i==0:
            if intervals[i].end>=intervals[i+1].start:
                intervals[i].end=intervals[i+1].end
                intervals.pop(i+1)
                n-=1
                i+=1
            else:
                i+=1
        else:
            if intervals[i-1].end>=intervals[i].start:
                intervals[i-1].end=intervals[i].end
                intervals.pop(i)
                n-=1
            else:
                i+=1
    return intervals
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)

