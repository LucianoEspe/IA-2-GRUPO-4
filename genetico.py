import random
from random import randint
import math
import cProfile, pstats, io
from pstats import SortKey
import matplotlib.pyplot as plt


class Nodo():
    def __init__(self, _fila, _columna, _nombre):
        self.columna = _columna
        self.fila = _fila
        self.nombre = _nombre
        self.inicio = False
        self.meta = False
        self.pasillo = False
        self.estante = False
        self.padre = None
        self.g = 1
        self.h = 9999999
        self.f = 9999999

    def crearPasillo(self):
        self.pasillo = True

    def crearEstante(self):
        self.estante = True

    def crearInicio(self):
        self.inicio = True

    def crearMeta(self):
        self.meta = True

    def esPasillo(self):
        return self.pasillo

    def esEstante(self):
        return self.estante

    def esInicio(self):
        return self.inicio

    def esMeta(self):
        return self.meta

    def heu(self, filaO, columnaO):
        self.h = abs(self.fila-filaO)+abs(self.columna-columnaO)
        self.f = self.h+self.g

    def gcost(self, fila_inicial, columna_inicial):
        self.g = abs(fila_inicial-self.fila)+abs(columna_inicial-self.columna)


def ordenar(lista):
    lista.sort(key=lambda x: x.f)
    return lista


def crearNodos(Mapa, _Inicio, _Meta):
    fila = 0
    Nodos = []
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Nodos.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    numero = 0
    for filas in Mapa:
        for columna, valor in enumerate(Mapa[fila]):
            if valor == " P":
                nodo = Nodo(fila, columna, "P"+str(numero))
                numero += 1
                nodo.crearPasillo()
                nodo.heu(_Meta[0], _Meta[1])
                Nodos[fila][columna] = nodo
            elif valor == " I":
                nodo = Nodo(fila, columna, valor)
                nodo.crearInicio()
                nodo.heu(_Meta[0], _Meta[1])
                Nodos[fila][columna] = nodo
            elif valor == " M":
                nodo = Nodo(fila, columna, valor)
                nodo.crearMeta()
                nodo.heu(_Meta[0], _Meta[1])
                Nodos[fila][columna] = nodo
            else:
                nodo = Nodo(fila, columna, valor)
                nodo.crearEstante()
                nodo.heu(_Meta[0], _Meta[1])
                Nodos[fila][columna] = nodo
        fila += 1
    Nodos[_Inicio[0]][_Inicio[1]].crearInicio()
    Nodos[_Inicio[0]][_Inicio[1]].heu(_Meta[0], _Meta[1])
    Nodos[_Meta[0]][_Meta[1]].crearMeta()
    Nodos[_Meta[0]][_Meta[1]].heu(_Meta[0], _Meta[1])
    return Nodos


