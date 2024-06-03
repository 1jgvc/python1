import sys
from itertools import permutations

def valid_hours(numbers:list):
    if(type(numbers) !=type([1,2])): #test like teacher example
        sys.exit("Solo lista de numeros")
    for testNumber in numbers:
        if (testNumber<0 or testNumber>9): sys.exit("fuera de rango")
    perm = permutations(numbers)
    amFormat=False
    maxHours=24
    if(amFormat): maxHours=13

    for tuplePerm in list(perm):
        currentPerm=""
        #tuples to int 
        for currentTuple in tuplePerm:
            currentPerm+=str(currentTuple)

        currentPerm=int(currentPerm)
        b=currentPerm%100
        a=int((currentPerm-b)/100)
        if((a>0 and a<maxHours) and (b>-1 and b<59)): print ( str(a)+":"+str(b))

valid_hours([1, 2, 3,9])
valid_hours("1")
