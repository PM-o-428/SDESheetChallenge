# Solution - 57
# Problem Link - https://bit.ly/3rkGuBb & https://leetcode.com/problems/roman-to-integer/
# Challege Start Date - 04.06.2022
# Date - 27.07.2022
# Day 51
def romanToInt(s):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ans=roman[s[0]]
    prev=roman[s[0]]
    for i in list(s[1:]):
        if prev<roman[i]:
            ans+=roman[i]-prev*2
        else:
            ans+=roman[i]
        prev=roman[i]
    
    return str(ans)

S=['IXM','XIM','VVL','XXL','XXM','CCML','IX']
for s in S:
    print(s+' = '+romanToInt(s))