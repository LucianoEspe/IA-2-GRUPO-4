import numpy as np
from matplotlib import pyplot as plt

class Entrada:
    def __init__(self,inicio):
        self.inicio=inicio
        self.conborroso={'NG': None ,'NP': None,'Z': None,'PP': None,'PG': None} 
        self.pertenencia={'NG': None ,'NP': None,'Z': None,'PP': None,'PG': None}
    def obtenerPertenencia(self,valor,deltaT):
        conjuntos=['NG','NP','Z','PP','PG']
        for terminos in conjuntos:
            self.pertenencia[terminos]=self.conborroso[terminos][int((valor+abs(self.inicio))/deltaT)]
class Salida:
    def __init__(self,inicio):
        self.inicio=inicio
        self.conborroso={'NG': None ,'NP': None,'Z': None,'PP': None,'PG': None} 
        self.pertenencia={'NG': None ,'NP': None,'Z': None,'PP': None,'PG': None}
        self.centro={'NG': None ,'NP': None,'Z': None,'PP': None,'PG': None} #NECESITO LOS CENTROS PARA EL DESBORROSIFICADOR

def particionBorrosa(nombre,minimo,maximo,centro,rango):
    funcion=[]
    for i in rango:
            if nombre=="NG":
                if i<=minimo:
                    y=1
                elif (i>minimo and i<=maximo):
                    y=1-(i-minimo)/(maximo-minimo)
                else:
                    y=0
                funcion.append(y)
            elif nombre=="PG":
                if i<=minimo:
                    y=0
                elif (i>minimo and i<=maximo):
                    y=(i-minimo)/(maximo-minimo)
                else:
                    y=1
                funcion.append(y)
            else:
                if (i>=minimo and i<centro):
                    y=(i-minimo)/(centro-minimo)
                elif (i>=centro and i<maximo):
                    y=1-(i-centro)/(maximo-centro)
                else:
                    y=0
                funcion.append(y)
    return funcion

def borrosificador(velocidad,valVel,xvel,angulo,valAng,xang,fuerza,valFue,xfuer):

    conjuntos=['NG','NP','Z','PP','PG']
    iter=0
    for terminos in conjuntos:
        velocidad.conborroso[terminos]=particionBorrosa(terminos,valVel[iter][0],valVel[iter][1],valVel[iter][2],xvel)
        angulo.conborroso[terminos]=particionBorrosa(terminos,valAng[iter][0],valAng[iter][1],valAng[iter][2],xang)
        fuerza.conborroso[terminos]=particionBorrosa(terminos,valFue[iter][0],valFue[iter][1],valFue[iter][2],xfuer)
        fuerza.centro[terminos]=valFue[iter][2]
        iter=iter+1

def calcula_aceleracion(angulo, v, F):

    M = 2  # Masa del carro
    m = 1  # Masa de la pertiga
    l = 1  # Longitud de la pertiga
    g = 9.81

    numerador = g * np.sin(angulo) + np.cos(angulo) * \
        ((F - m * l * np.power(v, 2) * np.sin(angulo)) / (M + m))
    denominador = l * (4/3 - (m * np.power(np.cos(angulo), 2) / (M + m)))
    return (numerador / float(denominador))

def graficar(yang0, yvel0, yacel0,yang,yvel,yacel):
    fig, ax = plt.subplots(2, 3,figsize=(10,10))
    ax[0,0].plot(tiempo, yang0)

    ax[0,0].set(xlabel='tiempo (s)', ylabel='angulo 0',title=f'Delta t = {delta_t} s')
    ax[0,0].grid()

    ax[0,1].plot(tiempo, yvel0)
    ax[0,1].set(xlabel='tiempo (s)', ylabel='velocidad 0',
            title=f'Delta t = {delta_t} s')
    ax[0,1].grid()

    ax[0,2].plot(tiempo, yacel0)
    ax[0,2].set(xlabel='tiempo (s)', ylabel='aceleracion 0',
            title=f'Delta t = {delta_t} s')
    ax[0,2].grid()

    ax[1,0].plot(tiempo, yang)

    ax[1,0].set(xlabel='tiempo (s)', ylabel='angulo',title=f'Delta t = {delta_t} s')
    ax[1,0].grid()

    ax[1,1].plot(tiempo, yvel)
    ax[1,1].set(xlabel='tiempo (s)', ylabel='velocidad',
            title=f'Delta t = {delta_t} s')
    ax[1,1].grid()

    ax[1,2].plot(tiempo, yacel)
    ax[1,2].set(xlabel='tiempo (s)', ylabel='aceleracion',
            title=f'Delta t = {delta_t} s')
    ax[1,2].grid()
    fig.tight_layout()
    plt.show()
