import numpy as np
import datetime

def rules(name_user, DIFFICULTY, level):
    print("\t- Hello " + name_user + ", vous avez 10e, Tres bien ! Installez vous SVP a la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n")
    print("\t- Je viens de penser a un nombre entre 1 et "+str(DIFFICULTY[level][1])+". Devinez lequel ?\n")
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
            if(nb_user >= 1 and nb_user <= max):
                break
            else:
                raise ValueError
        
        except ValueError:
            nb_user = input("\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et "+str(max)+" : ")

    return nb_user
    
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

    solde = solde - mise

    return mise, solde

#def get_stats(mise_moy, nb_coup_moy):
#    mise_moy = mise_totale / nb_mise
#    nb_coup_moy = nb_coup_total / nb_parties
#    return np.mean(mise_moy), np.mean(nb_coup_moy)

def affiche_stats(stats):
    print("\t- La mise moyenne est de : ", str(stats[0]), "euros.")
    print("\t- Le nombre de coup moyen est de : ", str(stats[1]), "coups.")
    print("\t- Mise la plus elevee: "+str(stats[2]))
    print("\t- Mise la plus faible: "+str(stats[3]))

def create_user(cur, cnx, name_user, solde):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql_add_user = """INSERT INTO user 
    (name, solde, timestamp, nb_mise, mise_total, level_max, level_actual, nb_win_first_try, nb_win, nb_lose, gain_max, mise_max, mise_min, coup_total, nb_parties) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    value = (name_user, solde, date, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'NULL', 0, 0)
    cur.execute(sql_add_user, value)
    cnx.commit()

def update_date(cur, cnx, name_user):
    sql_modify_date ="""UPDATE `user` SET `timestamp`= %s WHERE name = %s"""
    value = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), name_user)
    cur.execute(sql_modify_date, value)
    cnx.commit()

def update_mise_max(cur, cnx, mise_max, name_user):
    sql_modify_mise_max ="""UPDATE `user` SET `mise_max`= %s WHERE name = %s"""
    value = (mise_max, name_user)
    cur.execute(sql_modify_mise_max, value)
    cnx.commit()

def update_mise_min(cur, cnx, mise_min, name_user):
    sql_modify_mise_min ="""UPDATE `user` SET `mise_min`= %s WHERE name = %s"""
    value = (mise_min, name_user)
    cur.execute(sql_modify_mise_min, value)
    cnx.commit()
    
def update_nb_win_first_try(cur, cnx, nb_win_first_try, name_user):
    sql_modify_nb_win_first_try ="""UPDATE `user` SET `nb_win_first_try`= %s WHERE name = %s"""
    value = (nb_win_first_try, name_user)
    cur.execute(sql_modify_nb_win_first_try, value)
    cnx.commit()

def update_solde(cur, cnx, solde, name_user):
    sql_modify_solde ="""UPDATE `user` SET `solde`= %s WHERE name = %s"""
    value = (solde, name_user)
    cur.execute(sql_modify_solde, value)
    cnx.commit()

def set_level_max(level, level_max, cur, cnx, name_user):
    sql_modify_level_actual ="""UPDATE `user` SET `level_actual`= %s WHERE name = %s"""
    value = (level, name_user)
    cur.execute(sql_modify_level_actual, value)
    cnx.commit() 
    if level > level_max:
        print(level)
        level_max = level
        sql_modify_level_max ="""UPDATE `user` SET `level_max`= %s WHERE name = %s"""
        value = (level_max, name_user)
        cur.execute(sql_modify_level_max, value)
        cnx.commit()

def set_coups_parties(cur, cnx, coup_total, nb_parties, name_user):
    sql_modify_coup_total ="""UPDATE `user` SET `coup_total`= %s, `nb_parties` = %s WHERE name = %s"""
    value = (coup_total, nb_parties, name_user)
    cur.execute(sql_modify_coup_total, value)
    cnx.commit()

