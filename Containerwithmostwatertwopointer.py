def Container(arr):
    n=len(arr)
    maxWater=0
    i=0
    j=n-1
    while(i<j):
        ans=(j-i)*min(arr[i],arr[j])
        if ans>maxWater:
            maxWater=ans
        if arr[i]<arr[j]:
            i=i+1
        else:
            j=j-i        
    return maxWater    
lst=[1,5,6,3,4,2]
result=Container(lst)
print(result)