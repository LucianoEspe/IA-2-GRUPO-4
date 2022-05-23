class Nodo():
    def __init__(self, _fila, _columna,_nombre):
        self.columna = _columna
        self.fila = _fila
        self.nombre=_nombre
        self.inicio = False
        self.meta = False
        self.pasillo = False
        self.estante = False
        self.padre=None
        self.g=1
        self.h=9999999
        self.f=9999999


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

    def heu(self,filaO,columnaO):
        self.h=abs(self.fila-filaO)+abs(self.columna-columnaO)
        self.f=self.h+self.g
    
    def gcost(self,fila_inicial, columna_inicial): 
        self.g= abs(fila_inicial-self.fila)+abs(columna_inicial-self.columna)
      
def ordenar(lista):
  lista.sort(key=lambda x:x.f)
  return lista
  
def crearNodos(Mapa,_Meta):
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
    numero=0
    for filas in Mapa:
        for columna, valor in enumerate(Mapa[fila]):
            if valor == " P":
                nodo = Nodo(fila,columna,"P"+str(numero))
                numero+=1
                nodo.crearPasillo()
                nodo.heu(_Meta[0],_Meta[1])
                Nodos[fila][columna] = nodo
            elif valor == " I":
                nodo = Nodo(fila,columna,valor)
                nodo.crearInicio()
                nodo.heu(_Meta[0],_Meta[1])
                Nodos[fila][columna] = nodo
            elif valor == " M":
                nodo = Nodo(fila,columna,valor)
                nodo.crearMeta()
                nodo.heu(_Meta[0],_Meta[1])
                Nodos[fila][columna] = nodo
            else:
                nodo = Nodo(fila,columna,valor)
                nodo.crearEstante()
                nodo.heu(_Meta[0],_Meta[1])
                Nodos[fila][columna] = nodo
        fila += 1
    return Nodos



