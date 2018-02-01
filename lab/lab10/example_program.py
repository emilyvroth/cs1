""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""
import random
import time


def addone(x):
    '''
    addone(x) returns 1 more than
    the value x passed in.

    >>> addone(1)
    2
    >>> addone(0)
    1
    '''
    return x+1

def closest1(L):
    '''
    closest1(L) returns a tuples of the 
    two closest points in a list using double for loops.

    >>> closest1([5,8,8.1,8.15,5.5,70])
    (8.1, 8.15)
    >>> closest1([5,1])
    (None, None)
    >>> closest1([15.1,-12.1,5.4,11.8,17.4,4.3,6.9])
    (5.4, 4.3)
    '''
    dif=1000
    if len(L)>2:
        for i in L:
            for j in L:
                if  i != j:
                    if abs(i-j)<dif:
                        dif=abs(i-j)
                        tup=(i, j)
        return tup
    return (None, None)


def closest2(L):
    '''
    closest2(L) returns a tuples of the 
    two closest points in a list using sorting.

    >>> closest1([5,8,8.1,8.15,5.5,70])
    (8.1, 8.15)
    >>> closest1([5,1])
    (None, None)
    >>> closest1([15.1,-12.1,5.4,11.8,17.4,4.3,6.9])
    (5.4, 4.3)
    '''
    copy=L[:]
    copy.sort()
    dif=1000
    for i in range(len(copy)-1):
        if abs(copy[i]-copy[i+1])<dif:
            dif=abs(copy[i]-copy[i+1])
            tup=(copy[i], copy[i+1])
    return tup


if __name__ == "__main__":
    
    L1=[]
    for i in range(0,100):
        L1.append(random.uniform(0.0,1000.0))

    L2=[]
    for i in range(0,1000):
        L2.append(random.uniform(0.0,1000.0))

    L3=[]
    for i in range(0,10000):
        L3.append(random.uniform(0.0,1000.0))    

    t1=time.time()
    closest1(L1) 
    t2=time.time()
    closest1(L2)
    t3=time.time()
    closest1(L3)
    t4=time.time()

    closest2(L1) 
    t5=time.time()
    closest2(L2)
    t6=time.time()
    closest2(L3)
    t7=time.time()

    print("time for method 1 on a list of len 100: ",t2-t1)
    print("time for method 2 on a list of len 100: ",t5-t4)
    print("time for method 1 on a list of len 1000: ",t3-t2)
    print("time for method 2 on a list of len 1000: ",t6-t5)
    print("time for method 1 on a list of len 10,000: ",t4-t3)
    print("time for method 2 on a list of len 10,000: ",t7-t6)