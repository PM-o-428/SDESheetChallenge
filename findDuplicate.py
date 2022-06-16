# Solution - 5
# Problem Link - https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_1112602?topList=striver-sde-sheet-problems&leftPanelTab=1
# Challege Start Date - 04.06.2022
# Date - 16.06.2022
arr =list(map(int,input().split()))
arr.sort()
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]: print(arr[i])