def AlgoritmoAestrella(Mapa,Meta,posiY,posiX,posmY,posmX):
  Nodos = crearNodos(Mapa,Meta)
  
  Abiertos = [] #Sucesores sin explorar, ordenados en forma creciente de f
  Cerrados = [] #Nodos ya explorados
  
  for filas in Nodos:
    for nodo in filas:
      if nodo.esInicio():
          Abiertos.append(nodo)
          nodo.gcost(posiY, posiX) #da 0, costo desde el actual al nodo raíz
          nodo.heu(posmY,posmX) #costo desde el actual a la meta
  
  
  #Para comprobar que no busque en los bordes 
  bordesup=False
  bordeinf=False
  bordeizq=False
  bordeder=False
  
  if Abiertos[0].fila==0:
    bordesup=True
  if Abiertos[0].fila==17:
    bordeinf=True
  if Abiertos[0].columna==0:
    bordeizq=True
  if Abiertos[0].columna==17:
    bordeder=True
    ## Para agregar los sucesores iniciales
    #nodo de abajo
  if Abiertos[0].fila < 17 and Nodos[Abiertos[0].fila + 1][Abiertos[0].columna].esPasillo() and not bordeinf:
    Nodos[Abiertos[0].fila + 1][Abiertos[0].columna].gcost(posiY,posiX)
    Nodos[Abiertos[0].fila + 1][Abiertos[0].columna].heu(posmY,posmX)
    Nodos[Abiertos[0].fila + 1][Abiertos[0].columna].padre=Abiertos[0]
    Abiertos.append(Nodos[Abiertos[0].fila + 1][Abiertos[0].columna])
  #nodo de arriba
  if Abiertos[0].fila > 0 and Nodos[Abiertos[0].fila - 1][Abiertos[0].columna].esPasillo() and not bordesup: 
    Nodos[Abiertos[0].fila - 1][Abiertos[0].columna].gcost(posiY,posiX)
    Nodos[Abiertos[0].fila - 1][Abiertos[0].columna].heu(posmY,posmX)
    Nodos[Abiertos[0].fila - 1][Abiertos[0].columna].padre=Abiertos[0]
    Abiertos.append(Nodos[Abiertos[0].fila - 1][Abiertos[0].columna])
  #nodo a la derecha
  if Abiertos[0].columna < 17 and Nodos[Abiertos[0].fila][Abiertos[0].columna + 1].esPasillo() and not bordeder:
    Nodos[Abiertos[0].fila][Abiertos[0].columna+1].gcost(posiY,posiX)
    Nodos[Abiertos[0].fila][Abiertos[0].columna+1].heu(posmY,posmX)
    Nodos[Abiertos[0].fila][Abiertos[0].columna+1].padre=Abiertos[0]
    Abiertos.append(Nodos[Abiertos[0].fila][Abiertos[0].columna+1])  
    #nodo de la izquierda
  if Abiertos[0].columna > 0 and Nodos[Abiertos[0].fila][Abiertos[0].columna - 1].esPasillo() and not bordeizq: 
    Nodos[Abiertos[0].fila][Abiertos[0].columna-1].gcost(posiY,posiX)
    Nodos[Abiertos[0].fila][Abiertos[0].columna-1].heu(posmY,posmX)
    Nodos[Abiertos[0].fila][Abiertos[0].columna-1].padre=Abiertos[0]
    Abiertos.append(Nodos[Abiertos[0].fila][Abiertos[0].columna - 1])  
  #########################
  #EL INICIAL YA LO USAMOS ARRIBA PARA ENCONTRAR LOS VECINOS INICIALES
  #POR ESO CREO QUE YA NO DEBERIA ESTAR EN NINGUN LADO
  #O DE ULTIMA EN CERRADOS, PERO DEBERIAMOS ARRANCAR DESPUES CON EL CERRADOS[1]
  Cerrados.append(Abiertos[0])#AÑADE EL INICIAL A CERRADOS (YA EXPLORADO)
  Abiertos.remove(Abiertos[0])#SE ELIMINA EL INICIAL
  Abiertos=ordenar(Abiertos)#SE ORDENAN LOS VECINOS AGREGADOS
  NodoActual=Abiertos[0]#MEJOR VECINO
  stop=0
  print("Nodo Inicial [",Cerrados[0].fila,"][",Cerrados[0].columna,"]\n")
  while True:
    print("Nodo Actual [",NodoActual.fila,"][",NodoActual.columna,"]")
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
      
    #Verificacion de meta alcanzada
    if  (Nodos[NodoActual.fila + 1][NodoActual.columna].esMeta() and not bordeinf) or (Nodos[NodoActual.fila - 1][NodoActual.columna].esMeta()  and not bordesup) or (Nodos[NodoActual.fila][NodoActual.columna + 1].esMeta() and not bordeder ) or (Nodos[NodoActual.fila][NodoActual.columna - 1].esMeta() and not bordeizq):
      Camino=[]
      print("META ALCANZADA")
      print("CAMINO MAS CORTO:")
      while NodoActual is not None:
        Camino.append("["+str(NodoActual.fila)+"]["+str(NodoActual.columna)+"]")
        NodoActual=NodoActual.padre
      Camino=list(reversed(Camino))
      for elementos in Camino:
        print(elementos)
      break
      
    #nodo de abajo
    if  Nodos[NodoActual.fila + 1][NodoActual.columna].esPasillo() and not bordeinf and not Nodos[NodoActual.fila + 1][NodoActual.columna] in Cerrados and not Nodos[NodoActual.fila + 1][NodoActual.columna] in Abiertos:
      Nodos[NodoActual.fila + 1][NodoActual.columna].gcost(posiY,posiX)
      Nodos[NodoActual.fila + 1][NodoActual.columna].heu(posmY,posmX)
      Nodos[NodoActual.fila + 1][NodoActual.columna].padre=NodoActual
      Abiertos.append(Nodos[NodoActual.fila + 1][NodoActual.columna])
  
    #nodo de arriba
    if  Nodos[NodoActual.fila - 1][NodoActual.columna].esPasillo() and not bordesup and not Nodos[NodoActual.fila - 1][NodoActual.columna] in Cerrados and not Nodos[NodoActual.fila - 1][NodoActual.columna] in Abiertos: 
      Nodos[NodoActual.fila - 1][NodoActual.columna].gcost(posiY,posiX)
      Nodos[NodoActual.fila - 1][NodoActual.columna].heu(posmY,posmX)
      Nodos[NodoActual.fila - 1][NodoActual.columna].padre=NodoActual
      Abiertos.append(Nodos[NodoActual.fila - 1][NodoActual.columna])
    #nodo a la derecha
    if Nodos[NodoActual.fila][NodoActual.columna + 1].esPasillo() and not bordeder and not  Nodos[NodoActual.fila][NodoActual.columna + 1] in Cerrados and not Nodos[NodoActual.fila][NodoActual.columna + 1] in Abiertos:
      Nodos[NodoActual.fila][NodoActual.columna+1].gcost(posiY,posiX)
      Nodos[NodoActual.fila][NodoActual.columna+1].heu(posmY,posmX)
      Nodos[NodoActual.fila][NodoActual.columna+1].padre=NodoActual
      Abiertos.append(Nodos[NodoActual.fila][NodoActual.columna+1])
      #nodo de la izquierda
    if Nodos[NodoActual.fila][NodoActual.columna - 1].esPasillo() and not bordeizq and not Nodos[NodoActual.fila][NodoActual.columna - 1] in Cerrados and not Nodos[NodoActual.fila][NodoActual.columna - 1] in Abiertos: 
      Nodos[NodoActual.fila][NodoActual.columna-1].gcost(posiY,posiX)
      Nodos[NodoActual.fila][NodoActual.columna-1].heu(posmY,posmX)
      Nodos[NodoActual.fila][NodoActual.columna-1].padre=NodoActual
      Abiertos.append(Nodos[NodoActual.fila][NodoActual.columna - 1])
    
    if stop >=10000:  
      print("No se encotró la solución")
      break
    stop+=1 
    print("Iteracion numero:",stop)
  
    ##########################
    #UNA VEZ AGREGADOS LOS NODOS VECINOS A ABIERTOS:
    ##########################
    Cerrados.append(NodoActual) #AGREGO EL NODO ACTUAL A LOS CERRADOS
    Abiertos.remove(NodoActual)#ELIMINO EL NODO ACTUAL DE ABIERTOS
    Abiertos=ordenar(Abiertos) #ORDENO POR VALOR DE F
    NodoActual=Abiertos[0]#NODO ACTUAL ES EL DE MENOR F EN ABIERTOS

    
