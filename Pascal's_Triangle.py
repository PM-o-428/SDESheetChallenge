# Solution - 3
# Problem Link - https://www.codingninjas.com/codestudio/problems/pascal-s-triangle_1089580?topList=striver-sde-sheet-problems&leftPanelTab=1
# Challege Start Date - 04.06.2022
# Date - 12.06.2022
n=int(input())
ans=[]
for i in range(0,n):
    ans.append([]) #IMPORTANT FOR MAKING 2-D LIST
    if i==0: ans[i].append(1)
    elif i==1:
        ans=[[1],[1,1]]
    else:
        for j in range(0,i+1):
            if j==0: ans[i].append(1)
            elif j==i: ans[i].append(1)
            else:
                ans[i].append(ans[i-1][j-1]+ans[i-1][j])
print(ans)