# Solution - 35
# Problem Link - https://bit.ly/3I2iPvN
# Challege Start Date - 04.06.2022
# Date - 10.07.2022
# Day 34
# Same as MaxMeetings

def maximumActivities(start, finish):
    # Write your Code here.
    activities=1 # Starting from 2nd index so counter is set to 1
    dict={}
    for i in range(len(start)):
        if start[i] in dict:
            if finish[i]<dict[start[i]][0]:
                dict[start[i]][0]=finish[i]
        else:
            dict.update({start[i]:[finish[i],i]})
    dict_sorted=sorted(dict.items(), key =
            lambda kv:(kv[1], kv[0]))
    
    limit=dict_sorted[0][1][0]
    
    for i in range(1,len(dict_sorted)):
        if dict_sorted[i][0]>=limit:
            limit=dict_sorted[i][1][0]
            activities+=1
            
    return activities

start=[1, 3, 2, 5]
finish=[2, 4, 3, 6]
print(maximumActivities(start,finish))