import itertools
from sympy import FiniteSet

def reflexive(A,R):
    lst = []
    for x in A:
        if (x,x) not in R:
            lst.append(x)
    if lst == []:
        print("R is reflexive")
    else:
        print("R is not reflexive: ", str(lst))

def symmetric(R):
    lst = []
    for x in R:
        name = list(x)
        name.reverse()
        if tuple(name) not in R:
            lst.append(list(x))
    if lst == []:
        print("R is symmetric")
    else:
        print("R is not symmetric: ", lst[0])

def transitive(R):
    lst = []
    for a,b in R:
       for c,d in R:
           if b == c and (a,d) not in R:
               lst.append([a,b])
               lst.append([c,d])

    if lst == []:
        print("R is transitive")
    else:
        print("R is not transitive: ", str(lst))


import itertools
def func(A,R):
    A =  set(A)
    R = set(R)

    A1 = set(itertools.product(A, repeat=2))
    if R.issubset(A1) == True:
        print("R is a set")
        print("R is a subset of A*A")
        print("R is a relation on A")
        reflexive(A,R)
        symmetric(R)
        transitive(R)
    else:
        lst = []
        for x in R:
            if x not in list(A1):
                lst.append(x)
        print("R is a set")
        print("R is not a subset of A because the following element is in R but not in A*A: ",lst)
        print("R is not a relation on A")



func([1,2,3], [(1,1), (2,3), (3,1), (3,2)])