def Algoritmo(Mapa, Inicio, Meta): #algoritmo A estrella
    posiX = Inicio[0]
    posiY = Inicio[1]
    posmX = Meta[0]
    posmY = Meta[1]

    Nodos = crearNodos(Mapa, Inicio, Meta)

    Abiertos = []  # Sucesores sin explorar, ordenados en forma creciente de f
    Cerrados = []  # Nodos ya explorados

    for filas in Nodos:
        for nodo in filas:
            if nodo.esInicio():
                Abiertos.append(nodo)
                # da 0, costo desde el actual al nodo raíz
                nodo.gcost(posiY, posiX)
                nodo.heu(posmY, posmX)  # costo desde el actual a la meta

    # Para agregar los sucesores iniciales
    bordesup = False
    bordeinf = False
    bordeizq = False
    bordeder = False

    if Abiertos[0].fila == 0:
        bordesup = True
    if Abiertos[0].fila == 17:
        bordeinf = True
    if Abiertos[0].columna == 0:
        bordeizq = True
    if Abiertos[0].columna == 17:
        bordeder = True
        # nodo de abajo
    if Abiertos[0].fila < 17 and Nodos[Abiertos[0].fila + 1][Abiertos[0].columna].esPasillo() and not bordeinf:
        Nodos[Abiertos[0].fila + 1][Abiertos[0].columna].gcost(posiY, posiX)
        Nodos[Abiertos[0].fila + 1][Abiertos[0].columna].heu(posmY, posmX)
        Nodos[Abiertos[0].fila + 1][Abiertos[0].columna].padre = Abiertos[0]
        Abiertos.append(Nodos[Abiertos[0].fila + 1][Abiertos[0].columna])
    # nodo de arriba
    if Abiertos[0].fila > 0 and Nodos[Abiertos[0].fila - 1][Abiertos[0].columna].esPasillo() and not bordesup:
        Nodos[Abiertos[0].fila - 1][Abiertos[0].columna].gcost(posiY, posiX)
        Nodos[Abiertos[0].fila - 1][Abiertos[0].columna].heu(posmY, posmX)
        Nodos[Abiertos[0].fila - 1][Abiertos[0].columna].padre = Abiertos[0]
        Abiertos.append(Nodos[Abiertos[0].fila - 1][Abiertos[0].columna])
    # nodo a la derecha
    if Abiertos[0].columna < 17 and Nodos[Abiertos[0].fila][Abiertos[0].columna + 1].esPasillo() and not bordeder:
        Nodos[Abiertos[0].fila][Abiertos[0].columna+1].gcost(posiY, posiX)
        Nodos[Abiertos[0].fila][Abiertos[0].columna+1].heu(posmY, posmX)
        Nodos[Abiertos[0].fila][Abiertos[0].columna+1].padre = Abiertos[0]
        Abiertos.append(Nodos[Abiertos[0].fila][Abiertos[0].columna+1])
        # nodo de la izquierda
    if Abiertos[0].columna > 0 and Nodos[Abiertos[0].fila][Abiertos[0].columna - 1].esPasillo() and not bordeizq:
        Nodos[Abiertos[0].fila][Abiertos[0].columna-1].gcost(posiY, posiX)
        Nodos[Abiertos[0].fila][Abiertos[0].columna-1].heu(posmY, posmX)
        Nodos[Abiertos[0].fila][Abiertos[0].columna-1].padre = Abiertos[0]
        Abiertos.append(Nodos[Abiertos[0].fila][Abiertos[0].columna - 1])


    Cerrados.append(Abiertos[0])  # AÑADE EL INICIAL A CERRADOS (YA EXPLORADO)
    Abiertos.remove(Abiertos[0])  # SE ELIMINA EL INICIAL
    Abiertos = ordenar(Abiertos)  # SE ORDENAN LOS VECINOS AGREGADOS
    NodoActual = Abiertos[0]  # MEJOR VECINO
    stop = 0
    costo_ = 0
    while True:
        # Comprobación de Meta
        bordesup = False
        bordeinf = False
        bordeizq = False
        bordeder = False

        if NodoActual.fila == 0:
            bordesup = True
        if NodoActual.fila == 17:
            bordeinf = True
        if NodoActual.columna == 0:
            bordeizq = True
        if NodoActual.columna == 17:
            bordeder = True

        # Verificacion de meta alcanzada
        meta = 0
        if not bordeinf:
            if Nodos[NodoActual.fila + 1][NodoActual.columna].esMeta():
                meta = 1
        if not bordesup:
            if Nodos[NodoActual.fila - 1][NodoActual.columna].esMeta():
                meta = 1
        if not bordeder:
            if Nodos[NodoActual.fila][NodoActual.columna + 1].esMeta():
                meta = 1
        if not bordeizq:
            if Nodos[NodoActual.fila][NodoActual.columna - 1].esMeta():
                meta = 1
        if meta == 1:
            Camino = []
            while NodoActual is not None:
                Camino.append("["+str(NodoActual.fila)+"][" +
                              str(NodoActual.columna)+"]")
                NodoActual = NodoActual.padre
            Camino = list(reversed(Camino))
            costo_ = len(Camino)
            break

        # nodo de abajo
        if not bordeinf:
            if Nodos[NodoActual.fila + 1][NodoActual.columna].esPasillo() and not Nodos[NodoActual.fila + 1][NodoActual.columna] in Cerrados and not Nodos[NodoActual.fila + 1][NodoActual.columna] in Abiertos:
                Nodos[NodoActual.fila +
                      1][NodoActual.columna].gcost(posiY, posiX)
                Nodos[NodoActual.fila +
                      1][NodoActual.columna].heu(posmY, posmX)
                Nodos[NodoActual.fila + 1][NodoActual.columna].padre = NodoActual
                Abiertos.append(Nodos[NodoActual.fila + 1][NodoActual.columna])
        # nodo de arriba
        if not bordesup:
            if Nodos[NodoActual.fila - 1][NodoActual.columna].esPasillo() and not Nodos[NodoActual.fila - 1][NodoActual.columna] in Cerrados and not Nodos[NodoActual.fila - 1][NodoActual.columna] in Abiertos:
                Nodos[NodoActual.fila -
                      1][NodoActual.columna].gcost(posiY, posiX)
                Nodos[NodoActual.fila -
                      1][NodoActual.columna].heu(posmY, posmX)
                Nodos[NodoActual.fila - 1][NodoActual.columna].padre = NodoActual
                Abiertos.append(Nodos[NodoActual.fila - 1][NodoActual.columna])
        # nodo a la derecha
        if not bordeder:
            if Nodos[NodoActual.fila][NodoActual.columna + 1].esPasillo() and not Nodos[NodoActual.fila][NodoActual.columna + 1] in Cerrados and not Nodos[NodoActual.fila][NodoActual.columna + 1] in Abiertos:
                Nodos[NodoActual.fila][NodoActual.columna +
                                       1].gcost(posiY, posiX)
                Nodos[NodoActual.fila][NodoActual.columna+1].heu(posmY, posmX)
                Nodos[NodoActual.fila][NodoActual.columna+1].padre = NodoActual
                Abiertos.append(Nodos[NodoActual.fila][NodoActual.columna+1])
            # nodo de la izquierda
        if not bordeizq:
            if Nodos[NodoActual.fila][NodoActual.columna - 1].esPasillo() and not Nodos[NodoActual.fila][NodoActual.columna - 1] in Cerrados and not Nodos[NodoActual.fila][NodoActual.columna - 1] in Abiertos:
                Nodos[NodoActual.fila][NodoActual.columna -
                                       1].gcost(posiY, posiX)
                Nodos[NodoActual.fila][NodoActual.columna-1].heu(posmY, posmX)
                Nodos[NodoActual.fila][NodoActual.columna-1].padre = NodoActual
                Abiertos.append(Nodos[NodoActual.fila][NodoActual.columna - 1])

        if stop >= 10000:
            print("No se encotró la solución")
            break
        stop += 1

        # UNA VEZ AGREGADOS LOS NODOS VECINOS A ABIERTOS:
        ##########################
        Cerrados.append(NodoActual)  # AGREGO EL NODO ACTUAL A LOS CERRADOS
        Abiertos.remove(NodoActual)  # ELIMINO EL NODO ACTUAL DE ABIERTOS
        Abiertos = ordenar(Abiertos)  # ORDENO POR VALOR DE F
        NodoActual = Abiertos[0]  # NODO ACTUAL ES EL DE MENOR F EN ABIERTOS
    return costo_


