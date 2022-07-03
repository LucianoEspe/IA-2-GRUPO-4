import numpy as np
import matplotlib.pyplot as plt
from random import randint


# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)

def generar_datos_regresion(cantidad_ejemplos):
    AMPLITUD_ALEATORIEDAD = 0.5

    x = np.zeros((cantidad_ejemplos, 1))

    t = np.zeros((cantidad_ejemplos,1)) 

    randomgen = np.random.default_rng()

    # Se generan datos aleatorios siguiendo una linea recta como valor medio 
    x1 = np.linspace(0, 5, cantidad_ejemplos)

    x2 = np.power(x1,2) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=cantidad_ejemplos)

    # Generamos un rango con los subindices de cada punto generado.
    indices = range(0, cantidad_ejemplos)

    #Matriz de ejemplos
    x1.sort()           #Ordenamos en orden creciente las abcisas
    x[indices] = np.c_[x1] 

    t[indices] = np.c_[x2]

    return x, t



def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):
    randomgen = np.random.default_rng()

    w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))

    w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
    b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}


def ejecutar_adelante(x, pesos, sig):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]

    #agregar sigmoide!!
    if sig:
        h=sigmoid(z)
    # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
    else:
        h = np.maximum(0, z)

    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}


def clasificar(x, pesos, sig):
    # Corremos la red "hacia adelante"
    resultados_feed_forward = ejecutar_adelante(x, pesos, sig)
    
    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
    # (es decir, por filas)

    y = resultados_feed_forward["y"]

    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return y #[:, 0]

# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x, t, x_prueba, t_prueba, x_validacion, t_validacion, pesos, learning_rate, epochs, validacion, sig):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0)
    
    prevLoss = None   # precision minima de prediccion
    
    for i in range(epochs):
        # Ejecucion de la red hacia adelante
        resultados_feed_forward = ejecutar_adelante(x, pesos, sig)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]

        #---------MSE-------
        #ERROR CUADRATICO
        L = np.power((t - y), 2)

        #PROMEDIO DE LOS ERRORES
        loss = (1 / m) * np.sum(L)
        
        if i % validacion == 0:
            print()
            print("Entrenamiento Loss epoch", i, ":", loss)

            mm = np.size(x_validacion, 0)

            resultados = clasificar(x_validacion, pesos, sig)
            L_validacion = np.power((t_validacion - resultados), 2)
            loss_validacion = (1 / mm) * np.sum(L_validacion)
            print("Validacion Loss epoch", i, ":", loss_validacion)

            if prevLoss==None:
                prevLoss = loss_validacion
            elif loss_validacion<=prevLoss:
                prob = randint(0, 100)/100
                
                #Aplicar probabilidad de parada temprana
                if prob<(i/epochs): 
                    plt.scatter(x_validacion[:, 0], resultados)
                    plt.title("Aproximacion de validacion")
                    plt.show()
                    break
                else:
                    prevLoss = loss_validacion
            else:
                prevLoss = loss_validacion
    
        # Extraemos los pesos a variables locales
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dy = y-t     
        dL_dy = dL_dy*(2/m)

        dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
        dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2

        dL_dh = dL_dy.dot(w2.T)       
        #SIGMOIDE
        if sig:
            dL_dz = dL_dh *sigmoid(z)*(1-sigmoid(z))
        else:
            dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
            dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)


        dL_dw1 = x.T.dot(dL_dz)                   # Ajuste para w1
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1

        # Aplicamos el ajuste a los pesos
        w1 += -learning_rate * dL_dw1
        b1 += -learning_rate * dL_db1
        w2 += -learning_rate * dL_dw2
        b2 += -learning_rate * dL_db2

        # Actualizamos la estructura de pesos
        # Extraemos los pesos a variables locales
        pesos["w1"] = w1
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2

    mm = np.size(x_prueba, 0)
    resultados = clasificar(x_prueba, pesos, sig)
    L_test = np.power((t_prueba - resultados), 2)
    loss_test = (1 / mm) * np.sum(L_test)
    print("Testeo Loss epoch ",i,":",loss_test)
    plt.scatter(x_prueba[:, 0], resultados)
    plt.title("Test")
    plt.show()
    print(f"Entrenamiento terminado: {i} epochs")

    
#implementacion SIGMOIDE
def sigmoid(x):
    sig = np.where(x < 0, np.exp(x)/(1 + np.exp(x)), 1/(1 + np.exp(-x)))
    return sig   
    

def iniciar(numero_clases, numero_ejemplos, graficar_datos, sig=False):
    # Generamos datos (80/20)
    x, t = generar_datos_regresion(round(numero_ejemplos*0.8))
    x_validacion, t_validacion = generar_datos_regresion(round(numero_ejemplos*0.2))
    x_prueba, t_prueba = generar_datos_regresion(round(numero_ejemplos*0.2))

    # Graficamos los datos si es necesario
    if graficar_datos:
        plt.scatter(x[:, 0], t)
        plt.show()

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100    
    NEURONAS_ENTRADA = 1

    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)

    # Entrena
    LEARNING_RATE=0.1 #DEJAR EN 0.1
    EPOCHS=10000  
    VALIDACION = 500
    train(x, t, x_prueba, t_prueba, x_validacion, t_validacion, pesos, LEARNING_RATE, EPOCHS, VALIDACION, sig)


iniciar(numero_clases=1, numero_ejemplos=300, graficar_datos=True, sig=True)