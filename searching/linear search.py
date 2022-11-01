def Selection(x):
    list=[]
    if not x:
        return x
    else:
        minVal=min(x)
        list.append(minVal)
        x.remove(minVal)
    return list+Selection(x)
x=list(map(int,input().split()))
print(Selection(x))