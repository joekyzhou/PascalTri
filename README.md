# PascalTri
#Pascal Triangle is used in combinatorics to determine the total amount of possible combinations one can make. Ex: Making the number of characters with certain given shapes and/or #specific objects on a movie, cast, show, etc.

def binomial(n,k):
    from numpy import array
    if k==0 or n-k==0:
        print(1)
    elif n<k:
        print('Undefined')
    else:
        f=1
        g=1
        h=1
        for a in range(1,n+1):
            f*=a
        for b in range(1, k+1):
            g*=b
        for c in range(1, n-k+1): 
            if n-k==0:
                h*=1
            else:
                h*=c
        return f/(g*h)
p=int(input('Input the line of pascal:'))
a=[]
k=1
for k in range(p+1):        
    for i in range(k+1):
        if i==0 or i==k:
            a.append(1)
        else:
            a.append(binomial(k,i))
    print(list(map(int,a)))
    k+=1
    a=[]
