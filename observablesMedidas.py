import Complejos as c
import numpy as np
import math

def ejercicio431():
    A = np.array([[0,1],[1,0]])
    vp, vep = np.linalg.eig(A)
    print("Valores propios")
    for i in range(len(vp)):
        print("x"+str(i+1)+"="+str(vp[i]))
    print()
    print("Vectores propios")
    for i in range(len(vep)):
        print("e"+str(i+1)+"="+str(vep[i]))


"""def ejercicio432():
    A = [[0,1],[1,0]]
    a=1/2
    si = [a,a]
    p1 = 0
    for i in range(len(A)):
   """

def ejercicio441():
    u1=[[(0,0),(0,1)],[(0,1),(0,0)]]
    tp=math.sqrt(2)/2
    u2=[[(0,tp),(0,tp)],[(0,tp),(0,-tp)]]
    bool1 = c.matrizUnitariaComprobacion(u1)
    bool2 = c.matrizUnitariaComprobacion(u2)
    if bool1:
        print("La matriz U1 es unitaria")
    else:
        print("La matriz U1 no es unitaria")
    print()

    if bool1:
        print("La matriz U2 es unitaria")
    else:
        print("La matriz U2 no es unitaria")

    mult1 = c.productoDeMatrices(u1,u2)
    mult2 = c.productoDeMatrices(u2,u1)

    if(c.matrizUnitariaComprobacion(mult1)):
        print("La multiplicación U1 y U2 es unitaria")
    else:
        print("La multiplicación U1 y U2 no es unitaria")
    if(c.matrizUnitariaComprobacion(mult2)):
        print("La multiplicación U2 y U1 es unitaria")
    else:
        print("La multiplicación U2 y U1 no es unitaria")
    
    
    
    
    
    
    
