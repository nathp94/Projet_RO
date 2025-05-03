# Project Théorie des Graphes: Ordonnancement
# Professeur: Noureddine BENTHAMI
# Mars 2025

# Par Bastien Peltier, Nathan Pégé, Sébastien XU, Maxence Durand, Matthieu BACHELERIE

# Import
from fonction import *
from algoEK import *
from algoBF import *
from algoPR import *

def main():

    start = True
    while start != False:

        print_blue("\n===== Recherche Opérationnelle =====")

        # Affichage utilisateur
        num = choix_tableau()

        if num == False:
            start = False
            print_blue("\nMerci de votre utilisation, à bientôt !")

        else:
            # Lecture des fichiers txt
            n, tabC, tabD = lire_proposition(f'graphe/flot {num}.txt')
            afficher_proposition(n, tabC, tabD)





            # Affichage utilisateur
            print_green("\n=====================       Menu Principal       =====================\n")
            print("Numéro :", num, "\n")

            if tabD !=[]: # Cas où on fait un problème de flot min
                print_yellow("Il s'agit d'un problème de flot à coût minimal")

                print_light_green("\nVeuillez choisir une valeur de flot : ")

                flot_demande = int(input(">>> "))
                resultat = flot_a_cout_minimal(tabC, tabD, flot_demande)
                if resultat[0]:
                    flot, envoye, cout_total = resultat
                    print(f"\n Flot total envoyé : {envoye}")
                    print(f" Coût total minimal : {cout_total}")
                    print(" Matrice du flot final :")
                    for ligne in flot:
                        print(ligne)
                else:
                    print(
                        f"\n Impossible d'envoyer {flot_demande} unités. Seulement {resultat[1]} unités ont pu être envoyées.")
                    print(f" Coût partiel : {resultat[2]}")



            else: # Cas où on fait un problème de flot max
                print_yellow("Il s'agit d'un problème de flot max")
                print_light_green("\nVeuillez choisir Un algorithme : ")
                print_green("1 - Algorithme de Edmonds-Karp")
                print_green("2 - Algorithme pousser-réétiqueter ")
                val = int(input(">>> "))
                if val == 1:
                    afficher_proposition(n, tabC, tabD)
                    tabR = [i[:] for i in tabC]
                    afficher_matrice(tabR, 'r')

                    flotmax = ford_fulkerson(tabR)
                    print("La valeur maximale de flot est :", flotmax)
                    tabF = convertir_en_tab_flot(tabC, tabR)
                    afficher_matrice(tabF, 'f')
                else :
                    algo_pousser_reetiqueter(tabC)

# Lancement du programme
if __name__ == "__main__":
    # Lancement du programme
    main()
