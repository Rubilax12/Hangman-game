#Ce jeu est un pendu avec 6 vies, le principe est simple: trouver le mot avant de mourir. Bonne chance.

#Importation des librairies
import random #Aléatoire (pour le choix du mot)
import os #'Système' pour savoir si un chemin de fichier est correct

#Fonction d'affichage de l'avancement du pendu
def afficher_pendu(vies):
    # Déterminer le chemin du fichier texte en fonction du nombre de vies restantes
    chemin_fichier = f"pendu_{vies}.txt"
    
    # Charger et afficher le contenu du fichier
    try:
        with open(chemin_fichier, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Fichier non trouvé.")

# Charger la liste de mots à partir d'un fichier texte
def load_list(filename):
    #Ouverture du fichier + utilisation de l'encodage utf-8 (encodage moderne/classique)
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        #Renvoie le résultat sans espace ni retour chariot (à adapter selon votre fichier liste de mots) 
        return [line.strip() for line in f]

# Choisir un mot aléatoire dans la liste
def choisir_mot(liste_mots):
    return random.choice(liste_mots)

# Fonction pour afficher le mot partiellement deviné
def affichage_mot(mot, lettres_devinees):
    mot_partiel = ""
    #Recherche lettre par lettre dans le mot que l'ordinateur a selectionné plus haut
    for lettre in mot:
        #Si le joueur a trouvé une lettre alors on l'affiche
        if lettre.lower() in lettres_devinees:
            mot_partiel += lettre + " "
            #Sinon la lettre devient un '_'
        else:
            mot_partiel += "_ "
    return mot_partiel

#Fonction principale du jeu
def pendu():
    #Remplacer par le nom de votre fichier texte
    filename = "ListeMots.txt"
    #Gestion d'erreur si le fichier n'est pas trouvé
    if not os.path.exists(filename):
        print("Le fichier liste est introuvable.")
        return
    
    liste_mots = load_list(filename)
    #Choisir un mot aléatoire
    mot_choisi = choisir_mot(liste_mots)
    #Liste pour stocker les lettres devinées
    lettres_devinees = []
    #Nombre de vies prédéfinies
    vie = 6

    os.system('cls')
    print("Bienvenue au jeu du Pendu !")
    print("Le mot à deviner contient", len(mot_choisi), "lettres.")
    
    #Boucle principale du jeu
    while True:
        #Afficher le mot partiellement deviné
        print("Mot actuel :", affichage_mot(mot_choisi, lettres_devinees))
        
        #Vérifier si toutes les lettres ont été devinées
        if set(mot_choisi.lower()) == set(lettres_devinees):
            return("Félicitations ! Vous avez deviné le mot :", mot_choisi)
        
        #Demander à l'utilisateur de deviner une lettre
        lettre_utilisateur = input("Devinez une lettre : ").lower()
        
        #Vérifier si la lettre a déjà été devinée
        if lettre_utilisateur in lettres_devinees:
            print("Vous avez déjà deviné cette lettre. Veuillez en deviner une autre.")
            continue
        
        #Vérifier si la lettre est dans le mot
        if lettre_utilisateur in mot_choisi.lower():
            print("Bonne devinette ! La lettre", lettre_utilisateur, "est dans le mot.")
            lettres_devinees.append(lettre_utilisateur)
        else:
            vie -= 1
            print("Dommage ! La lettre", lettre_utilisateur, "n'est pas dans le mot." "\n Il vous reste : ", vie, "vie(s).")
            #Affiche un ascii art du pendu en fonction du nombre de vie restant
            afficher_pendu(f"{vie}")
            print("\n")

        if vie == 0:
            print("\n")
            afficher_pendu(0)
            print( "Vous avez perdu.\n\nLe mot était: ",mot_choisi  )
            break    

#Appeler la fonction principale du jeu
pendu()

#Merci d'avoir joué. 
#Améliorations possibles: améliorer les dessins et l'affichage + ralonger la liste de mots + changer la couleur du texte sur victoire
#Have a great day !