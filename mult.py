#A=[[1,2,3],[4,5,6]]
#B=[[7,8],[9,10],[11,12]]

A=[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
B=[[1],[1],[1],[1]]



#A1=[[7,8],[9,10],[11,12]]
#B1=[[1,2,3],[4,5,6]]

#A
mAM=len(A)
mAN=len(A[0])

mBM=len(B)
mBN=len(B[0])


print("A="+str(mAM)+"*"+str(mAN))
print("B="+str(mBM)+"*"+str(mBN))
print(str(mAM)+"*"+str(mBN))

"""
if(mBN==1 and mBM==mAM):
    print("vector")
    C= [[0 for j in range(mBN)] for i in range(mAM)]
else:
    C= [[0 for j in range(mAM)] for i in range(mBN)]
    """

C= [[0 for j in range(mBN)] for i in range(mAM)]
            dotProduct= [[0 for j in range(self.n)] for i in range(other.m)]

print(C)
#print(A[2][1])
#print(B[1][2])


accumulator=0;
for am in range(0,mAM):
    for an in range(0,mAN):
        for bn in range(0,mBN):
            Amatrix="A"+str(am)+""+str(an)+str(",")
            Bmatrix="B"+str(an)+""+str(bn)+str(",")
            Product=str(A[am][an])+"."+str(B[an][bn])
            accumulator=accumulator+1
            C[am][bn]=C[am][bn]+A[am][an]*B[an][bn]
            print(str(accumulator)+",",Amatrix,Bmatrix,Product)

print(C)


accumulator=0;
for am in range(0,mAM):
    for an in range(0,mAN):
        for bn in range(0,mBN):
            Amatrix="A"+str(am)+""+str(an)+str(",")
            Bmatrix="B"+str(an)+""+str(bn)+str(",")
            Product=str(A[am][an])+"."+str(B[an][bn])
            accumulator=accumulator+1
            C[am][bn]=C[am][bn]+A[am][an]*B[an][bn]
            print(str(accumulator)+",",Amatrix,Bmatrix,Product)

print(C)
"""
for i in range(0,2):
    for j in range(0,3):
        for k in range(0,2):
            #print(test1[k][j],"*",test2[j][i])
            dotProduct[i][k]=dotProduct[i][k]+(test1[i][j]*test2[j][k])
        #print(dotProduct)

    def __rmul__(self, other:int):
        return self.escalarMul(other);
        """
        if(type(other)!=type(self)):
        else:
            return self.matrixMul(other)
        """
"""
