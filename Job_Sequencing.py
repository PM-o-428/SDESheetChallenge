# Solution - 32
# Problem Link - https://bit.ly/3K9XZfV
# Challege Start Date - 04.06.2022
# Date - 08.07.2022
# Day 32
# O(N*M)+O(NlogN)

def comparator(e):
    return e[1]
def jobScheduling(jobs):

    # Write your code here
    # Return an integer denoting the maximum pofit  
    maxDays=max(jobs)[0]
    jobs.sort(reverse=True,key=comparator)
    profit=0
    dayMap=[-1]*(maxDays+1)
    for i in range(len(jobs)):
        if dayMap[jobs[i][0]]==-1:
            profit+=jobs[i][1]
            dayMap[jobs[i][0]]=i
        else:
            j=jobs[i][0]
            while dayMap[j]!=-1 and j>0:
                j-=1
            if j!=0:
                profit+=jobs[i][1]
                dayMap[j]=i
    return profit

jobs=[[2,40],[2,20],[1,10]]
print(jobScheduling(jobs))