def baseConocimiento(ang,vel):
    """
        angulo  NG  NP   Z   PP  PG
    velocidad | -------------------
            NG| NG  NG  NG   NP   Z
                --------------------
            NP| NG  NG  NP    Z  PP
                --------------------
            Z | NG  NP   Z   PP  PG
                --------------------
            PP| NP   Z  PP   PG  PG
                --------------------
            PG|  Z  PP  PG   PG  PG
    """
    angulo.obtenerPertenencia(ang, delta_t)
    velocidad.obtenerPertenencia(vel, delta_t)

    fuerza.pertenencia['NG'] = max(min(angulo.pertenencia['NG'], velocidad.pertenencia['NG']), min(angulo.pertenencia['NP'], velocidad.pertenencia['NG']), min(angulo.pertenencia['Z'], velocidad.pertenencia['NG']), min(
            angulo.pertenencia['NG'], velocidad.pertenencia['NP']), min(angulo.pertenencia['NP'], velocidad.pertenencia['NP']), min(angulo.pertenencia['NG'], velocidad.pertenencia['Z']))
    fuerza.pertenencia['NP'] = max(min(angulo.pertenencia['PP'], velocidad.pertenencia['NG']), min(angulo.pertenencia['Z'], velocidad.pertenencia['NP']), min(
        angulo.pertenencia['NP'], velocidad.pertenencia['Z']), min(angulo.pertenencia['NG'], velocidad.pertenencia['PP']))
    fuerza.pertenencia['Z'] = max(min(angulo.pertenencia['PG'], velocidad.pertenencia['NG']), min(angulo.pertenencia['PP'], velocidad.pertenencia['NP']), min(
        angulo.pertenencia['Z'], velocidad.pertenencia['Z']), min(angulo.pertenencia['NP'], velocidad.pertenencia['PP']), min(angulo.pertenencia['NG'], velocidad.pertenencia['PG']))
    fuerza.pertenencia['PP'] = max(min(angulo.pertenencia['PG'], velocidad.pertenencia['NP']), min(angulo.pertenencia['PP'], velocidad.pertenencia['Z']), min(
        angulo.pertenencia['Z'], velocidad.pertenencia['PP']), min(angulo.pertenencia['NP'], velocidad.pertenencia['PG']))
    fuerza.pertenencia['PG'] = max(min(angulo.pertenencia['PG'], velocidad.pertenencia['Z']), min(angulo.pertenencia['PG'], velocidad.pertenencia['PP']), min(angulo.pertenencia['PG'], velocidad.pertenencia['PG']), min(
        angulo.pertenencia['PP'], velocidad.pertenencia['PP']), min(angulo.pertenencia['PP'], velocidad.pertenencia['PG']), min(angulo.pertenencia['Z'], velocidad.pertenencia['PG']))
def desborrosificador(fuerza):
    num = 0
    den = 0
    for indice, i in fuerza.pertenencia.items():
        num += i*fuerza.centro[indice]
        den += i
    return (num/float(den))


############### MAIN ###################
delta_t=0.01
anguloInicial = 45
vel = 0                             #VALORES INICIALES
acel = 0
ang = (anguloInicial * np.pi) / 180  
F=0

ang0 = ang
vel0 = vel
acel0 = acel

yvel0=[]
yang0=[]
yacel0=[]

yvel=[]
yang=[]
yacel=[]

### BORROSIFICACION ################################################################################
### SE DEFINEN LOS INTERVALOS PARA CADA PARTICION BORROSA (minimo,maximo,centro)                   #
valoresVelocidad=[(-20,-10,-10),(-20, 0, -10),(-10, 10, 0),(0, 20, 10),(10, 20, 10)]               #
valoresAngulo=[(-20,-10,-10),(-20, 0, -10),(-10, 10, 0),(0, 20, 10),(10, 20, 10)]                  #
valoresFuerza=[(-200, -100, -100),(-200, 0, -100),(-100, 100, 0),(0, 200, 100),(100, 200, 100)]    #
in_vel=-300                                                                                        #
xv = np.arange(in_vel, 300, delta_t)                                                               #
in_theta=-90                                                                                       #
xa = np.arange(in_theta, 90, delta_t)   
in_fuer=-300                                                                                        #
xf = np.arange(in_vel, 300, delta_t)                                                            #
velocidad=Entrada(in_vel)                                                                          #
angulo=Entrada(in_theta)                                                                           #
fuerza=Salida(in_vel)                                                                              #
borrosificador(velocidad,valoresVelocidad,xv,angulo,valoresAngulo,xa,fuerza,valoresFuerza,xf)         #    
####################################################################################################
fig, ax = plt.subplots(3,1)
conjuntos=['NG','NP','Z','PP','PG']
for terminos in conjuntos:
    ax[0].plot(xa,angulo.conborroso[terminos])
    ax[1].plot(xv,velocidad.conborroso[terminos])
    ax[2].plot(xf,fuerza.conborroso[terminos])
ax[0].set(xlabel='Entrada Nitida', ylabel='Pertenencia',title='Conjunto Borroso Angulo')
ax[0].grid()
ax[1].set(xlabel='Entrada Nitida', ylabel='Pertenencia',title='Conjunto Borroso Velocidad')
ax[1].grid()
ax[2].set(xlabel='Entrada Nitida', ylabel='Pertenencia',title='Conjunto Borroso Fuerza')
ax[2].grid()
fig.tight_layout()
plt.show()

tiempo=np.arange(0,10,delta_t)
for t in tiempo:
    #### SIN EL CONTROLADOR DIFUSO ####
    acel0 = calcula_aceleracion(ang0, vel0, 0)
    vel0 = vel0 + acel0 * delta_t
    ang0 = ang0 + vel0 * delta_t + acel0 * np.power(delta_t, 2) / 2

    yang0.append(ang0)
    yvel0.append(vel0)
    yacel0.append(acel0)
    #### CON EL CONTROLADOR DIFUSO ####
    acel = calcula_aceleracion(ang, vel, F)
    vel = vel + acel * delta_t
    ang = ang + vel * delta_t + acel * np.power(delta_t, 2) / 2

    yang.append(ang)
    yvel.append(vel)
    yacel.append(acel)
    baseConocimiento(ang,vel)
    F = desborrosificador(fuerza)

graficar(yang0,yvel0,yacel0,yang,yvel,yacel)
