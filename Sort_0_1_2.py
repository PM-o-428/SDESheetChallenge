from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    count_0=0
    count_1=0
    count_2=0
    for i in range(0,n):
        if arr[i]==0: count_0+=1
        elif arr[i]==1: count_1+=1
        elif arr[i]==2: count_2+=1
    for i in range(0,n):
        if i<count_0: arr[i]=0
        elif i<count_0+count_1: arr[i]=1
        elif i<count_0+count_1+count_2: arr[i]=2

#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
