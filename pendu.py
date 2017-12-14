# -*-coding:Latin-1 -*

"""Ce fichier contient le jeu du pendu.

Il s'appuie sur les fichiers :
- donnees.py
- fonctions.py"""

import os

from donnees import *
from fonctions import *

scores = recup_scores()
utilisateur = recup_nom_utilisateur()

if utilisateur not in scores.keys():
	scores[utilisateur] = 0
	
#Variable pour savoir quand arrêter la partie
continuer_partie='o'

while continuer_partie != 'n':
	print("Le joueur {} a {} point(s)".format(utilisateur,scores[utilisateur]))
	mot_a_trouver = choisir_mot()
	lettres_trouvees=[]
	mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
	nb_chances = nb_coups
	
	while mot_a_trouver!=mot_trouve and nb_chances>0:
		print("Voici le mot à trouver: {0} , il vous reste {1} chances".format(mot_trouve, nb_chances))
		lettre = recup_lettre()
		
		if lettre in lettres_trouvees:
			print("Vous avez deja choisi cette lettre")
		elif lettre in mot_a_trouver:
			lettres_trouvees.append(lettre)
			print("Vous avez une lettre du mot")
		else:
			print("Dommage, cette lettre ne fait pas parti du mot")
			nb_chances -= 1
		
		mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees) 
		
	
	if mot_a_trouver==mot_trouve:
		print("BRAVO, vous avez trouvé le mot {0}".format(mot_trouve))
		scores[utilisateur] += nb_chances		
	else:
		print("PENDU!")
		
	continuer_partie=input("Voulez vous continuer (o/n)? : ")
	continuer_partie.lower()

enregistrer_scores(scores)

print("Vous finissez la partie avec {0} points".format(scores[utilisateur]))
	



