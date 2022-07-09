# Solution - 33
# Problem Link - https://bit.ly/3I7fNXn
# Challege Start Date - 04.06.2022
# Date - 09.07.2022
# Day 33
# O(N)+O(NlogN)
def comparator(e):
    return e[1]/e[0]
def maximumValue(items, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
    items.sort(reverse=True,key=comparator)
    max_values=0
    i=0
    while w>0 and i<len(items):
        if items[i][0]<=w:
            w-=items[i][0]
            max_values+=items[i][1]
        else:
            max_values+=(items[i][1]/items[i][0])*w
            w=0
        i+=1
    return max_values

items=[[1,26],[5, 57],[82,5],[2,90],[26,70],[26,45]]
w=100
print('%.2f'%maximumValue(items,w))