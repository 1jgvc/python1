#import sys
#from itertools import permutations
import copy

class Matriz:
    printMessages=True;
    def __init__(self, m=1,n=1, initStyle=""):
        self.m = m
        self.n = n
        #self.maxDigits = 3
        self.vertical = m>n
        self.initStyle = initStyle
        self.isSquare=(m==n)
        self.matrix=self.initList()
        if(self.initStyle=="diag"):
            self.matrix=self.diagonal()


    def listToMatrix(self, listMatrix):
        tmpNew =Matriz(len(listMatrix),len(listMatrix[0]),"");
        tmpNew.matrix=copy.deepcopy(listMatrix)
        return tmpNew

    def initList(self):
        if(self.initStyle=="unos"): val=1
        else: val=0
        return [[val for j in range(self.n)] for i in range(self.m)]

    def diagonal(self):
        if(self.isSquare==False):
            raise Exception("No es una matriz cuadrada = identidad")
            return False

        #slope= round(self.n/self.m)
        for i in range(0,self.m):
            self.matrix[i][i]=1
        return self.matrix;

    def __str__(self):
        matrixStr="\n"
        if(self.printMessages): matrixStr=self.concatSrtExpr()+"\n--------------\n"
        for i in range(0,self.m):
            for j in range(0,self.n):
                #ideally max int should set center parameter....
                matrixStr=matrixStr+str(self.matrix[i][j]).center(4)
            matrixStr=matrixStr+"\n"
        return matrixStr

    def __rmul__(self, other:int):
        if(type(other)==type(1)): return self.escalarMul(other);
        """
        if(type(other)!=type(self)):
        else:
            return self.matrixMul(other)
        """
    def __mul__(self, other):
        if(type(other)!=type(self)):
            return self.escalarMul(other);
        else:
            return self.matrixMul(other)

    def escalarMul(self, escalar):
        tmp=self.listToMatrix(self.matrix)
        for i in range(0,self.m):
            for j in range(0,self.n):
                tmp.matrix[i][j]=escalar*tmp.matrix[i][j]
        if(self.printMessages): print("Escalar multiplication *"+str(escalar))
        return tmp

    def matrixMul(self, other):
        if(other.n==self.m):
            if(self.printMessages):print("Matrix multiplication")
            #accumulator=0;
            dotProduct= [[0 for j in range(self.n)] for i in range(other.m)]
            for am in range(0,other.m):#//mAM
                for an in range(0,other.n):#//mAN
                    for bn in range(0,self.n):#mBN
                        #Amatrix="A"+str(am)+""+str(an)+str(",")
                        #Bmatrix="B"+str(an)+""+str(bn)+str(",")
                        #Product=str(A[am][an])+"."+str(B[an][bn])
                        #accumulator=accumulator+1
                        dotProduct[am][bn]=dotProduct[am][bn]+self.matrix[an][bn]*other.matrix[am][an]
                        #print(str(accumulator)+",",Amatrix,Bmatrix,Product)
            tmp=self.listToMatrix(dotProduct)
            return tmp
        else:
            #raise Exception("ColumnsA  !=  RowsB")
            return "Can't process dot product:"+self.concatSrtExpr()+"*"+self.concatSrtExpr(other)


    def __add__(self, other):
        if(self.n==other.n and self.m==other.m):
            if(self.printMessages):print("Matrix addition")
            tmp=self.listToMatrix(other.matrix)
            for i in range(0,self.m):
                for j in range(0,self.n):
                    tmp.matrix[i][j]=tmp.matrix[i][j]+other.matrix[i][j]
            return tmp
        else:
            #raise Exception("Can't add different dimensions")
            return "Can't add different dimensions"

    def quitaFila(self,rowNo):
        RowIdx=(int(abs(rowNo)))-1
        if(self.printMessages):print("Quita fila="+str(rowNo));
        if(self.m< RowIdx): return "Fila fuera de rango"
        del self.matrix[RowIdx]
        self.m=self.m-1
        return self 

    def quitaColumna(self,ColNo):
        ColIdx=int(abs(ColNo))-1
        if(self.printMessages):print("Quita columna="+str(ColNo))
        if(self.n< ColIdx): return "Columna fuera de rango"
        for i in range(0,self.m):
            del self.matrix[i][ColIdx]
        self.n=self.n-1
        return self
    def concatSrtExpr(self,other=""):
        if(other==""):
            return(str(self.m)+"x"+str(self.n))
        else:
            return(str(other.m)+"x"+str(other.n))


test1=[[1,2,3],[4,5,6]]
test2=[[7,8],[9,10],[11,12]]
m0=Matriz(5,5,"diag");
mt=Matriz(5,3,"");
m1=mt.listToMatrix(test1)
m2=mt.listToMatrix(test2)
m3=mt.listToMatrix(test1)
#m3=Matriz(3,4,"");
print(-1*m1)
print(m1*3)
print(m1*m2)
print(m1+m3)
print(m0)
m0.quitaFila(3)
print(m0)
m0.quitaColumna(1)
print(m0)
print(m0*m2)

A = Matriz(4,3)
print(A)
A = A.quitaFila(2)
print(A)
B = Matriz(4,4,'diag')
print(B)
print("C = Matriz(4,1,'unos')")
C = Matriz(4,1,'unos')
print(C)
print("D = 3 * B * C")#orden incorreto de operaciones en ejemplo?
D = 3 * (C * B)
#D = 3 * B * C
print(D)
print("E = 3 * B + C")
E = 3 * B + C
print(E)
"""
A = Matriz(n=3, m=4)
print(A)
A = A.quitaFila(2)
print(A)
B = Matriz(4,4,'diag')
print(B)
C = Matriz(4,1,'unos')
print("C = Matriz(4,1,'unos')")
print(C)
print("D = 3 * B * C")
D = 3 * B * C
print(D)
print("E = 3 * B + C")
E = 3 * B + C
A = Matriz(n=3, m=4)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Am=[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
Bm=[[1],[1],[1],[1]]

mt=Matriz(5,3,"");
A=mt.listToMatrix(Am)
B=mt.listToMatrix(Bm)
print(B*A)



print(A)
0 0 0 0
0 0 0 0
0 0 0 0

A = A.quitafila(2)

print(A)
0 0 0 0
0 0 0 0

B = Matriz(4,4,'diag')

print(B)
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1

C = Matriz(4,1,'unos')

print(C)
1
1
1
1

D = 3 * B * C

 print(D)
3
3
3
3

E = 3 * B + C
error "No seas menso, si no son de la misma dimensión las matrices no se pueden sumar"
"""

"""
Am=[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
Bm=[[1],[1],[1],[1]]

mt=Matriz(5,3,"");
A=mt.listToMatrix(Am)
B=mt.listToMatrix(Bm)
print(B*A)


test1=[[1,2,3],[4,5,6]]
test2=[[7,8],[9,10],[11,12]]
m0=Matriz(5,5,"diag");
mt=Matriz(5,3,"");
m1=mt.listToMatrix(test1)
m2=mt.listToMatrix(test2)
m3=mt.listToMatrix(test1)
#m3=Matriz(3,4,"");
print(-1*m1)
print(m1*3)
print(m1*m2)
print(m1+m3)
print(m0)
m0.quitaFila(3)
print(m0)
m0.quitaColumna(1)
print(m0)
print(m0*m2)

"""
