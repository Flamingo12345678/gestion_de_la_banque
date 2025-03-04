# # Exercice 1 : Gestion d'une banque

# transactions = []

# print("🏦 Bienvenue à la Banque Python !")

# # Vérification et création du mot de passe
# while True:
#     mot_de_passe = input("🔑 Créez un mot de passe (au moins 8 caractères et un chiffre) : ").strip()
#     if len(mot_de_passe) < 8 or not any(char.isdigit() for char in mot_de_passe):
#         print("❌ Mot de passe trop faible. Il doit contenir au moins 8 caractères et un chiffre.")
#     else:
#         print("✅ Mot de passe enregistré avec succès !")
#         break

# # Fonction pour changer de mot de passe
# def changer_mot_de_passe():
#     global mot_de_passe
#     while True:
#         mot_de_passe_actuel = input("🔑 Entrez votre mot de passe actuel : ").strip()
#         if mot_de_passe_actuel != mot_de_passe:
#             print("❌ Mot de passe incorrect. Réessayez.")
#         else:
#             nouveau_mot_de_passe = input("🔑 Entrez votre nouveau mot de passe : ").strip()
#             if len(nouveau_mot_de_passe) < 8 or not any(char.isdigit() for char in nouveau_mot_de_passe):
#                 print("❌ Mot de passe trop faible. Il doit contenir au moins 8 caractères et un chiffre.")
#             else:
#                 mot_de_passe = nouveau_mot_de_passe
#                 print("✅ Mot de passe modifié avec succès !")
#                 break

# # Fonction pour demander si l'utilisateur veut continuer
# def continuer():
#     while True:
#         choix = input("🔄 Voulez-vous continuer ? (o/n) : ").strip().lower()
#         if choix in ["o", "n"]:
#             return choix == "o"
#         print("❌ Veuillez entrer 'o' pour oui ou 'n' pour non.")

# # Fonction d'accès avec mot de passe
# def acces():
#     essais = 3  # Nombre d'essais autorisés
#     while essais > 0:
#         mdp = input("🔑 Entrez votre mot de passe : ").strip()
#         if mdp == mot_de_passe:
#             print("✅ Accès autorisé !")
#             return True
#         else:
#             essais -= 1
#             print(f"❌ Mot de passe incorrect. Essais restants : {essais}")
    
#     print("🚫 Accès refusé. Trop d'essais échoués.")
#     return False

# # Fonction pour enregistrer les transactions dans un fichier texte
# def enregistrer_transactions():
#     with open("transactions.txt", "a", encoding="utf-8") as fichier:
#         for transaction in transactions:
#             fichier.write(transaction + "\n")
            
# # Fonction pour faire un premier dépôt
# def premier_depot():
#     solde = input("💰 Faites un premier dépôt (minimum 100 €) : ").strip()

#     if not solde.isdigit():
#         print("❌ Veuillez entrer un montant valide.")
#         return 0

#     solde = int(solde)
    
#     if solde < 100:
#         print("❌ Le montant doit être d'au moins 100 €.")
#         return 0
#     else:
#         transaction = f"💰 Premier dépôt : +{solde} € | Solde restant : {solde} €"
#         transactions.append(transaction)
#         enregistrer_transactions()
#         print(f"✅ {transaction}")
#         return solde

# # Fonction pour retirer de l'argent
# def retirer_argent(solde):
#     montant = input("💸 Combien voulez-vous retirer ? ").strip()

#     if not montant.isdigit():
#         print("❌ Veuillez entrer un montant valide.")
#         return solde

#     montant = int(montant)
    
#     if montant <= 0:
#         print("❌ Le montant doit être supérieur à zéro.")
#     elif montant > solde:
#         print("❌ Vous n'avez pas assez d'argent sur votre compte.")
#     elif montant > 2000:
#         print("❌ Retrait limité à 2000 € par transaction.")
#     else:
#         solde -= montant
#         transaction = f"💸 Retrait : -{montant} € | Solde restant : {solde} €"
#         transactions.append(transaction)
#         enregistrer_transactions()
#         print(f"✅ {transaction}")
    
#     return solde

# # Fonction pour déposer de l'argent
# def deposer_argent(solde):
#     montant = input("💸 Combien voulez-vous déposer ? ").strip()

#     if not montant.isdigit():
#         print("❌ Veuillez entrer un montant valide.")
#         return solde

#     montant = int(montant)
    
