import random
import math
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


def Algoritmo(Mapa, Inicio, Meta):
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
    costo = 0
    while True:
      #Comprobación de Meta
      bordesup=False
      bordeinf=False
      bordeizq=False
      bordeder=False
    
      if NodoActual.fila==0:
        bordesup=True
      if NodoActual.fila==17:
        bordeinf=True
      if NodoActual.columna==0:
        bordeizq=True
      if NodoActual.columna==17:
        bordeder=True
        
      #Verificacion de meta alcanzada:
      meta=0
      if not bordeinf:
        if Nodos[NodoActual.fila + 1][NodoActual.columna].esMeta():
         meta=1
      if not bordesup:
        if Nodos[NodoActual.fila - 1][NodoActual.columna].esMeta():
          meta=1
      if not bordeder:
        if  Nodos[NodoActual.fila][NodoActual.columna + 1].esMeta():
          meta=1
      if not bordeizq:
        if Nodos[NodoActual.fila][NodoActual.columna - 1].esMeta():
          meta=1
      if meta ==1:
        Camino=[]
        while NodoActual is not None:
          Camino.append("["+str(NodoActual.fila)+"]["+str(NodoActual.columna)+"]")
          NodoActual=NodoActual.padre
        Camino=list(reversed(Camino))
        costo_=len(Camino)
        break
        
      #nodo de abajo
      if not bordeinf:
        if  Nodos[NodoActual.fila + 1][NodoActual.columna].esPasillo()  and not Nodos[NodoActual.fila + 1][NodoActual.columna] in Cerrados and not Nodos[NodoActual.fila + 1][NodoActual.columna] in Abiertos:
          Nodos[NodoActual.fila + 1][NodoActual.columna].gcost(posiY,posiX)
          Nodos[NodoActual.fila + 1][NodoActual.columna].heu(posmY,posmX)
          Nodos[NodoActual.fila + 1][NodoActual.columna].padre=NodoActual
          Abiertos.append(Nodos[NodoActual.fila + 1][NodoActual.columna])    
      #nodo de arriba
      if not bordesup:
        if  Nodos[NodoActual.fila - 1][NodoActual.columna].esPasillo() and not Nodos[NodoActual.fila - 1][NodoActual.columna] in Cerrados and not Nodos[NodoActual.fila - 1][NodoActual.columna] in Abiertos: 
          Nodos[NodoActual.fila - 1][NodoActual.columna].gcost(posiY,posiX)
          Nodos[NodoActual.fila - 1][NodoActual.columna].heu(posmY,posmX)
          Nodos[NodoActual.fila - 1][NodoActual.columna].padre=NodoActual
          Abiertos.append(Nodos[NodoActual.fila - 1][NodoActual.columna])
      #nodo a la derecha
      if not bordeder:
        if Nodos[NodoActual.fila][NodoActual.columna + 1].esPasillo() and not  Nodos[NodoActual.fila][NodoActual.columna + 1] in Cerrados and not Nodos[NodoActual.fila][NodoActual.columna + 1] in Abiertos:
          Nodos[NodoActual.fila][NodoActual.columna+1].gcost(posiY,posiX)
          Nodos[NodoActual.fila][NodoActual.columna+1].heu(posmY,posmX)
          Nodos[NodoActual.fila][NodoActual.columna+1].padre=NodoActual
          Abiertos.append(Nodos[NodoActual.fila][NodoActual.columna+1])
        #nodo de la izquierda
      if not bordeizq:
        if Nodos[NodoActual.fila][NodoActual.columna - 1].esPasillo() and not Nodos[NodoActual.fila][NodoActual.columna - 1] in Cerrados and not Nodos[NodoActual.fila][NodoActual.columna - 1] in Abiertos: 
          Nodos[NodoActual.fila][NodoActual.columna-1].gcost(posiY,posiX)
          Nodos[NodoActual.fila][NodoActual.columna-1].heu(posmY,posmX)
          Nodos[NodoActual.fila][NodoActual.columna-1].padre=NodoActual
          Abiertos.append(Nodos[NodoActual.fila][NodoActual.columna - 1])
      
      if stop >=10000:  
        print("No se encotró la solución")
        break
      stop+=1 

      #UNA VEZ AGREGADOS LOS NODOS VECINOS A ABIERTOS:
      ##########################
      Cerrados.append(NodoActual) #AGREGO EL NODO ACTUAL A LOS CERRADOS
      Abiertos.remove(NodoActual)#ELIMINO EL NODO ACTUAL DE ABIERTOS
      Abiertos=ordenar(Abiertos) #ORDENO POR VALOR DE F
      NodoActual=Abiertos[0]#NODO ACTUAL ES EL DE MENOR F EN ABIERTOS
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
    stop=0
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
        if stop==5000:
            break
        stop+=1
    return subconjunto


def calcularCosto(orden, _NodosAux, _Inicio):
    costoT = []
    InicioAux = _Inicio
    for producto in orden:
        costoT.append(Algoritmo(Mapa, InicioAux,buscarProducto(_NodosAux, producto)))
        InicioAux = buscarProducto(_NodosAux, producto)
    costoT.append(Algoritmo(Mapa, buscarProducto(_NodosAux, producto), _Inicio))
    return sum(costoT[:])

