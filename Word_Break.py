# Solution - 47
# Problem Link - https://bit.ly/3FxgW92
# Challege Start Date - 04.06.2022
# Date - 17.07.2022
# Day 41
def findSen(s,dictionary,temp,ans,index):
    if index==len(s):
        ans.append(temp.lstrip())
        return
    for i in range(index,len(s)):
        if s[index:i+1] in dictionary: # If curr string in dict
            copy=temp         # Copy curr temp for backtracking
            temp+=' '+s[index:i+1]   
            findSen(s,dictionary,temp,ans,i+1)
            temp=copy      
def wordBreak(s, dictionary):
    # Write your code here
    temp=''
    ans=[]
    findSen(s,dictionary,temp,ans,0)
    return ans

s='IamPritam'
dictionary={'I','am','Pritam','amPri','tam'}
for i in wordBreak(s, dictionary):
    print(i)