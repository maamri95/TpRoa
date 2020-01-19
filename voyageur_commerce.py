from itertools import combinations
from time import perf_counter
import matplotlib.pyplot as plt

import numpy as np


def initialisation_graph(size):
    """
    creer un graphe aleatoire
    :param size: taille de graphe a construire
    :return: retourne la representation matricielle de graphe
    """
    graph = np.random.randint(-1, 10, (size, size))
    np.fill_diagonal(graph, -1)
    graph[graph == 0] = -1
    return graph


def tourne_possible(size):
    """
    calcule les chemins probale en evitant les chemins mirroir
    :param size: taille de graph
    :return: les chemins probable
    """
    return [list(item + (item[0],)) for item in list(combinations(range(size), size))]


def cout(solution, graph):
    """
    calcule le cout de chemin donne
    :param solution: chemin possible donne
    :param graph: representation matricielle de graph
    :return: le cout de chemin donne
    """
    cout_solution = 0
    for i in range(len(solution) - 1):
        x = int(solution[i])
        y = int(solution[i + 1])
        if graph[x][y] == -1:
            return -1
        cout_solution += graph[x][y]
    return cout_solution


def solution_optimal(graph):
    """
    recherche le chemin optimal pour le ghraphe donne
    :param graph: representation matricielle de graph
    :return: le chemin optimal
    """
    size = graph.shape[0]
    solution_possibles = np.array(tourne_possible(size))
    solution = solution_possibles[0]
    cout_optimal = cout(solution, graph)
    for sol in solution_possibles[1:]:
        cout_sol = cout(sol, graph)
        if cout_sol < cout_optimal:
            cout_optimal = cout_sol
            solution = sol
    return solution


def performance(sizes):
    """
    calcul la perfermance de la fonction de recherche selon la taille de graphe
    :param sizes: taille a compare
    :return: temps necessaire pour chaque taille
    """
    times = list()
    for size in sizes:
        graph = initialisation_graph(size)
        start = perf_counter()
        print(solution_optimal(graph))
        end = perf_counter()
        times.append(end - start)
    return sizes, times


def plot(sizes, times):
    """
        affiche un graphique des performance
        :param sizes: taille compare
        :param times: resultat en seconde des test
        :return:


    """
    plt.plot(sizes, times, label='voyageur de commerce')
    plt.grid()
    plt.legend(loc='upper left')
    plt.xlabel("taille de la matrice")
    plt.ylabel("complexite tomporelle (s)")
    plt.show()


if __name__ == '__main__':
    sizes = [4, 5, 6, 10]
    plot(*performance(sizes))