#     if montant <= 0:
#         print("❌ Le montant doit être supérieur à zéro.")
#     else:
#         solde += montant
#         transaction = f"💰 Dépôt : +{montant} € | Solde restant : {solde} €"
#         transactions.append(transaction)
#         enregistrer_transactions()
#         print(f"✅ {transaction}")
    
#     return solde

# # Fonction pour vérifier le solde
# def verifier_solde(solde):
#     print(f"💰 Votre solde actuel est de : {solde} €")

# # Fonction pour afficher l'historique des transactions
# def historique_transactions():
#     print("\n📜 Historique des transactions :")
#     try:
#         with open("transactions.txt", "r", encoding="utf-8") as fichier:
#             transacs = fichier.readlines()
#             if not transacs:
#                 print("Aucune transaction enregistrée.")
#             else:
#                 for transaction in transacs:
#                     print(transaction.strip())
#     except FileNotFoundError:
#         print("❌ Aucun historique trouvé.")

# # Fonction pour charger le solde en prenant une valeur par défaut en paramètre
# def charger_solde(default_solde):
#     try:
#         with open("solde.txt", "r", encoding="utf-8") as fichier:
#             return int(fichier.read().strip())
#     except FileNotFoundError:
#         return default_solde
#     except ValueError:
#         print("❌ Erreur de lecture du solde. Réinitialisation à la valeur par défaut.")
#         return default_solde

# # Fonction pour sauvegarder le solde dans un fichier texte
# def sauvegarder_solde(solde):
#     with open("solde.txt", "w", encoding="utf-8") as fichier:
#         fichier.write(str(solde))

# # Chargement du solde avec une valeur par défaut de 0
# solde = charger_solde(0)

# # Vérification du mot de passe avant d'accéder au menu
# if not acces():
#     exit()

# # Vérification si l'utilisateur veut continuer
# if not continuer():
#     print("👋 Merci d'avoir utilisé notre banque. Au revoir !")
#     exit()
    
# # Premier dépôt
# solde = premier_depot()
# sauvegarder_solde(solde)

# # Menu principal
# while True:
#     print("\n📋 Menu")
#     print("1️⃣ Retirer de l'argent")
#     print("2️⃣ Déposer de l'argent")
#     print("3️⃣ Vérifier le solde")
#     print("4️⃣ Changer de mot de passe")
#     print("5️⃣ Voir l'historique des transactions")
#     print("6️⃣ Quitter")

#     choix = input("🔢 Que voulez-vous faire ? ").strip()
    
#     if choix == "1":
#         solde = retirer_argent(solde)
#         sauvegarder_solde(solde)
#     elif choix == "2":
#         solde = deposer_argent(solde)
#         sauvegarder_solde(solde)
#     elif choix == "3":
#         verifier_solde(solde)
#     elif choix == "4":
#         changer_mot_de_passe()
#     elif choix == "5":
#         historique_transactions()
#     elif choix == "6":
#         print("👋 Merci d'avoir utilisé notre banque. Au revoir !")
#         break
#     else:
#         print("❌ Veuillez entrer un choix valide.")

import random
import time
from datetime import datetime

transactions = []

print("🏦 Bienvenue à la Banque Python !")

# Vérification et création du mot de passe
while True:
    mot_de_passe = input("🔑 Créez un mot de passe (au moins 8 caractères et un chiffre) : ").strip()
    if len(mot_de_passe) < 8 or not any(char.isdigit() for char in mot_de_passe):
        print("❌ Mot de passe trop faible. Il doit contenir au moins 8 caractères et un chiffre.")
    else:
        print("✅ Mot de passe enregistré avec succès !")
        break

# Fonction pour changer de mot de passe
def changer_mot_de_passe():
    global mot_de_passe
    while True:
        mot_de_passe_actuel = input("🔑 Entrez votre mot de passe actuel : ").strip()
        if mot_de_passe_actuel != mot_de_passe:
            print("❌ Mot de passe incorrect. Réessayez.")
        else:
            nouveau_mot_de_passe = input("🔑 Entrez votre nouveau mot de passe : ").strip()
            if len(nouveau_mot_de_passe) < 8 or not any(char.isdigit() for char in nouveau_mot_de_passe):
                print("❌ Mot de passe trop faible. Il doit contenir au moins 8 caractères et un chiffre.")
            else:
                mot_de_passe = nouveau_mot_de_passe
                print("✅ Mot de passe modifié avec succès !")
                break