def buscarProducto(Nodos, producto):
    for filas in Nodos:
        for elementos in filas:
            if elementos.nombre == producto:
                return([elementos.fila, elementos.columna])


def estadosVecinos(orden, _espacioBusqueda):
    subconjunto = []
    ordenAux = orden[:]
    i = 0
    stop = 0
    while i < _espacioBusqueda:
        posA = random.randint(0, len(orden)-1)
        posB = random.randint(0, len(orden)-1)
        while posA == posB:
            posB = random.randint(0, len(orden)-1)
        ordenAux[posA], ordenAux[posB] = ordenAux[posB], ordenAux[posA]
        if ordenAux not in subconjunto:
            subconjunto.append(ordenAux[:])
            i += 1
        ordenAux = orden[:]
        if stop == 5000:
            break
        stop += 1
    return subconjunto


def calcularCosto(orden, _NodosAux, _Inicio):
    costoT = []
    InicioAux = _Inicio
    for producto in orden:
        costoT.append(Algoritmo(Mapa, InicioAux,
                      buscarProducto(_NodosAux, producto)))
        InicioAux = buscarProducto(_NodosAux, producto)
    costoT.append(Algoritmo(Mapa, buscarProducto(
        _NodosAux, producto), _Inicio))
    return sum(costoT[:])