####################################### MAIN #########################################################

    
Mapa = []
############## 0     1     2     3     4     5     6     7     8     9    10     11    12    13    14   15    16     17
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 0 PASILLO 
Mapa.append([" P", " 0", " 1", " P", " P", "24", "25", " P", " P", "48", "49", " P", " P", "72", "73", " P", " P", "96"])  # 1
Mapa.append([" P", " 2", " 3", " P", " P", "26", "27", " P", " P", "50", "51", " P", " P", "74", "75", " P", " P", "97"])  # 2
Mapa.append([" P", " 4", " 5", " P", " P", "28", "29", " P", " P", "52", "53", " P", " P", "76", "77", " P", " P", "98"])  # 3
Mapa.append([" P", " 6", " 7", " P", " P", "30", "31", " P", " P", "54", "55", " P", " P", "78", "79", " P", " P", "99"])  # 4
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 5 PASILLO
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 6 PASILLO
Mapa.append([" P", " 8", " 9", " P", " P", "32", "33", " P", " P", "56", "57", " P", " P", "80", "81", " P", " P", " P"])  # 7
Mapa.append([" P", "10", "11", " P", " P", "34", "35", " P", " P", "58", "59", " P", " P", "82", "83", " P", " P", " P"])  # 8
Mapa.append([" P", "12", "13", " P", " P", "36", "37", " P", " P", "60", "61", " P", " P", "84", "85", " P", " P", " P"])  # 9
Mapa.append([" P", "14", "15", " P", " P", "38", "39", " P", " P", "62", "63", " P", " P", "86", "87", " P", " P", " P"])  # 10
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 11 PASILLO
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 12 PASILLO
Mapa.append([" P", "16", "17", " P", " P", "40", "41", " P", " P", "64", "65", " P", " P", "88", "89", " P", " P", " P"])  # 13
Mapa.append([" P", "18", "19", " P", " P", "42", "43", " P", " P", "66", "67", " P", " P", "90", "91", " P", " P", " P"])  # 14
Mapa.append([" P", "20", "21", " P", " P", "44", "45", " P", " P", "68", "69", " P", " P", "92", "93", " P", " P", " P"])  # 15
Mapa.append([" P", "22", "23", " P", " P", "46", "47", " P", " P", "70", "71", " P", " P", "94", "95", " P", " P", " P"])  # 16
Mapa.append([" P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P", " P"])  # 17 PASILLO

while True:
    print("Ingrese coordenada Y del inicio (FILA) (Entrada al almacén): ")
    posiY = int(input())
    print("Ingrese coordenada X del inicio (COLUMNA)(Entrada al almacén): ")
    posiX = int(input())
    if  Mapa[posiY][posiX] == " P" and (posiY==0 or posiX==0 or posiY == 17 or posiX == 17) and posiY<=17 and posiX <=17: 
        Mapa[posiY][posiX] = " I"
        Inicio=[posiY,posiX]
        break
    else:
        print ("El inicio no puede estar encima de un producto. Debe estar en los laterales del almacén")

while True:
    print("Ingrese coordenada Y de la meta (FILA) (Producto a buscar): ")
    posmY = int(input())
    print("Ingrese coordenada X de la meta (COLUMNA) (Producto a buscar): ")
    posmX = int(input())
    if  Mapa[posmY][posmX] != " P" and posmY<=17 and posmX <=17:
        Mapa[posmY][posmX] = " M"
        Meta=[posmY,posmX]
        break
    else:
        print ("La meta debe ser la posición de un producto.")
        
AlgoritmoAestrella(Mapa,Meta,posiY,posiX,posmY,posmX)
