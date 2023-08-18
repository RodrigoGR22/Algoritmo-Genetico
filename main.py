import random as rand
import numpy as np

def InitializeP(p):
    for i in range(int(POP_SIZE/2)):
        vivos[i] = True
        while True:
            j = rand.randint(0,n-1)
            if (carry[i] + weights[j]) > maxCarry:
                break
            else:
                carry[i] = carry[i] + weights[j]
                vo[i] = vo[i] + profits[j]
                p[i][j] = 1
    return p

def ProduceOffspring(p):
    for hijo in range (POP_SIZE):
        mutacion = False
        if rand.randint(1,100) >= 80:
          mutacion = True
          if vivos[hijo] == False:
              # hay uno muerto, debemos buscarle padres
              p1 = rand.randint(0, POP_SIZE - 1)
              while vivos[p1] == False:
                  p1 = rand.randint(0, POP_SIZE - 1)

              p2 = rand.randint(0, POP_SIZE - 1)
              while vivos[p2] == False or p1 == p2:
                  p2 = rand.randint(0, POP_SIZE - 1)

                  carry[hijo] = 0
                  vo[hijo] = 0
                  minVo = min(vo)
                  propP1 = 100 * (vo[p1] - minVo) / (vo[p1] + vo[p2] - minVo * 2)
                  for j in range(n):
                      if rand.randint(1, 100) <= propP1:
                          temp2 = p[p1][j]
                      else:
                          temp2 = p[p2][j]
                  if temp2 == 1:
                      if carry[hijo] + weights[j] <= maxCarry:
                          p[hijo][j] = 1
                          carry[hijo] = carry[hijo] + weights[j]
                          vo[hijo] = vo[hijo] + profits[j]
                      else:
                          p[hijo][j] = 0
                  else:
                      p[hijo][j] = 0
                      if mutacion == True:
                          if rand.randint(1, 100) >= 80:
                              # probabilidad de generar un 1 independiente de los padres
                              if carry[hijo] + weights[j] <= maxCarry:
                                  p[hijo][j] = 1
                                  carry[hijo] = carry[hijo] + weights[j]
                                  vo[hijo] = vo[hijo] + profits[j]
        #vivos[hijo] = True
    return p

def ElitistSelection(p):
    prom = np.average(vo)
    for i in range (POP_SIZE):
        if vo[i] < prom:
            vivos[i] = False
    return p


if __name__ == '__main__':
    f = open("instancia15.txt", "r")
    itersSinMejora = 0
    MAX_ITERS_SIN_MEJORA = 10

    rand.seed(127)
    line = f.readline()

    POP_SIZE = 400
    n, maxCarry = line.strip().split(" ")
    n = int(n)
    maxCarry = int(maxCarry)

    profits = []
    weights = []

    for linea in range(n):
        linea = f.readline()
        profit, weight = linea.strip().split(" ")
        profits.append(int(profit))
        weights.append(int(weight))

    print('Profits: ', profits)
    print('Weights: ', weights)

    p = [[0 for i in range(n)] for j in range(POP_SIZE)]
    vivos = [False for i in range(POP_SIZE)]
    vo = [0 for j in range(POP_SIZE)]
    carry = [0 for j in range(POP_SIZE)]


    bestGlobal = -1
    while itersSinMejora < MAX_ITERS_SIN_MEJORA:
        itersSinMejora += 1
        p = InitializeP(p)
        p = ProduceOffspring(p)
        p = ElitistSelection(p)
        bestIter = max(vo)
        #print(bestGlobal)
        if bestIter > bestGlobal:
            bestGlobal = bestIter
            itersSinMejora = 0

    print("Best vo = " + str(bestGlobal))
