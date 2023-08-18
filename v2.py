import random

# Generar población inicial de manera aleatoria
def generar_individuo():
    return [random.choice([0, 1]) for _ in range(len(pesos))]

# Definir función objetivo
def funcion_objetivo(individuo):
    valor_total = sum(individuo[i] * valores[i] for i in range(len(individuo)))
    peso_total = sum(individuo[i] * pesos[i] for i in range(len(individuo)))
    #print(pesos,'  ',peso_total,'  ', capacidad_mochila)
    if peso_total < capacidad_mochila:
        valor_total = 0  # Penalizar soluciones inválidas
    return valor_total

# Realizar selección por torneo binario
def torneo_binario(poblacion, aptitudes):
    participantes = random.sample(range(len(poblacion)), 2)
    indice_participante1, indice_participante2 = participantes[0], participantes[1]
    aptitud_participante1 = aptitudes[indice_participante1]
    aptitud_participante2 = aptitudes[indice_participante2]
    if aptitud_participante1 > aptitud_participante2:
        return poblacion[indice_participante1]
    else:
        return poblacion[indice_participante2]

# Realizar el cruce de dos individuos
def cruzar(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 1)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    return hijo

# Aplicar mutación a un individuo
def mutar(individuo):
    indice_mutacion = random.randint(0, len(individuo) - 1)
    individuo[indice_mutacion] = 1 - individuo[indice_mutacion]


if __name__ == '__main__':
    f = open("instancia3.txt", "r")

    itersSinMejora = 0
    MAX_ITERS_SIN_MEJORA = 10

    random.seed(127)
    line = f.readline()

    tamano_poblacion = 400
    n, capacidad_mochila = line.strip().split(" ")
    n = int(n)
    capacidad_mochila = int(capacidad_mochila)

    # Definir los parámetros del problema de la mochila
    #pesos = [10, 20, 30, 40, 50]  # Pesos de los objetos
    #valores = [60, 100, 120, 140, 160]  # Valores de los objetos
    #capacidad_mochila = 100  # Capacidad total de la mochila

    # Definir parámetros del algoritmo genético
    #tamano_poblacion = 100
    num_generaciones = 50
    tasa_mutacion = 0.1

    valores = []
    pesos = []

    for linea in range(n):
        linea = f.readline()
        profit, weight = linea.strip().split(" ")
        valores.append(int(profit))
        pesos.append(int(weight))

    poblacion = []
    for _ in range(tamano_poblacion):
        individuo = generar_individuo()
        poblacion.append(individuo)

    for generacion in range(num_generaciones):
        # Evaluar la aptitud de cada individuo en la población
        aptitudes = [funcion_objetivo(individuo) for individuo in poblacion]

        # Seleccionar individuos para reproducción (torneo binario)
        nueva_poblacion = []
        for _ in range(tamano_poblacion):
            padre1 = torneo_binario(poblacion, aptitudes)
            padre2 = torneo_binario(poblacion, aptitudes)
            hijo = cruzar(padre1, padre2)
            nueva_poblacion.append(hijo)

        # Aplicar operador de mutación
        for individuo in nueva_poblacion:
            if random.random() < tasa_mutacion:
                mutar(individuo)
        # Reemplazar la población antigua por la nueva generada
        poblacion = nueva_poblacion

        # Obtener el mejor individuo de la última generación
        mejor_individuo = max(poblacion, key=funcion_objetivo)

        # Imprimir el resultado
    print("Mejor individuo:", mejor_individuo)
    print("Valor total:", funcion_objetivo(mejor_individuo))