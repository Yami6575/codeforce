n=int(input(''))
a=list(map(int,input().split()))
b=[]
for i in range(n):
    c=[]
    c.append(i+1)
    c.append(a[i])
    b.append(c)
for i in range(n-1):
    for j in range(n-i-1):
        if b[j][1]>b[j+1][1]:
            b[j],b[j+1]=b[j+1],b[j]
            
        
for i in range(n):
    print(b[i][0],end=' ')

    


