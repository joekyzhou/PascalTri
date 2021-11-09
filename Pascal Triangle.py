# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:04:18 2021

@author: joeky
"""
#Pascal Triangle Properties
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
"""
def Hockeystick(k,r,n):
    from numpy import math*
"""    
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
    