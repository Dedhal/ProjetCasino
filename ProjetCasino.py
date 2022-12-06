# -*- encoding: utf-8 -*-

from random import randint
import numpy as np
import mysql.connector

def rules(name_user):
    print("\t- Hello " + name_user + ", vous avez 10e, Tres bien ! Installez vous SVP a la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n")
    print("\t- Je viens de penser a un nombre entre 1 et 10. Devinez lequel ?\n")
    print("\t- Att : vous avez le droit a trois essais !\n")
    print("\t- Si vous devinez mon nombre des le premier coup, vous gagnez le double de votre mise !\n")
    print("\t- Si vous le devinez au 2e coup, vous gagnez exactement votre mise !\n")
    print("\t- Si vous le devinez au 3e coup, vous gagnez la moitie de votre mise !\n")
    print("\t- Si vous ne le devinez pas au 3e coup, vous perdez votre mise et vous avez le droit :\n")
    print("\t\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquerir le level perdu.\n")
    print("\t\t- de quitter le jeu.\n")
    print("\t- Des que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level superieur.\n")

def user_input(max):
    nb_user = input("\t- Alors mon nombre est : ")
    while True:
        try:
            nb_user = int(nb_user)
            if(nb_user < 1 or nb_user > max):
                break
            else:
                raise ValueError
        
        except ValueError:
            nb_user = input("\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et "+str(max)+" : ")
    
def continuer():
    while True:
        on = input("\t- Voulez vous continuer a jouer ? (O/N)")
        if on == "O":
            break
        elif on == "N":
            print("\t- A bientot !")
            exit(0)
        else:    
            continue
        
def fun_mise(solde):
    mise = input("\t- Le jeu commence, entrez votre mise : ")
    while True:
        try:
            mise = int(mise)
            if(mise > solde):
                raise ValueError
            break
        except ValueError:
            mise = input("\t- Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et "+str(solde)+"e : ")

    return mise

def get_stats(mise_moy, nb_coup_moy):
    np.array(mise_moy)
    np.array(nb_coup_moy)
    return np.mean(mise_moy), np.mean(nb_coup_moy)
    

def main():
    mise_moy = []
    nb_coup_moy = []
    DIFFICULTY = [(3, 10), (5, 20), (7,30)]
    DOTATION = 10
    solde = DOTATION
    level = 0

    name_user = input("\t- Je suis Python. Quel est votre pseudo ? ")
    rules(name_user)
    
    while True:
        print("\t- Votre solde: "+str(solde)+"e")
        
        mise = fun_mise(solde)
        
        mise_moy.append(mise)
        
        nb_python = randint(1, DIFFICULTY[level][1])
        print(nb_python)
        
        for nb_coup in range(DIFFICULTY[level][0]):
            
            nb_user = user_input(DIFFICULTY[level][1])
                    
            if nb_user == nb_python:
                print("\t- Bravo, vous avez gagne !")
                nb_coup_moy.append(nb_coup+1)
                if nb_coup == 0:
                    solde += mise * 2
                    print("\t- Vous avez gagne le double de votre mise !")
                    if level + 1 < 3:
                        level += 1
                        continuer()
                elif nb_coup == 1:
                    solde += mise
                    print("\t- Vous avez gagne votre mise !")
                    if level + 1 < 3:
                        level += 1
                        continuer()
                else:
                    solde += mise / 2
                    print("\t- Vous avez gagne la moitie de votre mise !")
                    if level + 1 < 3:
                        level += 1
                        continuer()
                        print("\t- Super ! Vous passez au Level "+str(level)+".")
                break
            elif nb_user > nb_python and (DIFFICULTY[level][0] - nb_coup - 1) > 0:
                print("\t- Votre nbre est trop grand !\n")
                print("\t- Il vous reste " + str(DIFFICULTY[level][0] - nb_coup - 1) + " essais !\n")
            elif nb_user < nb_python and (DIFFICULTY[level][0] - nb_coup - 1) > 0:
                print("\t- Votre nbre est trop petit !\n")
                print("\t- Il vous reste " + str(DIFFICULTY[level][0] - nb_coup - 1) + " essais !\n")
            else:
                print("\t- Vous avez perdu ! Mon nombre est "+str(nb_python)+" !")
                solde -= mise
                stats = get_stats(mise_moy, nb_coup_moy)
                print("")
                if level > 0:
                    level -= 1
                    continuer()
                
        
        #print("")
            

    #mise_moy.append(mise)

    
    

    
cnx = mysql.connector.connect(user="291957", password="eKy@SwM4Fe2ab6Z", host="mysql-casino-jmme.alwaysdata.net", database="casino-jmme_bdd")
print("Connexion successful !")
main()