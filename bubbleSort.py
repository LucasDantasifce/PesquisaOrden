from random import randint
from timeit import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import variables

def GeraLista(tam):
    Lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in Lista: Lista.append(n)
    return Lista

def DesenhaGrafi(x,y,name, yl = "Tempo", xl = "Tamanho"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = " ")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)
    plt.show()


def bubbleSort(Sortlist):
    tam = len(Sortlist)
    swap = 0
    swapped = True
    while swapped:
        swapped = False
        for index in range(tam):
            for i in range(0, tam-index-1):
                if Sortlist[i] > Sortlist[i+1]:
                    Sortlist[i], Sortlist[i+1] = Sortlist[i+1], Sortlist[i]
                    swapped = True
                    swap += 1
    variables.numSwaps = swap
    print(swap)


larg = [10000,20000,30000,40000,50000]
tempo = []
swaps = []

for comp in larg:
    listSort = GeraLista(comp)
    swaps.append(variables.numSwaps)
    tempo.append(timeit("bubbleSort({})".format(listSort),setup="from __main__ import bubbleSort",number=1))
   

print(swaps)

DesenhaGrafi(larg,swaps,"swaps.png","Swaps")
DesenhaGrafi(larg,tempo,"tempo.png")
