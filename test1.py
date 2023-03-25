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
        return 0
    if length%2 == 1:
        return array[length//2] #Length being odd
    else:
        median = (array[length//2 -1] + array[length//2])*0.5 #Length being even
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
    return result
    
if __name__ == "__main__":
    print("Enter List Separated by comma")
    ina=input().split(',')
    ina=[int(x) for x in ina]
    k=int(input("Enter size of Sliding Window\n"))
    res=window(ina, k)
    print("Output:\t{0}".format(res))
