# Solution - 40
# Problem Link - https://bit.ly/3HZPNgs & https://leetcode.com/problems/palindrome-partitioning/
# Challege Start Date - 04.06.2022
# Date - 12.07.2022
# Day 36
def isPallndrm(s,start,end):
    while start<=end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True

def func(s,index,temp,ans):
    if index==len(s):
        ans.append([])
        for j in temp:
            ans[len(ans)-1].append(j)
        return
    for i in range(index,len(s)):
        if isPallndrm(s,index,i):
            temp.append(''.join(s[index:i+1])) # Join-part just joins the indexed chars as word
            func(s,i+1,temp,ans)
            temp.pop(len(temp)-1)

s="aabb"
ans=[]
temp=[]
func(s,0,temp,ans)
print(ans)