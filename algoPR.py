def initialiser(capacites, source):
    n = len(capacites)
    residuel = [row.copy() for row in capacites]
    hauteur = [0] * n
    hauteur[source] = n
    excedent = [0] * n
    flot = [[0] * n for _ in range(n)]

    for v in range(n):
        if residuel[source][v] > 0:
            delta = residuel[source][v]
            flot[source][v] = delta
            flot[v][source] = -delta
            excedent[v] += delta
            excedent[source] -= delta
            residuel[source][v] = 0
            residuel[v][source] = delta
            print(f"Initialisation : envoi de {delta} unité(s) depuis la source {source} vers {v}")
            
    return residuel, hauteur, excedent, flot

def pousser(u, residuel, excedent, flot, hauteur):
    n = len(residuel)
    for v in range(n):
        if excedent[u] > 0 and residuel[u][v] > 0 and hauteur[u] == hauteur[v] + 1:
            delta = min(excedent[u], residuel[u][v])
            flot[u][v] += delta
            flot[v][u] = -flot[u][v]
            residuel[u][v] -= delta
            residuel[v][u] += delta
            excedent[u] -= delta
            excedent[v] += delta
            print(f"Flux de {delta} propagé de {u} vers {v} (hauteur {hauteur[u]} → {hauteur[v]})")
            return True
    return False

def reetiqueter(u, residuel, hauteur):
    n = len(residuel)
    min_h = float('inf')
    for v in range(n):
        if residuel[u][v] > 0:
            min_h = min(min_h, hauteur[v])
    if min_h < float('inf'):
        print(f"Réétiquetage : hauteur du sommet {u} passe de {hauteur[u]} à {min_h + 1}")
        hauteur[u] = min_h + 1

def afficher_matrice_flot(flot, capacites):
    print("\nMatrice des flots (format flot/capacité) :")
    n = len(flot)
    for u in range(n):
        ligne = []
        for v in range(n):
            if capacites[u][v] > 0:
                ligne.append(f"{flot[u][v]}/{capacites[u][v]}")
            else:
                ligne.append(" 0 ")
        print(" ".join(f"{val:>5}" for val in ligne))

def algo_pousser_reetiqueter(capacites):
    source = 0
    puits = len(capacites)-1
    print('--- Pousser-Réétiqueter ---')
    residuel, hauteur, excedent, flot = initialiser(capacites, source)
    n = len(capacites)

    actifs = [u for u in range(n) if u not in (source, puits) and excedent[u] > 0]

    while actifs:
        u = max(actifs, key=lambda x: (hauteur[x], -x))
        if not pousser(u, residuel, excedent, flot, hauteur):
            reetiqueter(u, residuel, hauteur)
        actifs = [v for v in range(n) if v not in (source, puits) and excedent[v] > 0]

    flot_max = sum(flot[source][v] for v in range(n))
    afficher_matrice_flot(flot, capacites)
    print(f"Flot maximal (Pousser-Réétiqueter) = {flot_max}")
    return flot_max

