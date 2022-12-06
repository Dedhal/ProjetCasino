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
    mise_max = 0
    mise_min = None
    partie = 0
    coup_moyen = 0
    coup_total = 0

    name_user = input("\t- Je suis Python. Quel est votre pseudo ? ")

    mc.rules(name_user)
    
    while True:
        print("\t- Votre solde: "+str(solde)+"e")
        
        mise = mc.fun_mise(solde)
        
        mise_moy.append(mise)
        
        nb_python = randint(1, DIFFICULTY[level][1])

        partie += 1
        
        
       
        print(nb_python)
        
        for nb_coup in range(DIFFICULTY[level][0]):
            
            nb_user = mc.user_input(DIFFICULTY[level][1])
                    
            if nb_user == nb_python:
                print("\t- Bravo, vous avez gagne !")
                
                # la mise la plus elevee
                mise_max = mise if mise > mise_max else mise_max
                print("\t- Mise la plus elevee: "+str(mise_max))

                # la mise la plus faible
                mise_min = mise if mise_min == None else mise if mise < mise_min else mise_min 
                #coups total
                coup_total += nb_coup
                # coup moyen par partie
                coup_moyen = (coup_total + nb_coup) / partie
                print("\t- Coup moyen par partie: "+str(coup_moyen))
                print("\t- Nombre de partie: "+str(partie))
                
                print("\t- Mise la plus faible: "+str(mise_min))
               
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
                
                # la mise la plus élevée 
                mise_max = mise if mise > mise_max else mise_max
                print("\t- Mise la plus elevee: "+str(mise_max))

                # la mise la plus faible
                mise_min = mise if mise_min == None else mise if mise < mise_min else mise_min 
                print("\t- Mise la plus faible: "+str(mise_min))
                #coup total
                coup_total += nb_coup

                # coup moyen par partie
                coup_moyen = (coup_total + nb_coup) / partie
                print("\t- Coup moyen par partie: "+str(coup_moyen))
                print("\t- Nombre de partie: "+str(partie))
                
                solde -= mise
                stats = mc.get_stats(mise_moy, nb_coup_moy)
                
                if level > 0:
                    level -= 1
                    mc.continuer()

            
        
        
        #print("")
            

    #mise_moy.append(mise)

    #nbre de partie total 

    #nbre de coup total

    
    

    
cnx = mysql.connector.connect(user="291957", password="eKy@SwM4Fe2ab6Z", host="mysql-casino-jmme.alwaysdata.net", database="casino-jmme_bdd")
print("Connexion successful !")
main()