from time import perf_counter_ns
import matplotlib.pyplot as plt
from scipy.sparse import random
from numpy import sum


def matrice_crose(sizes):
    """
    fonction qui calcul la perfermance de la fonction somme d'une matrice crose avec et sans les item nulle
    selon la taille de graphe
    :param sizes: taille a compare
    :return: temps necessaire pour chaque taille
    """
    complexite_matrice = list()
    complexite_vecteur = list()
    for size in sizes:
        matrice = random(size, size, 0.1).A  # genere une matrice sizexsize avec 90% d'element null
        vecteur = matrice[matrice > 0]  # extraction des element non nulle
        debute_matrice = perf_counter_ns()
        print("la somme matricielle de {} = {}".format(size, round(sum(matrice), 2)))
        fin_matrice = perf_counter_ns()
        complexite_matrice.append((fin_matrice - debute_matrice) / 1000)
        debute_vecteur = perf_counter_ns()
        print("la somme vecteurielle de {} = {}".format(size, round(sum(vecteur), 2)))
        fin_vecteur = perf_counter_ns()
        complexite_vecteur.append((fin_vecteur - debute_vecteur) / 1000)
    return complexite_matrice, complexite_vecteur, sizes


def plot(complexite_matrice, complexite_vecteur, sizes):
    """
    affiche un graphique des performance
    :param complexite_matrice: resultat des preformances de calcul sur une matrice
    :param complexite_vecteur: resultat des preformances de calcul sur un vecteur
    :param sizes: taille compare
    :return: un ghraphique
    """
    plt.plot(sizes, complexite_matrice, 'r', label="complexite avec matrice")
    plt.plot(sizes, complexite_vecteur, 'b--', label="complexite avec vecteur")
    plt.legend(loc='upper left')
    plt.xlabel("taille de la matrice")
    plt.ylabel("complexite tomporelle (µs)")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    sizes = [3, 5, 9, 12, 15, 20]
    plot(*matrice_crose(sizes))
