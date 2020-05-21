import math


def sumar(a,b):
    """Resuelve la suma de 2 numeros complejos.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.
    b -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    ente=a[0]+b[0]
    imag=a[1]+b[1]
    return (ente,imag)    

def restar(a,b):
    """Resuelve la resta de 2 numeros complejos.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.
    b -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    ente=a[0]-b[0]
    imag=a[1]-b[1]
    return (ente,imag)    

def multiplicar(a,b):
    """Resuelve la multiplicacion de 2 numeros complejos.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.
    b -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    ente=a[0]*b[0]+(-1*(b[1]*a[1]))
    imag=a[0]*b[1]+a[1]*b[0]
    return (ente,imag)    

def modulo(a):
    """Resuelve el modulo de un numero complejo.

    Devuelve una tupla de un real.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    return (math.sqrt((a[0]**2+a[1]**2)))
    
def division(a,b):
    """Resuelve la division de 2 numeros complejos.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.
    b -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    try:
        div=b[0]**2+b[1]**2
        ente=(a[0]*b[0]+a[1]*b[1])/div
        imag=(a[1]*b[0]-a[0]*b[1])/div
        return (ente,imag)    
    except:
        return 'Imposible hacer la division.'
        
def conjugado(a):
    """Resuelve el conugado de un numero complejo.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    ente=a[0]
    imag=a[1]*-1
    return (ente,imag)

def cartesianoPolar(a):
    """Cambia de coordenadas cartesianas a polares de un numero complejo.

    Devuelve una tupla con la parte real y un angulo en radianes.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    p=(math.sqrt(a[0]**2+a[1]**2))
    o=(math.atan2(a[1],a[0]))
    return (p,o)

def polarCartesiano(p):
    """Cambia de coordenadas polares a cartesianas de un numero complejo.

    Devuelve una tupla con la parte real y la parte imaginaria del numero complejo.

    Parametros:
    p -- Es una tupla que contiene parte real y un angulo.

    """
    a=round(p[0]*math.cos(p[1]),3)
    b=round(p[0]*math.sin(p[1]),3)
    return (a,b)

def fase(a):
    """Resuelve la fase de un numero complejo.

    Devuelve una tupla que contiene el angulo en radianes.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    res=math.atan2(a[1],a[0])
    return (round(res,2))

def sumaVectoresComplejos(a,b):
    """Resuelve la suma de dos vectores de numeros complejos.

    Devuelve un arreglo con la suma de vectores.

    Parametros:
    a -- Es un Arreglo que repesenta un vector.
    b -- Es un Arreglo que repesenta un vector.

    """
    try:
        res=[]
        for i in range(len(a)):
            row=sumar(a[i],b[i])
            res.append(row)
        return res
    except:
        return 'No es posible hacer la suma de vectores, revisa las dimensiones.'

def inversaVectores(a):
    """Calcula la inversa de un vector de numeros complejos.

    Devuelve un arreglo con la inversa del vector a.

    Parametros:
    a -- Es un Arreglo que representa un vector, contiene tuplas de numeros complejos.

    """
    res=[]
    for i in range(len(a)):
        real=a[i][0]
        img=a[i][1]
        row=(-real,-img)
        res.append(row)
    return res

def multEscalarVectores(escalar,vector):
    """Resuelve la multiplicacion de un escalar por un vectores de numeros complejos.

    Devuelve un arreglo con la multiplicacion del escalar por el vector.

    Parametros:
    escalar -- Es una tupla que contiene un numero complejo (real, imaginario).
    vector -- Es un Arreglo que repesenta un vector, con tuplas de complejos.

    """
    res=[]
    for i in range(len(vector)):
        row=multiplicar(escalar,vector[i])
        res.append(row)
    return res

def sumaMatricesComplejas(a,b):
    """Resuelve la suma de dos matrices de numeros complejos.

    Devuelve un arreglo con la suma de las matrices.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.
    b -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    try:
        res=[]
        for i in range(len(a)):
            row=[]
            for j in range(len(a[i])):
                add=sumar(a[i][j],b[i][j])
                row.append(add)
            res.append(row)
        return res
    except:
        return 'No es posible hacer la suma de matrices, revisa las dimensinones.'



def inversaMatricesComplejas(a):
    """Calcula la inversa de una matriz de numeros comlejos.

    Devuelve un arreglo de arreglos con la inversa de a.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    res=[]
    for i in range(len(a)):
        res.append(inversaVectores(a[i]))
    return res

def multEscalarMatriz(escalar,matriz):
    """Calcula la multiplicaicon de un escalar por una matriz de numeros complejos.

    Devuelve un arreglo de arreglos que representa la multiplicacion.

    Parametros:
    escalar -- Es una tupla de un numero complejo.
    matriz -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    res=[]
    for i in matriz:
        res.append(multEscalarVectores(escalar,i))
    return res

def transpuestaMatriz(a):
    """Calcula la transpuesta de una matriz de numeros complejos.
    En particular, si se ingresa un vector seria de la forma:[[(r0,c0),(r1,c1),(rn,cn)]]

    Devuelve un arreglo de arreglos con la transpuesta de a.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    res=rellenar(a)    
    for i in range(len(a)):
        for j in range(len(a[i])):
            res[j][i]=a[i][j]
    return res

