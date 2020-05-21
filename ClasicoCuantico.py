import Complejos
import math
from matplotlib import pyplot

def sistemaDeterministicoProbabilistico(grafo, vector, clics):
    """Calcula los clics en un sistema deterministico.

    Devuelve vector de probabilidades.

    Parametros:
    grafo -- Es un arreglo de arreglos que repesenta una matriz booleana.
    vector -- Es un arreglo que repesenta el estado inicial de cuantas canicas hay en cada vetice.
    clics -- Cuantos movimientos de tiempo debe hacer.

    """
    
    if clics==0:
        return vector
    else:
        temp=click(grafo,clics)
        res=Complejos.productoMatrizVector(temp,vector)
        return res  

def sistemaProbabilisticoMultiplesRendijas(rendijas,objetivo,probabilidades):
    """Calcula los clics en un sistema deterministico.

    Devuelve vector de probabilidades.

    Parametros:
    rendija -- Representa la cantidad de rendijas que se usaran en la simulacion.
    objetivos -- Representa la cantidad de objetivos que se usaran en la simulacion.
    probabilidades -- Es un vector que contiene las probabilidades de ir de una rendija a un objetivo.

    """
    vecIni=[(1,0)]
    temp=rendijas+1
    lim=objetivo+2
    frac2=1/rendijas
    divisiones=objetivo//2
    dim=calcularTamaño(objetivo,rendijas,divisiones)+rendijas
    grafo=crarGrafo(dim+1,temp)
    grafo=llenarUno(grafo,rendijas,dim,objetivo,frac2)
    grafo=llenarDos(grafo,rendijas,objetivo,probabilidades,divisiones)
    for i in range(dim-1):
        vecIni.append((0,0))
    k=click(grafo,2)
    res=sistemaDeterministicoProbabilistico(grafo, vecIni, 2)
    return res
    

def simulacionCuanticaMultiplesRendijas(rendijas,objetivo,probabilidades):
    """Calcula los clics en un sistema deterministico.

    Devuelve vector de probabilidades.

    Parametros:
    rendijas -- Representa la cantidad de rendijas que tendra el sistema.
    objetivos -- Representa la cantidad de objetivos que tendra el sistema.
    probabilidades -- Es un vector que contiene las probabilidades de ir de una rendija a un objetivo.

    """
    vecIni=[(1,0)]
    temp=rendijas+1
    lim=objetivo+2
    frac2=1/math.sqrt(rendijas)
    divisiones=objetivo//2
    dim=calcularTamaño(objetivo,rendijas,divisiones)+rendijas
    grafo=crarGrafo(dim+1,temp)
    grafo=llenarUno(grafo,rendijas,dim,objetivo,frac2)
    grafo=llenarDos(grafo,rendijas,objetivo,probabilidades,divisiones)
    for i in range(dim-1):
        vecIni.append((0,0))
    k=click(grafo,2)
    grafo=cambiarProbabilidad(k)
    res=sistemaDeterministicoProbabilistico(grafo, vecIni, 2)
    graficar(res)
    return res

def click(grafo,click):
    """ Calcula la potencia de una matriz, eso representa los click.

    Devuelve una matriz.

    Parametros:
    grafo -- Es un vector de vectores que representa la matriz.
    click -- es un entero que me dice cuantos clicks quiere que haga.
    """
    
    temp=grafo
    for i in range(click-1):
        temp=Complejos.productoDeMatrices(grafo,temp)
    return temp

def crarGrafo(dim,temp):
    """Permite crear la dimension de la matriz, la cual representa el grafo.

    Devuelve una matriz que representa el grafo.

    Parametros:
    dim -- Como la matriz es cuadrada mandamos la dimension con un entero.
    temp -- Es un entero que representa la cantidad de rendijas.
    """
    grafo=[]
    for i in range(dim):
        row=[]
        for j in range(dim):
            if i==temp and j==temp:
                row.append((1,0))
                temp+=1
            else:
                row.append((0,0))
        grafo.append(row)
    return grafo

def calcularTamaño(ob,re,div):
    """Esta funcion me permite calcular la dimension que tendra la maatriz

    Devuelve un entero que representa la dimension de la matriz

    Parameteros:
    ob -- Cantidad de objetivos del experimento
    re -- Cantidad de rendijas del experimento
    div -- Repensenta los objetivos que hay por rendija.
    """
    res=div
    for i in range(re):
        res+=div
    return res+re

def llenarUno(g,x,dim,obj,frac2):
    """Llena la primera collumna de la matriz con los valores que tiene cada objetivo

    Devuelve una matriz

    Parametros:
    g -- Es la matriz que representa el grafo
    x -- Cantidad de rendijas del experimento
    dim -- La dimension de la matriz
    obj -- Cantidad de objetivos del experimento
    frac2 -- El valor que debe ir en la respectiva casilla
    """
    for j in range(1,dim+1):
        if j<=x:
            g[j][0]=(frac2,0)
    return g

def llenarDos(g,r,o,p,div):
    """Llena ls demas columnas que necesitan colocar sus valores representando el peso.

    Devuelve una matriz que representa el estado inicial del experimento
    
    Parametros:
    g -- Es la matriz que representa el grafo
    r -- Cantidad de rendijas del experimento
    o -- Cantidad de objetivos del experimento
    p -- Vector que contiene las probabilidades de ir de una rendija a un objetivo
    div -- Cantidad de objetivos que hay por rendija.
    """
    temp=0
    k=o
    vec=0
    while temp!=r:
        temp+=1
        i=0
        while i!=o:
            g[k][temp]=p[vec]
            vec+=1
            i+=1
            k+=1
        k-=div
    return g

def cambiarProbabilidad(g):
    """Nos permite cambiar una matriz de complejos a reales.

    Devuelve un sistema probabilisitco

    Parametros:
    g -- La matriz que representa el grafo.
    """
    for i in range(len(g)):
        for j in range(len(g[i])):
            temp=g[i][j]
            g[i][j]=(temp[0]*temp[0]+temp[1]*temp[1],0)
    return g

def graficar(vec):
    """Hace un diagrama de barras que muestre las probabilidades de un vector de estados

    Devuelve un diagrama de barras

    Parametros:
    vec -- Es el vector que contiene las probabilidades
    """
    res=[]
    pos=[]
    for i in range(len(vec)):
        res.append(vec[i][0])
        pos.append(i)
    pyplot.title("Probabilidad experimento de rendija cuantica")
    pyplot.bar(pos, height=res, color='blue', width=0.5)
    pyplot.show()
