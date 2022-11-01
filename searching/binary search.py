def binary(x,a):
    low=0
    high=len(a)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if a[mid]==x:
            return mid
        elif a[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
a=[21,3,5,7,9,10,11]
x=7
result=binary(x,a)
if result==-1:
    print("not found")
else:
    print("index",result)