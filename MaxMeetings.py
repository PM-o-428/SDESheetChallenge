# Solution - 14
# Problem Link - https://www.codingninjas.com/codestudio/problems/1062658?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
# Challege Start Date - 04.06.2022
# Date - 25.06.2022
# Day 21
start = [4, 1, 5, 7, 9, 6, 7, 2, 1, 8]
end=[14, 11, 18, 10, 19, 19, 14, 18, 7, 16]
dict={}
ans=[]
for i in range(len(start)):
    if start[i] in dict:
        if dict[start[i]][0]>end[i]: # Accessing End time, dict[start[i]]=[end,i] so dict[start[i]][0]=end
            dict.update({start[i]:[end[i],i]}) #Saving the start and end time with the index -> dict{start:[end,endex]}
            
    else:
        dict.update({start[i]:[end[i],i]})
dict_sorted=sorted(dict.items(), key =
            lambda kv:(kv[1], kv[0])) # key is end time
# dict_sorted is sorted by end time so the first element will be the meeting with min end time
limit=dict_sorted[0][1][0] # Adding end time, dict_sorted[0]=[start,[end,index]]
index_=[]
index_.append(dict_sorted[0][1][1]+1) 

for i in range(1,len(dict_sorted)):
    if dict_sorted[i][0]>limit: #If start time of this is greater than end time of prev
        limit=dict_sorted[i][1][0] #setting limit with current added meeting's end time
        index_.append(dict_sorted[i][1][1]+1)
print(index_)
#print(dict_sorted)
#print(dict_sorted[0][1])