# Solution - 7
# Problem Link - https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_1112602?topList=striver-sde-sheet-problems&leftPanelTab=1
# Challege Start Date - 04.06.2022
# Date - 18.06.2022
from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
	# Write your code here.
    if n==0:
        return 1
    elif n%2==0: # If even then divide in two parts
        result = modularExponentiation(x,n//2,m) #Divide and Conquor Algorithm applied
        return (result*result)%m
    else: # IF Odd then (x*x^n-1)%m = ((x%m)*(x^n-1)%m)%m
        return ((x%m)*modularExponentiation(x,n-1,m))%m

# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1