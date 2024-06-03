#import sys
#import random

def printPatterns(pattern:int,patterLength:int):
    if(patterLength<4): sys.exit("n>=4")
    if(patterLength>60): patterLength=60

    info=("pattern: "+str(pattern)+", length="+str(patterLength))
    print(info)
    match pattern:
        case 1:
            for i in range(1,patterLength*2):
                print("*"*i)
        case 2:
            #for i in range(0,patterLength): #first i saw it as ladder...
            for i in range(0,2): #is a square
                for j in range(0,patterLength):
                    print((" "*(i*patterLength)) + ("+"*patterLength))
        case 3:
            """
            maxPatternLegth=n;
            """
            patternTop=[];
            for blanks in range(0,patterLength):
                patternReps=patterLength-(blanks)
                leftSide=("o"*patternReps)+(" "*(patterLength-patternReps))
                rightSide=(" "*(patterLength-patternReps))+("o"*patternReps)
                
                patternTop.append(leftSide+rightSide);
                print(leftSide+rightSide)
            for bottomLines in reversed(patternTop):
                print(bottomLines)



printPatterns(1,60)
printPatterns(3,15)
"""
#printPatterns(2,random.randint(4, 10))
printPatterns(3,10)
totalArgs=len(sys.argv)-1;
print("Total args="+str(totalArgs))
if(totalArgs==1):
    printPatterns(sys.argv[1] ,random.randint(4, 10))
elif (totalArgs==2):
    printPatterns(sys.argv[1] ,sys.argv[2])
else:
    printPatterns(random.randint(1, 3),random.randint(4, 10))


for balls in range(patterLength,0,-1):
    topLeftSide=("o"*balls)+((" ")*(patterLength-balls))
    topRightSide=((" ")*(patterLength-balls))+("o"*balls)
    patternTop.append(topLeftSide+topRightSide);
    print(topLeftSide+topRightSide)
"""