def crearMapa(productos):
    Mapa = []
    # 0     1     2     3     4     5     6     7     8     9    10     11    12    13    14   15    16     17
    Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P",
                " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 0 PASILLO
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " E"])  # 1
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " E"])  # 2
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " E"])  # 3
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " E"])  # 4
    Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P",
                " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 5 PASILLO
    Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P",
                " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 6 PASILLO
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " P"])  # 7
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " P"])  # 8
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " P"])  # 9
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " P"])  # 10
    Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P",
                " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 11 PASILLO
    Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P",
                " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 12 PASILLO
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " P"])  # 13
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " P"])  # 14
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " P"])  # 15
    Mapa.append([" P", " E", " E", " P", " P", " E", " E", " P", " P",
                " E", " E", " P", " P", " E", " E", " P", " P", " P"])  # 16
    Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P",
                " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 17 PASILLO
    # productos=[]
    # for numeros in range(0,100):
    #    productos.append(str(numeros))
    fila = 0
    i = 0
    for filas in Mapa:
        for columna, valor in enumerate(Mapa[fila]):
            if valor == " E":
                # elegido=random.choice(productos)
                Mapa[fila][columna] = str(productos[i])
                # productos.remove(elegido)
                i += 1
        fila += 1
    return Mapa

def Temple(orden, Mapa):
    Inicio = [0, 0]
    # LO UTILIZO PARA BUSCAR LA UBICACION DE LOS PRODUCTOS
    NodosAux = crearNodos(Mapa, Inicio, [1, 1])
    cantidadEstados = math.factorial(len(orden)-1)
    espacioBusqueda = cantidadEstados//2
    estadosvisitados = []
    T = 10
    while T > 0:
        #print("T:", T)
        costoActual = calcularCosto(orden, NodosAux, Inicio)
        while True:
            ordenAux = random.choice(estadosVecinos(orden[:], espacioBusqueda))
            for ordenes in estadosvisitados:
                if ordenAux == ordenes[0]:
                    #print("ORDEN", ordenAux)
                    #print("ORDEN EN ESTADOS", ordenes[0])
                    ordenAux = random.choice(
                        estadosVecinos(orden[:], espacioBusqueda))
            else:
                break
        costoSucesor = calcularCosto(ordenAux, NodosAux, Inicio)
        if costoActual >= costoSucesor:
            orden = ordenAux
            estadosvisitados.append([orden[:], costoSucesor])
            costoActual = costoSucesor
            #print("ESTADO VECINO ACEPTADO POR DELTA")
        else:
            prob = random.uniform(0, 1)
            #print("Probabilidad random:", prob)
            x = -abs(costoActual-costoSucesor)/T
            crit = math.exp(x)
            #print("Probabilidad criterio", crit)
            if prob <= crit:
                orden = ordenAux
                estadosvisitados.append([orden[:], costoSucesor])
                costoActual = costoSucesor
                #print("ESTADO VECINO ACEPTADO POR PROBABILIDAD")
        T -= 1
    mejorCosto = 9999
    mejorVecino = [0, 0]
    for elementos in estadosvisitados:
        # print(elementos)
        if elementos[1] <= mejorCosto:
            mejorCosto = elementos[1]
            mejorVecino = elementos
    #print("ESTADO Y COSTO FINAL", estadosvisitados[len(estadosvisitados)-1])
    #print("MEJOR ESTADO Y COSTO ENCONTRADO",mejorVecino)
    return mejorCosto

