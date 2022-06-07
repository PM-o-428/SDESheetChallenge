# Solution - 1
# https://www.codingninjas.com/codestudio/problems/total-unique-paths_1081470?topList=striver-sde-sheet-problems
# My CP Notes - https://docs.google.com/document/d/1Ts8O7Qyp_z2_D-joURAcGY5kpyg4JJ-YsFkrIJvQF9E/edit?usp=sharing
# Challege Start Date - 04.06.2022
# Date - 07.06.2022

def uniquePaths(m, n):
	# Write your code here.
	direction = n + m - 2
	p = n-1 if n<m else m-1
	ways = 1
	for i in range(1,p+1):
		ways = ways*(direction-p+i)/i
	return int(ways)