########################### MAIN ##################################################################

Mapa = []
# 0     1     2     3     4     5     6     7     8     9    10     11    12    13    14   15    16     17
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P"," P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 0 PASILLO
Mapa.append([" P", " 0", " 1", " P", " P", "24", "25", " P", " P","48", "49", " P", " P", "72", "73", " P", " P", "96"])  # 1
Mapa.append([" P", " 2", " 3", " P", " P", "26", "27", " P", " P","50", "51", " P", " P", "74", "75", " P", " P", "97"])  # 2
Mapa.append([" P", " 4", " 5", " P", " P", "28", "29", " P", " P","52", "53", " P", " P", "76", "77", " P", " P", "98"])  # 3
Mapa.append([" P", " 6", " 7", " P", " P", "30", "31", " P", " P","54", "55", " P", " P", "78", "79", " P", " P", "99"])  # 4
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P"," P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 5 PASILLO
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P"," P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 6 PASILLO
Mapa.append([" P", " 8", " 9", " P", " P", "32", "33", " P", " P","56", "57", " P", " P", "80", "81", " P", " P", " P"])  # 7
Mapa.append([" P", "10", "11", " P", " P", "34", "35", " P", " P","58", "59", " P", " P", "82", "83", " P", " P", " P"])  # 8
Mapa.append([" P", "12", "13", " P", " P", "36", "37", " P", " P","60", "61", " P", " P", "84", "85", " P", " P", " P"])  # 9
Mapa.append([" P", "14", "15", " P", " P", "38", "39", " P", " P","62", "63", " P", " P", "86", "87", " P", " P", " P"])  # 10
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P"," P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 11 PASILLO
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P"," P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 12 PASILLO
Mapa.append([" P", "16", "17", " P", " P", "40", "41", " P", " P","64", "65", " P", " P", "88", "89", " P", " P", " P"])  # 13
Mapa.append([" P", "18", "19", " P", " P", "42", "43", " P", " P","66", "67", " P", " P", "90", "91", " P", " P", " P"])  # 14
Mapa.append([" P", "20", "21", " P", " P", "44", "45", " P", " P","68", "69", " P", " P", "92", "93", " P", " P", " P"])  # 15
Mapa.append([" P", "22", "23", " P", " P", "46", "47", " P", " P","70", "71", " P", " P", "94", "95", " P", " P", " P"])  # 16
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P"," P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 17 PASILLO

Inicio = [0, 0]
NodosAux = crearNodos(Mapa, Inicio, [1, 1]) # LO UTILIZO PARA BUSCAR LA UBICACION DE LOS PRODUCTOS
orden = [" 2", " 9", "36", "25", "11"," 4","54","62","88","94","44","40","70","82"]
cantidadEstados = math.factorial(len(orden)-1)
espacioBusqueda = cantidadEstados//2
estadosvisitados = []
Tgraf=[]
Cgraf=[]

T1=0.01
T = math.exp(-T1+6)
while T>0.1:
    print("T:", T)
    Tgraf.append(float(T))
    costoActual = calcularCosto(orden, NodosAux, Inicio)
    Cgraf.append(int(costoActual))
    while True:
        ordenAux = random.choice(estadosVecinos(orden[:], espacioBusqueda))
        for ordenes in estadosvisitados:
            if ordenAux == ordenes[0]:
                ordenAux = random.choice(
                    estadosVecinos(orden[:], espacioBusqueda))
        else:
            break
    costoSucesor = calcularCosto(ordenAux, NodosAux, Inicio)
    if costoActual >= costoSucesor:
        orden = ordenAux
        estadosvisitados.append([orden[:], costoSucesor])
        costoActual = costoSucesor
        #ESTADO VECINO ACEPTADO POR DELTA
    else:
        prob = random.uniform(0, 1)
        x = -abs(costoActual-costoSucesor)/T
        crit = math.exp(x)
        if prob <= crit:
            orden = ordenAux
            estadosvisitados.append([orden[:], costoSucesor])
            costoActual = costoSucesor
            #ESTADO VECINO ACEPTADO POR PROBABILIDAD
    T1 += 0.01
    T = math.exp(-T1+6)

mejorCosto=999
mejorVecino=[0,0]
for elementos in estadosvisitados:
    print(elementos)
    if elementos[1]<=mejorCosto: #elementos 1 es el costo
        mejorCosto=elementos[1]
        mejorVecino=elementos

print("ESTADO Y COSTO FINAL", estadosvisitados[len(estadosvisitados)-1])
print("MEJOR ESTADO Y COSTO ENCONTRADO",mejorVecino)

fig, ax = plt.subplots()
ax.plot(Tgraf, Cgraf)
plt.xscale("log")
plt.xlabel("Temperatura (°C)", size = 16)
plt.ylabel("Costo", size = 16)
ax.set_title("Evolucion de los costos en funcion del decrecimiento de T exponencial",loc="center")
ax.invert_xaxis()
plt.ylim([90,300])
plt.show()