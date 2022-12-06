# -*- encoding: utf-8 -*-

from random import randint
import mysql.connector
import moduleCasino as mc

def main():
    mise_moy = []
    nb_coup_moy = []
    DIFFICULTY = [(3, 10), (5, 20), (7,30)]
    DOTATION = 10
    solde = DOTATION
    level = 0

    name_user = input("\t- Je suis Python. Quel est votre pseudo ? ")
    mc.rules(name_user)
    
    while True:
        print("\t- Votre solde: "+str(solde)+"e")
        
        mise = mc.fun_mise(solde)
        
        mise_moy.append(mise)
        
        nb_python = randint(1, DIFFICULTY[level][1])
        print(nb_python)
        
        for nb_coup in range(DIFFICULTY[level][0]):
            
            nb_user = mc.user_input(DIFFICULTY[level][1])
                    
            if nb_user == nb_python:
                print("\t- Bravo, vous avez gagne !")
                nb_coup_moy.append(nb_coup+1)
                if nb_coup == 0:
                    solde += mise * 2
                    print("\t- Vous avez gagne le double de votre mise !")
                    if level + 1 < 3:
                        level += 1
                        mc.continuer()
                elif nb_coup == 1:
                    solde += mise
                    print("\t- Vous avez gagne votre mise !")
                    if level + 1 < 3:
                        level += 1
                        mc.continuer()
                else:
                    solde += mise / 2
                    print("\t- Vous avez gagne la moitie de votre mise !")
                    if level + 1 < 3:
                        level += 1
                        mc.continuer()
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
                stats = mc.get_stats(mise_moy, nb_coup_moy)
                print("")
                if level > 0:
                    level -= 1
                    mc.continuer()
                
        
        #print("")
            

    #mise_moy.append(mise)

    
    

    
cnx = mysql.connector.connect(user="291957", password="eKy@SwM4Fe2ab6Z", host="mysql-casino-jmme.alwaysdata.net", database="casino-jmme_bdd")
print("Connexion successful !")
main()