# Solution - 31
# Problem Link - https://bit.ly/3npx0mW
# Challege Start Date - 04.06.2022
# Date - 08.07.2022
# Day 32
# O(2N)+O(NlogN)

arr=[775, 494, 252, 1680]
dep=[2052, 2254, 1395, 2130]
n=len(arr)
arr.sort()
dep.sort() # Particular train's arr dep time doesn't matter, so sorting...
Max_plats=0
plats=0
i=0
j=0
while i<n and j<n:
    if arr[i]<=dep[j]: # IF plat is not empty increase one plat
        plats+=1
        i+=1
    else:              # If Plat is empty reduce plat needed by one
        plats-=1
        j+=1
    Max_plats=max(Max_plats,plats)
print(Max_plats)