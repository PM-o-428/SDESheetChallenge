# Solution - 25
# Problem Link - https://bit.ly/3no44fb & https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Challege Start Date - 04.06.2022
# Date - 04.07.2022
# Day 28
input=input()
count=0
l=0
n=len(input)
dict={}
for r in range(n):
    if input[r] in dict:
        if dict[input[r]]>=l and dict[input[r]]<=r: #If found char within current l,r range
            l=dict[input[r]]+1           # Shift l to immediate right to found char's index
        dict[input[r]]=r                                        # Update found char's index
    else:
        dict.update({input[r]:r})        # Add new char with index
    count=max(count,r-l+1)               # Length of curr substring r-l+1
print(count)