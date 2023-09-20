def trap(arr):
    n=len(arr)
    l=0
    r=n-1
    ans=0
    lmax=0
    rmax=0
    while(l<r):
        if arr[l]<arr[r]:
            if arr[l]>=lmax:
                lmax=arr[l]
            else:
                ans=ans+lmax-arr[l]
            l=l+1
        else:
            if arr[r]>=rmax:
                rmax=arr[r]
            else:
                ans=ans+rmax-arr[r]
            r=r-1                    
    return ans
lst=[3,0,2,0,4]
result=trap(lst)
print(result)