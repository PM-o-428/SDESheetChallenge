# Solution - 36
# Problem Link - https://www.codingninjas.com/codestudio/problems/subset-sum_3843086?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
# Challege Start Date - 04.06.2022
# Date - 10.07.2022
# Day 34
sums=[]
def subsetSum(num,index,sum,sums):
    # Write your code here.
    if index==n:
        sums.append(sum)
        return
    # Pick
    subsetSum(num,index+1,sum+num[index],sums)
    # Not Pick
    subsetSum(num,index+1,sum,sums)

num=[27, 11, 21, 28]
n=len(num)

subsetSum(num,0,0,sums)
sums.sort()
print(sums)