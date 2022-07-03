# Solution - 24
# Problem Link - https://bit.ly/3fp24yN & https://www.interviewbit.com/problems/subarray-with-given-xor/
# Challege Start Date - 04.06.2022
# Date - 03.07.2022
# Day 27
arr=[6, 6, 6, 6, 6, 6, 6, 6]
x=6
count=0
xor=0
dict={}
for i in arr:
    xor=xor^i
    if xor==x:
        count+=1
    if xor^x in dict:
        count+=dict[xor^x] #Y=Xor ^ X : If Y is there then how many times Y is found 
                           # for that many times K is also there
    if xor in dict:
        dict[xor]+=1
    else:
        dict.update({xor:1})    
print(count)