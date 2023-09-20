def trap(arr):
    lst=[]
    n=len(arr)
    trapwater=0
    i=0
    
    while i<n:
        while lst and arr[i]>arr[lst[-1]]:
            top=lst.pop()
            if not lst:
                break
            length=i-lst[-1]-1
            height=min(arr[i],arr[lst[-1]])-arr[top]
            trapwater=trapwater+length*height 
        lst.append(i)
        i=i+1
    return trapwater            



lst=[9,1,4,0,2,8,6,3,5]
result=trap(lst)
print(result)