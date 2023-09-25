def Bsearch(user_list,s,e,k):
    while(s<e):
        m= int(s+(e-s)/2)
        if user_list[m]==k:
            return m
            break
        elif k > user_list[m]:
            s=m+1
        else:
            e=m-1   

    return -1          
lis=input()
user_list =lis.split()
user_list = [int(item) for item in user_list]
s=0
e=len(user_list)-1
k=3
res=Bsearch(user_list,s,e,k) 
print(res)