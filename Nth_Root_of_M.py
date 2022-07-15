# Solution - 43
# Problem Link - https://bit.ly/3rj7Ib1
# Challege Start Date - 04.06.2022
# Date - 14.07.2022
# Day 38
m=int(input())
n=int(input())
# Answer with Exponential function
ans="{:.6f}".format(m**(1/n))

# Calculating with Binary Search - TC-> n*log2(m*10^d) d=how many decimal places are required
def getNthSq(mid,t):
    ans=1.0
    while t>0:
        ans*=mid
        t-=1
    return ans
eps=1e-7 # Will get Precision upto 6digit
high=m
low=1
while(high-low>eps):
    mid = (high+low)/2.0
    mid_n = getNthSq(mid,n)
    if mid_n<m:
        low=mid
    else:
        high=mid                 # low and high is same after while ends upto 6digit after point
print("{:.6f}".format(low)==ans) # Check If binary search ans matches builtin function ans