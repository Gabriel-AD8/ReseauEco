# Ici, nous allons stocker nos projets.
# Pour l'instant, c'est une liste vide. Chaque projet sera un dictionnaire.
projets = []

def afficher_menu():
    """Affiche le menu principal de l'application."""
    print("\n--- Mon Arbre d'Actions Solarpunk ---")
    print("1. Créer un nouveau projet")
    print("2. Ajouter une action à un projet existant")
    print("3. Voir l'état de mes arbres")
    print("4. Quitter l'application")
    print("-------------------------------------")

def creer_nouveau_projet():
    """Demande à l'utilisateur de créer un nouveau projet et l'ajoute à la liste."""
    print("\n--- Création d'un nouveau projet ---")
    nom_projet = input("Entrez le nom du nouveau projet : ")

    # Vérifier si le projet existe déjà (pour éviter les doublons simples)
    for p in projets:
        if p['nom'].lower() == nom_projet.lower(): # Compare en minuscules pour ignorer la casse
            print(f"Erreur : Le projet '{nom_projet}' existe déjà. Veuillez choisir un autre nom.")
            return # Sort de la fonction si le projet existe déjà

    # Créer un dictionnaire pour représenter le nouveau projet
    nouveau_projet = {
        'nom': nom_projet,
        'actions': [],  # Une liste pour stocker les actions de ce projet
        'niveau_arbre': 0 # Un simple compteur pour la croissance de l'arbre
    }
    projets.append(nouveau_projet) # Ajoute le nouveau projet à notre liste globale
    print(f"Projet '{nom_projet}' créé avec succès !")

def gerer_choix_menu():
    """Gère le choix de l'utilisateur dans le menu."""
    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == '1':
            creer_nouveau_projet() # <-- APPEL DE LA NOUVELLE FONCTION ICI
        elif choix == '2':
            print("Fonctionnalité 'Ajouter une action' à implémenter.")
            # Ici, nous appellerons une fonction pour ajouter une action
        elif choix == '3':
            print("Fonctionnalité 'Voir l'état des arbres' à implémenter.")
            # Ici, nous appellerons une fonction pour voir les arbres
        elif choix == '4':
            print("Merci d'avoir utilisé Mon Arbre d'Actions Solarpunk. À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez entrer un chiffre entre 1 et 4.")

# Point d'entrée de l'application
if __name__ == "__main__":
    gerer_choix_menu()