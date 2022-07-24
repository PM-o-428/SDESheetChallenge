# Solution - 54
# Problem Link - https://bit.ly/3zV52ob
# Challege Start Date - 04.06.2022
# Date - 24.07.2022
# Day 48
def canPlace(positions,c,minimum):
    count=1 # Currently Placed Players
    curr_pos=positions[0] # Current Player's Position
    for i in positions[1:]:
        if i-curr_pos>=minimum: # Place next player in next pos and check if this exceeds minimum
            count+=1 # Increase Players placed
            curr_pos=i # Update Position
        if count==c: # If All players placed 
            return True
    return False
def chessTournament(positions, n , c):
    result=0
    positions.sort() # Sort the Array of Positions
    low = 0
    high = positions[n-1]-positions[0] # Highest Difference possible
    while low<=high:
        mid=(low+high)//2 # Checking if all players can be placed by this Difference 
        if canPlace(positions,c,mid): 
            result=mid # This difference can be my ans
            low=mid+1 # Check for greater diffs
        else:
            high=mid-1 # Check for lower Diffs
    return result
positions=[1,4,6,7,9,14]
n=len(positions)
c=4
print(chessTournament(positions,n,c))