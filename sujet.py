#    """
#	*  *  *  *  *  *  *  *  *  *  * PROJET : REALISER UN JEU DE CASINO *  *  *  *  *  *  *  *  *\n
#	Le jeu comporte 3 levels avec la possibili� que le joueur choissise son level (si ce n'est pas sa 1� fois dans le Casino).
#	En d'autres termes, tout nouveau joueur doit passer par le 1� level. Suite � la 1� partie, il a le droit de choisir son level en lui rappelant / proposant le dernier niveau atteint\n.
#	Lors de chaque niveau, Python tire un nombre : level 1 (entre 1 et 10),
#	level2 (1 et 20), level3 (1 et 30). C'est � vous de deviner le nombre myst�rieux avec 3 essais (en tout) lors du 1� 
#	level, 5 au 2� level et 7 au 3� level. Chaque essai ne durera pas plus de 10 secondes. Au-del�, 
#	vous perdez votre essai. Att : si vous perdez un level, vous rejouez le level pr�c�dent.
#	Quand vous souhaitez quitter le jeu, un compteur de 10 secondes est mis en place. 
#	En absence de validation de la d�cision, le jeu est termin�.
#	Python fournit enfin les statistiques du jeu (voir ci-dessous).
  
#\n\n
#	Les messages � imprimer (� respecter) : \n
#	* Vous pouvez les personnaliser en soulignant les mots-d'int�r�t et en adaptant un jeu de couleur suivant le type de message (perte / gain)
#	* Proposer au joueur si il veut bien afficher les r�gles du jeu ?\n      
#	\t- Je suis Python. Quel est votre pseudo ? \n     
#	\t- Hello Ren�, vous avez 10 �, Tr�s bien ! Installez vous SVP � la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n
#	\t- Je viens de penser � un nombre entre 1 et 10. Devinez lequel ?\n
#	\t- Att : vous avez le droit � trois essais !\n
#	\t- Si vous devinez mon nombre d�s le premier coup, vous gagnez le double de votre mise !\n
#	\t- Si vous le devinez au 2� coup, vous gagnez exactement votre mise !\n
#	\t- Si vous le devinez au 3� coup, vous gagnez la moiti� votre mise !\n    
#	\t- Si vous ne le devinez pas au 3� coup, vous perdez votre mise et
#	\tvous avez le droit : 
#	\t\t- de retenter votre chance avec l'argent qu'il vous reste pour reconqu�rir le level perdu.
#	\t\t- de quitter le jeu.\n
#	\t- D�s que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level sup�rieur.\n     
#	\t- Le jeu commence, entrez votre mise : ?\n
#	\t- Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 � :  ?\n    
#	\t- Alors mon nombre est : ?\n
#	\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :  ?\n
#	\t- Vous avez d�pass� le d�lai de 10 secondes" ! Vous perdez l'essai courant\n\t\t\t et il vous reste "E" essai(s) !\n
#	\t- Votre nbre est trop grand !\n
#	\t- Votre nbre est trop petit !\n
#	\t- Il vous reste une chance !\n      
#	\t- Bingo Ren�, vous avez gagn� en "N" coup(s) et vous avez emport� "E" � !\n
#	\t- Vous avez perdu ! Mon nombre est "nb_python" !\n
#	\t- Souhaitez-vous continuer la partie (O/N) ?\n
#	\t- Je ne comprends pas votre r�ponse. Souhaitez-vous continuer la partie (O/N) ?\n
#	\t- Au revoir ! Vous finissez la partie avec "M" �.\n    
#	\t- Super ! Vous passez au Level 2.\n
#	\t- Les statistiques du level 1 sont les suivantes : ...
#	\t- Rappelez vous, le principe est le m�me sauf que mon nombre est maintenant entre 1 et 20 et\n\t\t vous avez le droit � 5 essais !\n
#	\t- Entrez votre mise : ?\n
#	\t- Erreur, votre mise est plus elev� que votre solde.\n
#	\t- Entrer une mise inf�rieure ou �gale � "S" � : ?\n
#	\t ... \n  
#	\t- Super ! Vous passez au Level 3 !\n
#	\t- Les statistiques du level 2 sont les suivantes : ...    
#	\t- Rappelez vous, le principe est le m�me sauf que mon nombre est entre 1 et 30 et\n\t\t vous avez le droit � 7 essais !\n 
#	\t ... \n
#	\t Bravo, vous avez gagn� ! Les statistiques de la partie sont les suivantes : ... \n    
#	\t- Rebonjour Ren�, Content de vous revoir au Casino, pr�t pour un nouveau challenge !\n.
#	\t- Voici statistiques, depuis la 1� fois jj/mm/aaaa hh:mm :\n
#	\t\t- Vos meilleures statistiques : 
#	\t\t\t- Level le plus �lev� atteint est "level",\n
#	\t\t\t- Vous avez r�ussi � trouver le bon nombre d�s le 1� coup "f" fois.\n
#	\t\t\t- Le gain le plus elev� est
#	\t\t\t- La mise la plus elev� est 
#	\t\t\t- ...
  
#	\t\t- Vos pires statistiques : 
#	\t\t\t- ...
  
#	\tVos moyennes : 
#	\t\t\t- La mise moyenne est de "mise_moy"    
#	\t\t\t - Le nombre moyen de tentatives pour trouver le bon nombre est : 
#	\t\t\t(on ne comptabilisera le nombre de coups qu'en cas de r�ussite)\n 
#\t\t\t-...     
  
#	\t- Pouvez-vous faire mieux ? :\n
  
#le pourcentage de r�ussite

#\n\n\n
#	Les noms des vars � respecter (liste non exhaustive) :\n
#	\t- name_user = le nom de l'utilisateur\n
#	\t- nb_python = le nombre choisi par l'ordi al�atoirement !\n
#	\t- nb_user = le nombre choisi par le user !\n
#	\t- nb_coup = le nombre de coup restant pour le user !\n 
#	\t- level = niveau de jeu : 1, 2, 3 !\n     
#	\t- mise = le montant de la mise du joueur !\n
#	\t- dotation = la dotation initiale du joueur !\n
#	\t- gain = le montant de la mise du joueur !\n
#	\t- solde = le montant de la mise du joueur !\n  
#	\t- mise moyenne est de "mise_moy"\n
#	\t- ...
#	"""