def Ordenes():
    ordenes = []
    orden1 = []
    orden2 = []
    orden3 = []
    orden4 = []
    orden5 = []
    orden6 = []
    orden7 = []
    orden8 = []
    orden9 = []
    orden10 = []

    with open("ordenes.txt", "r") as archivo:
        i = 0
        for linea in archivo:
            if i > 0 and i <= 10:
                orden1.append(linea.replace("\n", "").replace("P", ""))
            if i > 12 and i <= 22:
                orden2.append(linea.replace("\n", "").replace("P", ""))
            if i > 24 and i <= 34:
                orden3.append(linea.replace("\n", "").replace("P", ""))
            if i > 36 and i <= 46:
                orden4.append(linea.replace("\n", "").replace("P", ""))
            if i > 48 and i <= 58:
                orden5.append(linea.replace("\n", "").replace("P", ""))
            if i > 60 and i <= 70:
                orden6.append(linea.replace("\n", "").replace("P", ""))
            if i > 72 and i <= 82:
                orden7.append(linea.replace("\n", "").replace("P", ""))
            if i > 84 and i <= 94:
                orden8.append(linea.replace("\n", "").replace("P", ""))
            if i > 96 and i <= 106:
                orden9.append(linea.replace("\n", "").replace("P", ""))
            if i > 108 and i <= 118:
                orden10.append(linea.replace("\n", "").replace("P", ""))
            i += 1
        ordenes.append(orden1)
        ordenes.append(orden2)
        ordenes.append(orden3)
        ordenes.append(orden4)
        ordenes.append(orden5)
        ordenes.append(orden6)
        ordenes.append(orden7)
        ordenes.append(orden8)
        ordenes.append(orden9)
        ordenes.append(orden10)
        return ordenes

def cruceOrden(individuo1,individuo2):
    corte1=randint(1,99)
    corte2=randint(1,99)
    while corte2<=corte1:
        corte2=randint(1,99)

    ind1aux=[]
    ind2aux=[]
    
    for numeros in range(corte1,corte2):
        ind1aux.append(individuo2[numeros])
        ind2aux.append(individuo1[numeros])

    for prod in individuo1:
        if (prod not in ind1aux) and len(ind1aux)<=len(individuo1)-1-corte1:
            ind1aux.append(prod)
    pos=0
    for prod in individuo1:
        if (prod not in ind1aux) and len(ind1aux)<=len(individuo1)-1:
            ind1aux.insert(pos,prod)
            pos+=1
    
    for prod in individuo2:
        if (prod not in ind2aux) and len(ind2aux)<=len(individuo2)-1-corte1:
            ind2aux.append(prod)
    pos=0
    for prod in individuo2:
        if (prod not in ind2aux) and len(ind2aux)<=len(individuo2)-1:
            ind2aux.insert(pos,prod)
            pos+=1

    return ([ind1aux,ind2aux])

def eleccion_prob(lista): #recibe una lista con los costos de cada individuo de la población

    probabilidad=[]
    for c in range(10):
        lista[c]=1/lista[c]
    suma=float(sum(lista))
    for c in range(10):

        probabilidad.append(((lista[c]/suma)*100))

    prob=random.randint(0, 99)
    if prob>=0 and prob<probabilidad[0]:
        indice=0
    if prob>=probabilidad[0] and prob<probabilidad[0]+probabilidad[1]:
        indice=1
    if prob>=probabilidad[0]+probabilidad[1] and prob<probabilidad[0]+probabilidad[1]+probabilidad[2]:
        indice=2
    if prob>=probabilidad[0]+probabilidad[1]+probabilidad[2] and prob<probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]:
        indice=3
    if prob>=probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3] and prob<probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]:
        indice=4
    if prob>=probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4] and prob<probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5]:
        indice=5
    if prob>=probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5] and prob<probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5]+probabilidad[6]:
        indice=6
    if prob>=probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5]+probabilidad[6] and prob<probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5]+probabilidad[6]+probabilidad[7]:
        indice=7
    if prob>=probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5]+probabilidad[6]+probabilidad[7] and prob<probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5]+probabilidad[6]+probabilidad[7]+probabilidad[8]:
        indice=8
    if prob>=probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5]+probabilidad[6]+probabilidad[7]+probabilidad[8] and prob<probabilidad[0]+probabilidad[1]+probabilidad[2]+probabilidad[3]+probabilidad[4]+probabilidad[5]+probabilidad[6]+probabilidad[7]++probabilidad[8]+probabilidad[9]:
        indice=9
    return indice


