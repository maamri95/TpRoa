from time import perf_counter
import matplotlib.pyplot as plt
from numpy.random import randint
from numpy import sum, array


def solution_possible(nombre_object):
    """
    :param nombre_object: nombre_object disponible
    :return: toute les combinison d'objet possible
    """
    tmp = [bin(x).split("b")[1] for x in range(2 ** nombre_object)]
    tmp = ["0" * (nombre_object - len(x)) + x for x in tmp]
    return array([[int(x) for x in y] for y in tmp])


def sac_a_dos(poidsmax, objets, poids, valeurs):
    utilmax = 0
    solution_optimale = []
    for possibilite in objets:
        if sum(possibilite * poids) <= poidsmax:
            util = sum(possibilite * valeurs)
            if util > utilmax:
                solution_optimale = possibilite
                utilmax = util
    return array([x for x in [(x+1)*y for x, y in enumerate(solution_optimale[:-1])] if x != 0])


def performance(nbr_objects):
    times = list()
    for n in nbr_objects:
        poidsmax, objets, poids, valeurs = randint(100, 250), solution_possible(n), randint(0, 10, n), randint(0, 10, n)
        start = perf_counter()
        print(sac_a_dos(poidsmax, objets, poids, valeurs))
        end = perf_counter()
        times.append(end - start)
    return nbr_objects, times


def plot(nbr_objects, times):
    plt.plot(nbr_objects, times, label='sac a dos')
    plt.grid()
    plt.legend(loc='upper left')
    plt.xlabel("taille de la matrice")
    plt.ylabel("complexite tomporelle (s)")
    plt.show()


if __name__ == '__main__':
    nombre_objects = [5, 10, 15, 20]
    plot(performance(nombre_objects))