def conjugadoMatriz(a):
    """Calcula el conjugado de una matriz de numeros complejos.
    En particular, si se ingresa un vector seria de la forma:[[(r0,c0),(r1,c1),(rn,cn)]]

    Devuelve un arreglo de arreglos con el conjugado de a.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    res=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(a[i])):
            row.append(conjugado(a[i][j]))
        res.append(row)
    return res

def adjuntaMatriz(a):
    """Calcula la adjunta de un matriz de numeros complejos.

    Devuelve un arreglo de arreglos con la adjunta de a.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    conj=conjugadoMatriz(a)
    return transpuestaMatriz(conj)

def productoDeMatrices(a,b):
    """Calcula el producto dos matrices de numeros complejos.

    Devuelve un arreglo de arreglos con el producto de a y b.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.
    b -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    try:
        res=[]
        for i in range(len(a)):
            row=[]
            for j in range(len(a[i])):
                suma=(0,0)
                for k in range(len(a[i])):
                    temp=multiplicar(a[i][k],b[k][j])
                    suma=sumar(temp, suma)
                row.append(suma)
            res.append(row)
        return res
    except:
        return 'No es posible hacer el prudcto de matrices, revisa las dimensiones.'

def productoMatrizVector(matriz,vector):
    """Calcula el producto una matrices y un vector; de numeros complejos.

    Devuelve un arreglo con el producto de la matriz y el vector.

    Parametros:
    matriz -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.
    vector -- Es un arreglo repesenta un vector, contiene tuplas de numeros complejos.

    """
    try:
        res=[]
        for i in range(len(matriz)):
            suma=(0,0)
            for j in range(len(vector)):
                temp=multiplicar(matriz[i][j],vector[j])
                suma=sumar(temp,suma)
            res.append(suma)                  
        return res
    except:
        return 'No es posible hacer el producto de matriz y vector, revisa las dimensiones.'

def productoInternoVectores(a,b):
    """Calcula el producto interno de 2 vectores de numeros complejos.

    Devuelve un numero complejo con el producto interno de a y b.

    Parametros:
    a -- Es un arreglo que repesenta un vector, contiene tuplas de numeros complejos.
    b -- Es un arreglo que repesenta un vector, contiene tuplas de numeros complejos.

    """
    try:
        newA=adjuntaMatriz([a])
        suma=(0,0)
        for i in range(len(a)):
            for j in range(len(newA[i])):
                temp=multiplicar(newA[i][j],b[i])
                suma=sumar(temp,suma)
        return suma
    except:
        return 'No es posible hacer el prodcuto interno de vecctores, revisa las dimensiones.'

def normaVector(a):
    """Calcula la norma o loguitud de un vectorde numeros complejos.

    Devuelve un numero que representa la norma o longuitud.

    Parametros:
    a -- Es un arreglo que repesenta un vector, contiene tuplas de numeros complejos.
    """
    pim=productoInternoVectores(a,a)
    return math.sqrt(pim[0])

def distanciaVectores(a,b):
    """Calcula la distancia de 2 vectores de numeros complejos.

    Devuelve un numero que representa la disstancia.

    Parametros:
    a -- Es un arreglo que repesenta un vector, contiene tuplas de numeros complejos.
    b -- Es un arreglo que repesenta un vector, contiene tuplas de numeros complejos.

    """
    newB=multEscalarVectores((-1,0),b)
    A=sumaMatricesComplejas([a],[newB])
    pim=productoInternoVectores(A[0],A[0])
    return math.sqrt(pim[0])    

def matrizUnitariaComprobacion(a):
    """Comprueba si la matriz es o no unitaria.

    Devuelve un booleano avisando si la matriz es o no unitaria.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    adj=adjuntaMatriz(a)
    mul=productoDeMatrices(a,adj)
    res=crearIdentidad(a)
    rm=redondear(mul)
    if res==rm:
        return True
    return False

def matrizHermitianaComprobacion(a):
    """Comprueba si la matriz es o no hermitiana.

    Devuelve un booleano avisando si la matriz es o no hermitiana.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """
    adj=adjuntaMatriz(a)
    if adj==a:
        return True
    return False
    
def productoTensor(a,b):
    """Calcula el producto tensor entre 2 matrices de numeros complejos.

    Devuelve una matriz con el producto tensor de a y b.

    Parametros:
    a -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.
    b -- Es un arreglo de arreglos que repesenta una matriz, contiene tuplas de numeros complejos.

    """

    res=[]
    for i in range(len(a)):
        for j in range(len(b)):
            row=[]
            for k in range(len(a[i])):
                for l in range(len(b[k])):
                    val=multiplicar(a[i][k],b[j][l])
                    row.append(val)
            res.append(row)            
    return res
    
def redondear(a):
    res=[]
    for i in a:
        row=[]
        for j in i:
            row.append((round(j[0]),j[1]))
        res.append(row)
    return res

def crearIdentidad(a):
    res=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(a[i])):
            if j==i:
                row.append((1,0))
            else:
                row.append((0,0))
        res.append(row)
    return res
                    
def rellenar(a):
    res=[]
    for i in range(len(a[0])):
        row=[]
        for j in range(len(a)):
            row.append(None)
        res.append(row)
    return res
            
        
            
    
    
        
        