# Fonction d'accès avec mot de passe
def acces():
    essais = 3
    while essais > 0:
        mdp = input("🔑 Entrez votre mot de passe : ").strip()
        if mdp == mot_de_passe:
            print("✅ Accès autorisé !")
            return True
        else:
            essais -= 1
            print(f"❌ Mot de passe incorrect. Essais restants : {essais}")
            if essais == 0:
                print("🚫 Accès refusé. Veuillez patienter 10 secondes avant de réessayer.")
                time.sleep(10)
                essais = 3  # Réinitialisation des essais

# Fonction pour enregistrer les transactions dans un fichier texte
def enregistrer_transactions():
    with open("transactions.txt", "a", encoding="utf-8") as fichier:
        for transaction in transactions:
            fichier.write(transaction + "\n")

# Fonction pour ajouter une transaction avec la date et l'heure
def ajouter_transaction(description):
    maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = f"{maintenant} - {description}"
    transactions.append(transaction)
    enregistrer_transactions()
    print(f"✅ {transaction}")

# Fonction pour faire un premier dépôt
def premier_depot():
    while True:
        solde = input("💰 Faites un premier dépôt : ").strip()
        if not solde.isdigit():
            print("❌ Veuillez entrer un montant valide.")
            continue

        solde = int(solde)
        if solde <= 0:
            print("❌ Le montant saisie doit etre superieur a 0")
        else:
            ajouter_transaction(f"Premier dépôt : +{solde} € | Solde restant : {solde} €")
            return solde

# Fonction pour gérer les transactions (retrait, dépôt)
def effectuer_transaction(solde, type_operation):
    montant = input(f"💸 Combien voulez-vous {type_operation} ? ").strip()

    if not montant.isdigit():
        print("❌ Veuillez entrer un montant valide.")
        return solde

    montant = int(montant)

    if montant <= 0:
        print("❌ Le montant doit être supérieur à zéro.")
    elif type_operation == "retirer" and montant > solde:
        print("❌ Vous n'avez pas assez d'argent sur votre compte.")
    elif type_operation == "retirer" and montant > 2000:
        print("❌ Retrait limité à 2000 € par transaction.")
    else:
        solde = solde - montant if type_operation == "retirer" else solde + montant
        signe = "-" if type_operation == "retirer" else "+"
        ajouter_transaction(f"{type_operation.capitalize()} : {signe}{montant} € | Solde restant : {solde} €")

    return solde

# Fonction pour vérifier le solde
def verifier_solde(solde):
    print(f"💰 Votre solde actuel est de : {solde} €")

# Fonction pour afficher l'historique des transactions
def historique_transactions():
    print("\n📜 Historique des transactions :")
    try:
        with open("transactions.txt", "r", encoding="utf-8") as fichier:
            transactions = fichier.readlines()
            if not transactions:
                print("Aucune transaction enregistrée.")
            else:
                for transaction in transactions:
                    print(transaction.strip())
    except FileNotFoundError:
        print("❌ Aucun historique trouvé.")

# Fonction pour charger et sauvegarder le solde
def charger_solde(default_solde):
    try:
        with open("solde.txt", "r", encoding="utf-8") as fichier:
            return int(fichier.read().strip())
    except FileNotFoundError:
        return default_solde
    except ValueError:
        print("❌ Erreur de lecture du solde. Réinitialisation à la valeur par défaut.")
        return default_solde

def sauvegarder_solde(solde):
    with open("solde.txt", "w", encoding="utf-8") as fichier:
        fichier.write(str(solde))

# Chargement du solde
solde = charger_solde(0)

# Vérification du mot de passe
if not acces():
    exit()

# Premier dépôt uniquement si le solde est nul
if solde == 0:
    solde = premier_depot()
    sauvegarder_solde(solde)

# Menu principal
while True:
    print("\n📋 Menu")
    print("1️⃣ Retirer de l'argent")
    print("2️⃣ Déposer de l'argent")
    print("3️⃣ Vérifier le solde")
    print("4️⃣ Changer de mot de passe")
    print("5️⃣ Voir l'historique des transactions")
    print("6️⃣ Quitter")

    choix = input("🔢 Que voulez-vous faire ? ").strip()

    if choix == "1":
        solde = effectuer_transaction(solde, "retirer")
        sauvegarder_solde(solde)
    elif choix == "2":
        solde = effectuer_transaction(solde, "déposer")
        sauvegarder_solde(solde)
    elif choix == "3":
        verifier_solde(solde)
    elif choix == "4":
        changer_mot_de_passe()
    elif choix == "5":
        historique_transactions()
    elif choix == "6":
        print("👋 Merci d'avoir utilisé notre banque. Au revoir !")
        break
    else:
        print("❌ Veuillez entrer un choix valide.")