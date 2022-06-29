#Solution - 2(Optimal) (O(n))
#Dutch National Flag Algorithm
# https://bit.ly/3tlM60B
# Challege Start Date - 04.06.2022
# Date - 29.06.2022
arr=[1,1,0,2,0,2,1,1,0,0]
low=0
mid=0
high=len(arr)-1

def swap(arr,i,j):
    temp=arr[j]
    arr[j]=arr[i]
    arr[i]=temp
while(mid<=high):
    if arr[mid]==0:
        swap(arr,mid,low)
        mid+=1
        low+=1
    elif arr[mid]==1:
        mid+=1
    elif arr[mid]==2:
        swap(arr,mid,high)
        high-=1
print(arr)