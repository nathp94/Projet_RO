import time
from algoEK import *
from algoBF import *
from algoPR import *




import numpy as np
import random
import matplotlib.pyplot as plt



def generate_random_flow_problem(n):
    # Initialisation des matrices C et D avec des zéros
    C = np.zeros((n, n), dtype=int)
    D = np.zeros((n, n), dtype=int)

    # Nombre total d'arêtes possibles sans la diagonale
    total_edges = n * n // 2

    # Génération des arêtes de capacité et de coût aléatoires
    for _ in range(total_edges):
        i, j = random.sample(range(n), 2)

        # Assigner une capacité aléatoire entre 1 et 100
        capacity = random.randint(1, 100)
        C[i, j] = capacity

        # Assigner un coût aléatoire entre 1 et 100 uniquement si la capacité est non nulle
        if capacity > 0:
            cost = random.randint(1, 100)
            D[i, j] = cost

    # Conversion en listes de listes
    return C.tolist(), D.tolist()







def afficher_colonne_verticale(temps, n,nom):
    """
    Affiche un nuage de points alignés verticalement à une position x donnée.
    """

    x = [n] * len(temps)
    y = temps

    plt.figure(figsize=(4, 6))
    plt.scatter(x, y, color='red', marker='o', label="Temps (s)")
    plt.title(nom)
    plt.xlabel('n')
    plt.ylabel("Temps (secondes)")
    plt.grid(True, axis='y')
    plt.xticks([n])  # montrer uniquement la colonne
    plt.legend()
    plt.tight_layout()
    plt.show()

def creation_plot():
    liste_dure_ff = []
    liste_dure_min = []
    liste_dure_pr = []
 
    for taille in [10,20,40]:
        for i in range(100):
            debut = time.perf_counter()
            C, D = generate_random_flow_problem(taille)

            tabR = [i[:] for i in C]
            flotmax = ford_fulkerson(tabR)
            fin = time.perf_counter()
            duree = fin - debut
            liste_dure_ff.append(duree)

            debut = time.perf_counter()
            flot_a_cout_minimal(C, D, flotmax/2)
            fin = time.perf_counter()
            duree = fin - debut
            liste_dure_min.append(duree)

            debut = time.perf_counter()
            algo_pousser_reetiqueter(C)
            fin = time.perf_counter()
            duree = fin - debut
            liste_dure_pr.append(duree)

        afficher_colonne_verticale(liste_dure_ff,taille,"flot_max_ff")
        afficher_colonne_verticale(liste_dure_min,taille,"flot_min")
        afficher_colonne_verticale(liste_dure_pr,taille,"flot_max_pr")


