# -*-coding:Latin-1 -*

import os
import pickle
from random import choice


from donnees import *

#Gestion scores
def recup_scores():

	"""Cette fonction récupère les scores enregistrés si le fichier existe.
    Dans tous les cas, on renvoie un dictionnaire, 
    soit l'objet dépicklé,
    soit un dictionnaire vide.

    On s'appuie sur nom_fichier_scores défini dans donnees.py"""
	
	if os.path.exists(mon_fichier_scores):
		
		fichier_scores = open(mon_fichier_scores, "rb")
		mon_depickler=pickle.unpickler(fichier_scores)
		scores = mon_depickler.load()
		fichier_scores.close()
	
	else: #le fichier n'existe pass
		scores={}
	
	return scores

def enregistrer_scores(scores):

	"""Cette fonction se charge d'enregistrer les scores dans le fichier
    nom_fichier_scores. Elle reçoit en paramètre le dictionnaire des scores
    à enregistrer"""
		
	fichier_scores=open(mon_fichier_scores, "wb")
	mon_pickler=pickle.Pickler(fichier_scores)
	mon_pickler.dump(scores)
	fichier_scores.close()
	
#Gestion saisi utilisateur
	

def recup_nom_utilisateur():
    """Fonction chargée de récupérer le nom de l'utilisateur.
    Le nom de l'utilisateur doit être composé de 4 caractères minimum,
    chiffres et lettres exclusivement.

    Si ce nom n'est pas valide, on appelle récursivement la fonction
    pour en obtenir un nouveau"""

    utilisateur = input("Tapez votre nom: ")
    # On met la première lettre en majuscule et les autres en minuscules
    utilisateur = utilisateur.capitalize()
    if not utilisateur.isalnum() or len(utilisateur)<4:
        print("Ce nom est invalide.")
        # On appelle de nouveau la fonction pour avoir un autre nom
        return recup_nom_utilisateur()
    else:
        return utilisateur

def recup_lettre():
	"""Cette fonction récupère une lettre saisie par
    l'utilisateur. Si la chaîne récupérée n'est pas une lettre,
    on appelle récursivement la fonction jusqu'à obtenir une lettre"""
	
	lettre = input("Tapez une lettre: ")
	lettre =  lettre.lower()
	
	if len(lettre)>1 or not lettre.isalnum():
		print("Lettre invalide!")
		return recup_lettre()
	else:
		return lettre
	
# Fonctions du jeu de pendu

def choisir_mot():
    """Cette fonction renvoie le mot choisi dans la liste des mots
    liste_mots.

    On utilise la fonction choice du module random (voir l'aide)."""
    
    return choice(liste_mots)
	
def recup_mot_masque(mot_complet, lettres_trouvees):
    """Cette fonction renvoie un mot masqué tout ou en partie, en fonction :
    - du mot d'origine (type str)
    - des lettres déjà trouvées (type list)

    On renvoie le mot d'origine avec des * remplaçant les lettres que l'on
    n'a pas encore trouvées."""
    
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque
	
	