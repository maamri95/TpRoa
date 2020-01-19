import numpy as np
from numpy.random import randint
from time import perf_counter_ns
import matplotlib.pyplot as plt


def isEulerien(graphe):
    """
    fonction de reconnaissance de graphe eulerien
    :param graphe: graphe a test
    :return: reponds a la question Est ce un graphe Eulerien
    """
    size = graphe.shape[0]
    dis = graphe.sum(axis=0)
    count = dis[dis % 2 == 0].sum()
    return count == size


def performance(sizes):
    """
    fonction qui calcul la perfermance de la fonction de reconnaissance de graphe eulerien
    selon la taille de graphe
    :param sizes: taille a compare
    :return: temps necessaire pour chaque taille
    """
    times = list()
    for size in sizes:
        graphe = randint(0, 2, (size, size))
        np.fill_diagonal(graphe, 0)
        start = perf_counter_ns()
        if isEulerien(graphe):
            print("le graphe de taille {} est un graphe eulerien".format(size))
        else:
            print("le graphe de taille {} n'est pas un graphe eulerien".format(size))
        end = perf_counter_ns()
        times.append((end - start)/1000)
    return sizes, times


def plot(sizes, times):
    """
    affiche un graphique des performance
    :param sizes: taille compare
    :param times: resultat en microseconde des test
    :return: ghraphique
    """
    plt.plot(sizes, times, label='cycle eulerien')
    plt.grid()
    plt.legend(loc='upper left')
    plt.xlabel("taille de la matrice")
    plt.ylabel("complexite tomporelle (µs)")
    plt.show()


if __name__ == '__main__':
    sizes = [5, 10, 15, 20, 25]
    plot(*performance(sizes))
