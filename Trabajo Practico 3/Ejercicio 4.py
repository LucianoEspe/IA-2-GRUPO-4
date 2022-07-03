import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)
def generar_datos_circulos(cantidad_ejemplos):
    x, t = make_circles(n_samples=cantidad_ejemplos, shuffle=True, 
    noise=0.1, random_state=40)
    return x, t

def generar_datos_clasificacion(cantidad_ejemplos, cantidad_clases):
    FACTOR_ANGULO = 0.79
    AMPLITUD_ALEATORIEDAD = 0.1

    # Calculamos la cantidad de puntos por cada clase, asumiendo la misma cantidad para cada 
    # una (clases balanceadas)
    n = int(cantidad_ejemplos / cantidad_clases)

    # Entradas: 2 columnas (x1 y x2)
    x = np.zeros((cantidad_ejemplos, 2))
    # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")

    randomgen = np.random.default_rng()

    # Por cada clase (que va de 0 a cantidad_clases)...
    for clase in range(cantidad_clases):
        # Tomando la ecuacion parametrica del circulo (x = r * cos(t), y = r * sin(t)), generamos 
        # radios distribuidos uniformemente entre 0 y 1 para la clase actual, y agregamos un poco de
        # aleatoriedad
        radios = np.linspace(0, 1, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)

        # ... y angulos distribuidos tambien uniformemente, con un desfasaje por cada clase
        angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n)

        # Generamos un rango con los subindices de cada punto de esta clase. Este rango se va
        # desplazando para cada clase: para la primera clase los indices estan en [0, n-1], para
        # la segunda clase estan en [n, (2 * n) - 1], etc.
        indices = range(clase * n, (clase + 1) * n)

        # Generamos las "entradas", los valores de las variables independientes. Las variables:
        # radios, angulos e indices tienen n elementos cada una, por lo que le estamos agregando
        # tambien n elementos a la variable x (que incorpora ambas entradas, x1 y x2)
        x1 = radios * np.sin(angulos)
        x2 = radios * np.cos(angulos)
        x[indices] = np.c_[x1, x2]

        # Guardamos el valor de la clase que le vamos a asociar a las entradas x1 y x2 que acabamos
        # de generar
        t[indices] = clase

    return x, t

def generar_datos_clasificacion_modificado(cantidad_ejemplos, cantidad_clases):
    FACTOR_ANGULO = 0.43
    AMPLITUD_ALEATORIEDAD = 0.12

    # Calculamos la cantidad de puntos por cada clase, asumiendo la misma cantidad para cada 
    # una (clases balanceadas)
    n = int(cantidad_ejemplos / cantidad_clases)

    # Entradas: 2 columnas (x1 y x2)
    x = np.zeros((cantidad_ejemplos, 2))
    # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")

    randomgen = np.random.default_rng()

    # Por cada clase (que va de 0 a cantidad_clases)...
    for clase in range(cantidad_clases):
        # Tomando la ecuacion parametrica del circulo (x = r * cos(t), y = r * sin(t)), generamos 
        # radios distribuidos uniformemente entre 0 y 1 para la clase actual, y agregamos un poco de
        # aleatoriedad
        radios = np.linspace(0, 1, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)

        # ... y angulos distribuidos tambien uniformemente, con un desfasaje por cada clase
        angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n)

        # Generamos un rango con los subindices de cada punto de esta clase. Este rango se va
        # desplazando para cada clase: para la primera clase los indices estan en [0, n-1], para
        # la segunda clase estan en [n, (2 * n) - 1], etc.
        indices = range(clase * n, (clase + 1) * n)

        # Generamos las "entradas", los valores de las variables independientes. Las variables:
        # radios, angulos e indices tienen n elementos cada una, por lo que le estamos agregando
        # tambien n elementos a la variable x (que incorpora ambas entradas, x1 y x2)
        x1 = radios * np.sin(angulos)
        x2 = radios * np.cos(angulos)
        x[indices] = np.c_[x1, x2]

        # Guardamos el valor de la clase que le vamos a asociar a las entradas x1 y x2 que acabamos
        # de generar
        t[indices] = clase

    return x, t

def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):
    randomgen = np.random.default_rng()

    w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))

    w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
    b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}


def ejecutar_adelante(x, pesos):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]

    # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
    h = np.maximum(0, z)

    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}


def clasificar(x, pesos):
    # Corremos la red "hacia adelante"
    resultados_feed_forward = ejecutar_adelante(x, pesos)
    
    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
    # (es decir, por filas)
    max_scores = np.argmax(resultados_feed_forward["y"], axis=1)

    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return max_scores#[:, 0]

# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x, t,x_prueba,t_prueba,x_validacion,t_validacion, pesos, learning_rate, epochs,validacion):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0) 
    precision_val_anterior=None
    for i in range(epochs):
        # Ejecucion de la red hacia adelante
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]

        # LOSS
        # a. Exponencial de todos los scores
        exp_scores = np.exp(y)

        # b. Suma de todos los exponenciales de los scores, fila por fila (ejemplo por ejemplo).
        #    Mantenemos las dimensiones (indicamos a NumPy que mantenga la segunda dimension del
        #    arreglo, aunque sea una sola columna, para permitir el broadcast correcto en operaciones
        #    subsiguientes)
        sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)

        # c. "Probabilidades": normalizacion de las exponenciales del score de cada clase (dividiendo por 
        #    la suma de exponenciales de todos los scores), fila por fila
        p = exp_scores / sum_exp_scores

        # d. Calculo de la funcion de perdida global. Solo se usa la probabilidad de la clase correcta, 
        #    que tomamos del array t ("target")
        loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))

        # Mostramos solo cada 1000 epochs
        if i %1000 == 0:
            print("Loss epoch", i, ":", loss)
            cantidad_ejemplos=np.size(x, 0)
            precision=0
            mejor_neurona=np.argmax(y, axis=1)
            for j in range(cantidad_ejemplos):
                if mejor_neurona[j]==t[j]:
                    precision+=1
            precision=precision/cantidad_ejemplos
            print("Precision:", precision)
        # Extraemos los pesos a variables locales
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dy = p                # Para todas las salidas, L' = p (la probabilidad)...
        dL_dy[range(m), t] -= 1  # ... excepto para la clase correcta
        dL_dy /= m

        dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
        dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2

        dL_dh = dL_dy.dot(w2.T)
        
        dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
        dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)

        dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
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
        if i %validacion==0:
            cantidad_ejemplos_validacion=np.size(x_validacion, 0)
            resultados_validacion=clasificar(x_validacion, pesos)
            precision_validacion=0
            for j in range(cantidad_ejemplos_validacion):
                if resultados_validacion[j]==t_validacion[j]:
                    precision_validacion+=1
            precision_validacion=precision_validacion/cantidad_ejemplos_validacion
            print(f"\nPrecision validacion epoch {i}:", precision_validacion)
            if precision_val_anterior==None:
                precision_val_anterior=precision_validacion
            elif precision_validacion<precision_val_anterior*0.96:
                print("Entrenamiento terminado")
                break
            else:
                precision_val_anterior=precision_validacion
    #probar precision con x_prueba y t_prueba
    cantidad_ejemplos_prueba=np.size(x_prueba, 0)
    resultados=clasificar(x_prueba, pesos)
    precision_prueba=0
    for j in range(cantidad_ejemplos_prueba):
        if resultados[j]==t_prueba[j]:
            precision_prueba+=1
    precision_prueba=precision_prueba/cantidad_ejemplos_prueba
    print("Precision prueba:", precision_prueba)


def iniciar(generador,numero_clases, numero_ejemplos, graficar_datos):
    # Generamos datos    
    if generador=="original":
        x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases)
        cantidad_ejemplos_pruebas=int(numero_ejemplos*0.2)
        x_prueba, t_prueba = generar_datos_clasificacion(cantidad_ejemplos_pruebas, numero_clases)
        x_validacion,t_validacion=generar_datos_clasificacion(cantidad_ejemplos_pruebas, numero_clases)
    if generador=="modificado":
        x, t = generar_datos_clasificacion_modificado(numero_ejemplos, numero_clases)
        cantidad_ejemplos_pruebas=int(numero_ejemplos*0.2)
        x_prueba, t_prueba = generar_datos_clasificacion_modificado(cantidad_ejemplos_pruebas, numero_clases)
        x_validacion,t_validacion=generar_datos_clasificacion_modificado(cantidad_ejemplos_pruebas, numero_clases)
    elif generador=="circulos":
        x, t = generar_datos_circulos(numero_ejemplos)
        cantidad_ejemplos_pruebas=int(numero_ejemplos*0.2)
        x_prueba, t_prueba = generar_datos_circulos(cantidad_ejemplos_pruebas)
        x_validacion,t_validacion=generar_datos_circulos(cantidad_ejemplos_pruebas)
    # Graficamos los datos si es necesario
    if graficar_datos:
        # Parametro: "c": color (un color distinto para cada clase en t)
        plt.scatter(x[:, 0], x[:, 1], c=t)
        plt.show()

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 2
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)

    # Entrena
    LEARNING_RATE=1
    EPOCHS=10000
    VALIDACION=500
    train(x, t,x_prueba,t_prueba,x_validacion,t_validacion, pesos, LEARNING_RATE, EPOCHS, VALIDACION)

#GENERADOR DE DATOS (CIRCULOS)
iniciar("circulos",numero_clases=2, numero_ejemplos=200, graficar_datos=True)

iniciar("circulos",numero_clases=2, numero_ejemplos=300, graficar_datos=True)

#GENERADOR DE DATOS MODIFICADO
iniciar("modificado",numero_clases=2, numero_ejemplos=300, graficar_datos=True)

iniciar("modificado",numero_clases=4, numero_ejemplos=400, graficar_datos=True)

#GENERADOR DE DATOS ORIGINAL
iniciar("original",numero_clases=2, numero_ejemplos=300, graficar_datos=True)

iniciar("original",numero_clases=5, numero_ejemplos=500, graficar_datos=True)

iniciar("original",numero_clases=7, numero_ejemplos=300, graficar_datos=True)

