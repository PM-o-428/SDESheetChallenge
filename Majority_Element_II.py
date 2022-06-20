# Solution - 9
# Problem Link - https://www.codingninjas.com/codestudio/problems/majority-element-ii_893027?topList=striver-sde-sheet-problems&leftPanelTab=0
# Challege Start Date - 04.06.2022
# Date - 20.06.2022
arr = [20,20, 20, 4, 5, 4, 1, 4, 4, 20 ]
dict={} #Using Hash Maps
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict.update({i:1})
max_ele=[]
for i in dict:
    if dict[i]>(len(arr)//3): max_ele.append(i)
print(max_ele,sep=' ')