#########  ALGORITMO GENÉTICO#########


pr = cProfile.Profile()
pr.enable()
listaOrdenes = Ordenes()
# crea una lista para almacenar los productos en un orden aleatorio sin repetir.
matriz=[]
for i in range(0,10):
    productos=[]
    productosorden=[]
    for numeros in range(0,100):
        productos.append(str(numeros))  #crea una lista con productos del 0 al 99
    for i in range(0,100):
        elegido=random.choice(productos) #elige un elemento de la lista productos al azar
        productosorden.append(elegido) #guardamos ese producto en una lista auxiliar
        productos.remove(elegido) #eliminamos el producto de la lista creada en el bucle for anterior
    matriz.append(productosorden)
########### MATRIZ CONTIENE 10 ORDENAMIENTOS AL AZAR (población inicial de 10 individuos) ##########
print("Generacion 0 creada...")
generacion=1
stop = 0

costoordenes=[]
while generacion<=3:
    while stop < 10:
        print("#")
        if generacion==1:
            Mapa = crearMapa(matriz[stop])
        elif generacion==2:
            Mapa = crearMapa(matriz[stop+10])
        Costos = []
        for i in range(0, len(listaOrdenes)-1):
            Costos.append(Temple(listaOrdenes[i], Mapa))
        sumacostos = sum(Costos)
        costoordenes.append(int(sumacostos))  #ACA GUARDAMOS EL COSTO DE CADA ORDENAMIENTO
        stop += 1
        
    print("\n")
    stop=0
    generacion+=1

    
    ### SELECCIONO 2 INDIVIDUOS BAJO CIERTA PROBABILIDAD Y HAGO EL CROSSOVER, REPITO HASTA COMPLETAR DE INDIVIDUOS LA SIGUIENTE GENERACIÓN #### 
    ind=0
    individuos=[]
    print("Proceso de Crossover...")
    if generacion-1<3:
        while ind<5:
            if generacion-1==1:
                selA=matriz[eleccion_prob(costoordenes)] #eleccion_prob me devuelve el índice de uno de los elementos de la lista matriz, por probabilidad el menor costo 
                selB=matriz[eleccion_prob(costoordenes)]
                while selA==selB:
                    selB=matriz[eleccion_prob(costoordenes)]
            elif generacion-1==2:
                selA=matriz[10+eleccion_prob(costoordenes[10:])]
                selB=matriz[10+eleccion_prob(costoordenes[10:])]
                while selA==selB:
                    selB=matriz[10+eleccion_prob(costoordenes[10:])]

            individuos.append(cruceOrden(selA,selB))
            for vect in individuos:
                for indi in vect:
                    matriz.append(indi)
            ind+=1
            individuos.clear()
            individuos=[]
        print(f"Generacion {generacion-1} creada...")
print("costoordendes: ",costoordenes)
costmin=costoordenes[:].index(min(costoordenes[:]))
print(f"El mejor ordenamiento es {matriz[costmin]} y su costo es {min(costoordenes[:])}")

## ESTADÍSTICAS DE TIEMPO
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())


## GRAFICO
i=0
CostGen=[]
Generaciones=[0,1,2]
for iter in range(3):
    mini=costoordenes.index(min(costoordenes[i:i+10]))
    CostGen.append(costoordenes[mini])
    i+=10
fig, ax = plt.subplots()
ax.plot(Generaciones, CostGen)
plt.xlabel("Generacion", size = 16)
plt.ylabel("Costo del mejor individuo", size = 16)
ax.set_title("Evolucion de los costos en funcion de la generacion",loc="center")
plt.xticks([0, 1, 2])
plt.show()

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], costoordenes[0:10], color = 'tab:purple', label = 'generacion 0')
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], costoordenes[10:20], color = 'tab:green', label = 'generacion 1')
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], costoordenes[20:30], color = 'tab:red', label = 'generacion 2')
ax.set_xlabel("Individuos")
ax.set_ylabel("Costos")
ax.legend(loc = 'upper right')
plt.show()

