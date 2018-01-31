r=int(input())
for i in range(r):
    s=input()
    flag=1
    x=[]
    for j in s:
        if j=='T' and len(x)==0:
            flag=0
            break
        if j=='H':
            x.append(j)
        if j=='T':
            x.append(j)
    for k in range(len(x)-1):
        if x[k]==x[k+1]:
            flag=0
            break
    if flag==0:
        print("Invalid")
    else:
        print("valid")