def trap(arr):
    lst=[] #empty list for using as stack
    n=len(arr)  #length of array
    trapwater=0 # to return answe
    i=0
    
    while i<n: 
        while lst and arr[i]>arr[lst[-1]]: #till stack is not empty and til cuurent of array is greater than top of stack
            top=lst.pop() #removing top of stack
            if not lst: #if list becomes empty
                break
            length=i-lst[-1]-1 #length of container
            height=min(arr[i],arr[lst[-1]])-arr[top]#height of container
            trapwater=trapwater+length*height 
        lst.append(i)
        i=i+1
    return trapwater            



lst=[9,1,4,0,2,8,6,3,5]
result=trap(lst)
print(result)