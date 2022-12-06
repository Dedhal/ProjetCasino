# -*- encoding: utf-8 -*-

from asyncio.windows_events import NULL
from random import randint
import datetime
import mysql.connector
import moduleCasino as mc
from babel.dates import format_date

def main():
    mise_moy = []
    mise_max = 0
    mise_min = None
    nb_win_first_try = 0
    DIFFICULTY = [(3, 10), (5, 20), (7,30)]
    DOTATION = 10
    solde = DOTATION
    level = 0
    partie = 0
    coup_moyen = 0
    coup_total = 0

    name_user = input("\t- Je suis Python. Quel est votre pseudo ? ")

    sql_check_if_user_exist = """SELECT 
    count(`name`) AS exist, name, solde, timestamp, nb_mise, mise_total, level_max,	level_actual,	
    nb_win_first_try, nb_win, nb_lose, gain_max, mise_max, mise_min, coup_total, nb_parties FROM `user` WHERE name = %s"""
    value = name_user
    cur.execute(sql_check_if_user_exist, (value,))
    myresult = cur.fetchone()

    if myresult[0] > 0:
        name_user = myresult[1]
        solde = myresult[2]
        date = myresult[3]
        nb_mise = myresult[4]
        mise_total = myresult[5]
        level_max = myresult[6]
        level = myresult[7]
        nb_win_first_try = myresult[7]
        nb_win = myresult[8]
        nb_lose = myresult[9]
        gain_max = myresult[10]
        mise_max = myresult[11]
        mise_min = myresult[12]
        coup_total = myresult[13]
        partie = myresult[14]
        
        
        print("\t- Votre derniere connexion remonte au", format_date(date, format='long', locale='fr'))
        mc.update_date(cur, cnx, name_user)
    else: 
        mc.create_user(cur, cnx, name_user, DOTATION)
        mc.rules(name_user, DIFFICULTY, level)
    
    while True:
        
        print("\t- Votre solde: "+str(solde)+"e")
        
        print("\n----------------------------NIVEAU "+str(level+1)+"----------------------------\n")
        
        mise, solde = mc.fun_mise(solde)
        mc.update_solde(cur, cnx, solde, name_user)

        mise_max = mise if mise > mise_max else mise_max
        mc.update_mise_max(cur, cnx, mise_max, name_user)
        print("\t- Mise la plus elevee: "+str(mise_max))
            
        mise_min = mise if mise_min == None else mise if mise < mise_min else mise_min
        mc.update_mise_min(cur, cnx, mise_min, name_user)
        print("\t- Mise la plus faible: "+str(mise_min))
        
        nb_python = randint(1, DIFFICULTY[level][1])
        partie += 1
        print(nb_python)
        
        for nb_coup in range(DIFFICULTY[level][0]):
            
            nb_user = mc.user_input(DIFFICULTY[level][1])
                    
            if nb_user == nb_python:
                print("\t- Bravo, vous avez gagne !")
                #coups total
                coup_total += nb_coup +1
                mc.set_coups_parties(cur, cnx, coup_total, partie, name_user)
                # coup moyen par partie
                coup_moyen = coup_total / partie
                print("\t- Coup moyen par partie: "+str(coup_moyen))
                print("\t- Nombre de partie: "+str(partie))
                if nb_coup == 0:
                    nb_win_first_try += 1
                    mc.update_nb_win_first_try(cur, cnx, nb_win_first_try, name_user)
                    if nb_win_first_try == 1:
                        print("\t- Vous avez reussi a trouver le bon nombre des le premier coup a "+str(nb_win_first_try)+" reprise")
                    else:
                        print("\t- Vous avez reussi a trouver le bon nombre des le premier coup a "+str(nb_win_first_try)+" reprises")
                    solde += mise * 2
                    mc.update_solde(cur, cnx, solde, name_user)
                    print("\t- Vous avez gagne le double de votre mise !")
                    if level + 1 < 3:
                        level += 1
                    mc.set_level_max(level, level_max, cur, cnx, name_user)
                    mc.continuer()
                elif nb_coup == 1:
                    solde += mise
                    mc.update_solde(cur, cnx, solde, name_user)
                    print("\t- Vous avez gagne votre mise !")
                    if level + 1 < 3:
                        level += 1
                    mc.set_level_max(level, level_max, cur, cnx, name_user)
                    mc.continuer()
                else:
                    solde += mise / 2
                    mc.update_solde(cur, cnx, solde, name_user)
                    print("\t- Vous avez gagne la moitie de votre mise !")
                    if level + 1 < 3:
                        level += 1
                        print("\t- Super ! Vous passez au Level "+str(level)+".")
                    mc.set_level_max(level, level_max, cur, cnx, name_user)
                    mc.continuer()
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
                mc.update_solde(cur, cnx, solde, name_user)
                #stats = mc.get_stats(mise_moy, nb_coup_moy)
                print("")
                if level > 0:
                    level -= 1
                mc.set_level_max(level, level_max, cur, cnx, name_user)
                #coups total
                coup_total += nb_coup+1
                mc.set_coups_parties(cur, cnx, coup_total, partie, name_user)
                # coup moyen par partie
                coup_moyen = coup_total / partie
                print("\t- Coup moyen par partie: "+str(coup_moyen))
                print("\t- Nombre de partie: "+str(partie))
                mc.continuer()
    
cnx = mysql.connector.connect(user="291957", password="eKy@SwM4Fe2ab6Z", host="mysql-casino-jmme.alwaysdata.net", database="casino-jmme_bdd")
cur = cnx.cursor()
main()