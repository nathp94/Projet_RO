# Project Théorie des Graphes: Ordonnancement
# Professeur: Noureddine BENTHAMI
# Mars 2025

# Par Bastien Peltier, Nathan Pégé, Sébastien XU, Maxence Durand, Matthieu Bachelerie




# Initialisation

def lire_proposition(chemin_fichier):
    fichier = open(chemin_fichier, 'r', encoding='utf-8')
    lignes = fichier.readlines()

    n = int(lignes[0].strip())

    tabC = []
    for i in lignes[1:1 + n]:
        l = list(map(int, i.strip().split(' ')))
        tabC.append(l)

    tabD = []
    for i in lignes[1 + n:]:
        l = list(map(int, i.strip().split(' ')))
        tabD.append(l)

    return n, tabC, tabD


def afficher_matrice(mat, type):
    if not mat:
        return False
    width = len(mat) * 4 + 3
    if type == 'c':
        print(f"{'GRAPHE RÉSIDUEL':-^{width}}")
    elif type == 'd':
        print(f"{'TABLEAU DE COÛT':-^{width}}")
    elif type == 'f':
        print(f"{'TABLEAU DE FLOT':-^{width}}")
    headers = list(range(len(mat)))
    print('\t', end='')
    for header in headers:
        print(header, end='\t')
    print()
    for i in range(len(mat)):
        print(headers[i], end='\t')
        for j in range(len(mat[i])):
            print(mat[i][j], end='\t')
        print()
    print(f"{'-' * width}")
    print()


def afficher_proposition(n, tabC, tabD):
    print("Nombre de sommets: " + str(n) + "\n")
    afficher_matrice(tabC, 'c')
    afficher_matrice(tabD, 'd')







# Juste pour ajouter un peu de couleurs ...
def print_red(message):
    # Code d'échappement ANSI pour définir la couleur du texte sur rouge vif (91)
    print("\033[1;91m",end="")  # Rouge vif
    print(message, end="")
    print("\033[0m")

def print_blue(message):
    print("\033[1;34m", end="")  # Bleu clair
    print(message, end="")
    print("\033[0m")

def print_yellow(message):
    print("\033[1;93m", end="")  # Jaune vif
    print(message, end="")
    print("\033[0m")

def print_green(message):
    print("\033[1;32m", end="")
    print(message, end="")
    print("\033[0m")

def print_light_green(message):
    print("\033[1;92m", end="")
    print(message, end="")
    print("\033[0m")

# Demande à l'utilisateur de choisir un tableau
def choix_tableau():
    while True:
        try:
            print_light_green("\nVeuillez choisir un tableau de 1 à 14")
            print_yellow("0: Quitter le programme")
            choix = int(input(">>> "))

            if choix == 0:
                return False

            if 1 <= choix <= 14:
                return choix
            else :
                print_red("\n>>> Veuillez saisir un nombre ENTIER valide <<<\n")

        except ValueError:
            print_red("\n>>> Veuillez saisir un nombre ENTIER valide <<<\n")


# Demande à l'utilisateur de choisir une action à afficher
def choix_action(num,n):
    while True:
        try:
            # Affichage utilisateur
            print_green("\n=====================       Menu Principal       =====================\n")
            print("Numéro :", num, "\n")
            print_light_green("Le graphe est un graphe d’ordonnancement valide.")

            print("1: Afficher les rangs des sommets")
            print("2: Afficher les calendriers au plus tôt")
            print("3: Afficher les calendriers au plus tard")
            print("4: Afficher les marges")
            print("5: Afficher le(s) chemin(s) critique(s)")
            print_yellow("0: Changer de problème\n")
            print_light_green("\nVeuillez choisir une action de 1 à 5")
            choix = int(input(">>> "))

            if choix == 0:
                return False
            if 1 <= choix <= 5:
                return choix
            else :
                print_red("\n>>> Veuillez saisir un nombre ENTIER valide <<<\n")

        except ValueError:
            print_red("\n>>> Veuillez saisir un nombre ENTIER valide <<<\n")