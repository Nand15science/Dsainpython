def Incresedecrease(arr,s,e):
    if(s==e):
        return arr[low]
    if(e==s+1) and arr[s]>=arr[e]:
        return arr[s]
    if(e==s+1) and arr[s]<arr[e]:
        return arr[e]
    
    m=int(s+(e-s)/2)
    if arr[m]>arr[m+1] and arr[m]>arr[m-1]:
        return arr[m] #if we get in on middle then return that
    if arr[m]>arr[m-1] and arr[m]<arr[m+1]:
        return Incresedecrease(user_list,m+1,e) #if the middle is less than arr[i+1] and the middle is greater than arr[i-1]
    else:
        return Incresedecrease(user_list,s,m-1)

lst=input()
user_list=lst.split()
user_list=[int(item) for item in user_list]
s=0
e=len(user_list)-1
res=Incresedecrease(user_list,s,e)
print(res)


