def func(arr,index,ans,temp,k):
    if k==0:
        ans.append([])
        for j in temp:
            ans[len(ans)-1].append(j)
    if index>=len(arr):
        return
    # Pick
    for i in range(index,len(arr)):
        if i!=index and arr[i]==arr[i-1]: # Check for duplicate element
            continue
        temp.append(arr[i])     #Append Curr element
        func(arr,i+1,ans,temp,k-arr[i])  # Start Recursion for updating ans & adding next elements in the next subset
        temp.pop(len(temp)-1)

arr=[1, 4, 1, 3, 4, 4, 3, 3, 2]
arr.sort()
k=11
ans=[]
temp=[]
func(arr,0,ans,temp,k)
print(ans)