# Solution - 15
# Problem Link - https://bit.ly/3GsANaD
# Challege Start Date - 04.06.2022
# Date - 28.06.2022
# Day 22
prices=[100,200,5,100]
profit=0
min_ele=prices[0]
for i in range(1,len(prices)):
    if min_ele>prices[i]:
        min_ele=prices[i]
    else:
        temp=prices[i]-min_ele
        if profit<temp:
            profit=temp
print(profit)