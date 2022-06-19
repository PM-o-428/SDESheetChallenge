# Solution - 8
# Problem Link - https://www.codingninjas.com/codestudio/problems/majority-element_842495?topList=striver-sde-sheet-problems&leftPanelTab=0
# Challege Start Date - 04.06.2022
# Date - 19.06.2022
arr = [20,20, 20, 4, 5, 20, 1, 20, 4, 20 ]
dict={} #Using Hash Maps
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict.update({i:1})
max_ele=-1
got_max=max(dict,key=dict.get) #Getting Key with maximum value
if dict[got_max]>(len(arr)//2): max_ele=got_max      
print(max_ele)