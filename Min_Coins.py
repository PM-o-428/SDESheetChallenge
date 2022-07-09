# Solution - 34
# Problem Link - https://www.codingninjas.com/codestudio/problems/find-minimum-number-of-coins_975277?topList=striver-sde-sheet-problems
# Challege Start Date - 04.06.2022
# Date - 09.07.2022
# Day 33

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

def findMinimumCoins(amount):

	# Write your code here
    coins=0
    which_coins=[]
    for i in range(len(denominations)-1,-1,-1):
        if amount==0: break
        coins+=amount//denominations[i]
        if amount//denominations[i]>0:
            which_coins.append(denominations[i])
        amount=amount%denominations[i]
    return coins,which_coins

amount=int(input())

print(findMinimumCoins(amount))