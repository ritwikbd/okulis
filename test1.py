# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:29:59 2023

@author: ritwi
"""

def median(array):
    #Returns the median of any list
    length=len(array)
    array=sorted(array)
    if length == 0:
        return 'NA'
    if length%2 == 1:
        return array[length//2] #Length being odd
    else:
        median = (array[length//2 -1] + array[length//2])*0.5 #Length being odd
        return median
    
def window(superset,k):
    #Returns the median of each window
    length=len(superset)
    start=0
    result=[]
    while start<=length-k:
        subset=superset[start:start+k] #Sliding Window
        med=median(subset)
        start=start+1
        result.append(float(med)) #Typecasting to float for uniformity in case of odd and even values of k
    print(result)
    
#window([1,3,-1,-3,5,3,6,7],3)