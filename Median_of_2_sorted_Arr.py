# Solution - 51
# Problem Link - https://bit.ly/3Ka3jQr & https://leetcode.com/problems/median-of-two-sorted-arrays/
# Challege Start Date - 04.06.2022
# Date - 21.07.2022
# Day 45
def median(a, b):
    if len(a)>len(b):
            return median(b,a)
    low=0
    high=len(a)
    while(low<=high):
        mid=(low+high)//2
        cut1=mid # 1st cut for taking elements from array 1
        cut2=(len(a)+len(b)+1)//2 - cut1 # Taking remaining elements of left half from the array 2
        l1=a[cut1-1] if cut1>0 else -10 # Last element of truncated arr1 is the max one
        l2=b[cut2-1] if cut2>0 else -10 # Same as above
        r1=a[cut1] if cut1<len(a) else int(1e9 + 10) # First ele of remaining arr1 is the min one
        r2=b[cut2] if cut2<len(b) else int(1e9 + 10)
        if l1<=r2 and l2<=r1:
            if (len(a)+len(b))%2==0: # If the total array is of even size
                return "{:.1f}".format((max(l1,l2)+min(r1,r2))/2.0)
            else: # If the array is odd
                return "{:.1f}".format(float(max(l1,l2)))
        elif l1>r2:
            high=mid-1 # l1 is > so reduce 1st half of arr1 and take from arr2
        else:
            low=mid+1 # l2 is > so reduce 2nd half of arr2 and take from arr1
    return 0.0

a=[2]
b=[]
print(median(a,b))