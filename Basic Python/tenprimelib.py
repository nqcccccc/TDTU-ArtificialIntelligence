"""
Name: tenprimelib.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 20/09/2021 10:49
Desc:
"""
import math

def tenPrime(n):
    count = 0
    i = n
    a = []
    while(count < 10):
        if i > 1:
            for j in range(2, int(i)):
                if i % j == 0:
                    break
            else:
                a.append(i)
                print(i, end=' ')
                count +=1
        i = i +1

    return a
