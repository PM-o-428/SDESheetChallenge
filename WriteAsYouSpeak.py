# Solution - 65
# Problem Link - https://bit.ly/3K8Uwyi
# Challege Start Date - 04.06.2022
# Date - 04.08.2022
# Day 59
def findseq(n,ans):
    if n<2:
        return ans
    else:
        i=0
        temp=''
        while i<len(ans):
            count=1
            while i+1<len(ans) and ans[i]==ans[i+1]:
                i+=1
                count+=1
            temp=temp+str(count)+str(ans[i])
            i+=1
        return findseq(n-1,temp)
def writeAsYouSpeak(n):
    # Write your code here.
    ans='1'
    if n==1:
        return ans
    return findseq(n,ans)

n=4
print(writeAsYouSpeak(n))