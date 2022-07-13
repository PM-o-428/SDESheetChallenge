# Solution - 42
# Problem Link - https://bit.ly/3fmwxNV & https://leetcode.com/problems/permutations/
# Challege Start Date - 04.06.2022
# Date - 13.07.2022
# Day 37
def getpermu(s,ans,left,right):
    if left==right:
        ans.append(''.join(s)) # Add ans after all swapping are done
    else:
        for i in range(left,right):
            s[left],s[i] = s[i],s[left] # Swap
            getpermu(s,ans,left+1,right) # Find Permutation in next elements
            s[left],s[i] = s[i],s[left] # BackTrack, Undo Swap
def findPermutations(s):
	# Write your code here.
    ans=[]
    s=list(s)
    getpermu(s,ans,0,len(s))
    return ans

s='123'
print(findPermutations(s))