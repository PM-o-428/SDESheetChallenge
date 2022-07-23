# Solution - 53
# Problem Link - https://bit.ly/3FrKxk7
# Challege Start Date - 04.06.2022
# Date - 23.07.2022
# Day 47
def isAllocationPossible(time,barrier,n):
    countDays=1
    seconds=0
    for i in range(len(time)):
        if time[i]>barrier: return False # If curr subject's pages > limit
        if seconds+time[i]>barrier:
            countDays+=1
            seconds=time[i]
        else:
            seconds+=time[i]
        if countDays>n: return False # If we cannot allocate all subjects in given days with given barrier
    return True
def ayushGivesNinjatest(n,time):
    # Write your code here.
    low = min(time) # low & high is min seconds of subject & high is sum of total subject's seconds
    high = sum(time)
    result=0
    while low<=high:
        mid=(low+high)//2 # This is the barrier 
        if isAllocationPossible(time,mid,n): # If We can allocate subjects to each days w.o. crossing the barrier
            result=mid # Now mid might be the answer
            high=mid-1 # Reduce Search space and barrier as current barrier allocates successfully
        else:
            low=mid+1 # Increase barrier as curr barrier failed
    return result 

time=[2, 2, 3, 3, 4, 4, 1]
n=4
print(ayushGivesNinjatest(n,time))