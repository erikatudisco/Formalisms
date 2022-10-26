#!/usr/bin/env python

def fib(nterms):
    # check if nterms is lower than zero
    if nterms <= 0:
        print('choose a larger number')
        return
    # check if neterms is 1
    elif nterms==1: 
        result=1
    # check if nterms is 2
    elif nterms==2:
        result=1
    else:
        result= fib(nterms-1)+fib(nterms-2)
    return result

for i in range(1,15):
    print(fib(i))
