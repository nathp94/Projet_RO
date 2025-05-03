# Algorithme d'Edmonds-Karp

from fonction import *


def successeurs(tab):
    n = len(tab)
    succ = []
    for i in range(n):
        succ_i = []
        for j in range(n):
            if tab[i][j] != 0:
                succ_i.append(j)
        succ.append(succ_i)
    return succ


def parcours_largeur(tab, succ):
    n = len(tab)
    Q = [0]  # File de parcours commence par s
    E = []  # Liste des sommets examinés
    parent = [-1] * n
    while n - 1 not in Q:  # Tant que t n'est pas parcouru
        if Q != []:
            for i in succ[Q[0]]:  # Analyser la tête de file
                if i not in Q and i not in E:
                    Q.append(i)  # Ajouter ses successeurs s'ils ne sont ni dans les files ni dans les sommets examinés
                    parent[i] = Q[0]  # Recorder pour chaque successeur son parent
            E.append(Q.pop(0))
            # print("Q :", Q)
            # print("Examiné :", E)
        else:
            return False
    return parent


def chaine_ameliorante(parent):
    n = len(parent)
    chemin = [n - 1]  # On part du sommet t
    while parent[chemin[-1]] != -1:  # Tant qu'on n'atteint pas le sommet source (0)
        chemin.append(parent[chemin[-1]])  # Ajouter son parent dans le chemin
    chemin.reverse()  # Inverser le chemin pour qu'il aille de s à t
    return chemin



def ameliorer(tabR, chaine):
    n = len(tabR)
    k = len(chaine)
    flot = 999
    for i in range(k - 1):
        if tabR[chaine[i]][chaine[i + 1]] < flot:
            flot = tabR[chaine[i]][chaine[i + 1]]
    print("Flot possible à augmenter :", flot, "\n")
    for i in range(k - 1):
        tabR[chaine[i]][chaine[i + 1]] -= flot
        tabR[chaine[i + 1]][chaine[i]] += flot
    return tabR, flot


def ford_fulkerson(tabR):
    i = 0
    flotmax = 0
    while True:
        print(f"Itération {i}", "——"*50)
        succ = successeurs(tabR)
        print("Successeur :", succ)
        parent = parcours_largeur(tabR, succ)
        print("Parent :", parent)
        if not parent:
            print("Il y a plus de chaîne améliorante.")
            print(f"Fin d'Itération", "——"*48, end="\n\n")
            return flotmax
        chaine = chaine_ameliorante(parent)
        print("Chaîne améliorante identifiée :", chaine)
        tabR, flot = ameliorer(tabR, chaine)
        afficher_matrice(tabR, 'r')
        flotmax += flot
        i += 1

def convertir_en_tab_flot(tabC, tabR):
    n = len(tabC)
    tabF = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tabF[i][j] = tabC[i][j] - tabR[i][j]
            if tabF[i][j] < 0 :
                tabF[i][j] = 0
    return tabF

