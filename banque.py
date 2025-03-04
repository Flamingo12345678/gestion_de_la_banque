import random
import time
from datetime import datetime
import os
import hashlib
import uuid
import getpass
transactions = []

print("🏦 Bienvenue à la Banque Python !")

# Fonction pour hacher un mot de passe avec un sel (salt)
def hacher_mot_de_passe(mot_de_passe, salt=None):
    if salt is None:
        salt = uuid.uuid4().hex
    hash_obj = hashlib.sha256(salt.encode() + mot_de_passe.encode())
    mot_de_passe_hache = hash_obj.hexdigest()
    return salt + ":" + mot_de_passe_hache

# Fonction pour vérifier un mot de passe avec son hash
def verifier_mot_de_passe(mot_de_passe, hash_stocke):
    salt, hash_original = hash_stocke.split(':')
    hash_verifie = hashlib.sha256(salt.encode() + mot_de_passe.encode()).hexdigest()
    return hash_verifie == hash_original

# Fonction pour générer un numéro de compte unique
def generer_numero_compte():
    return ''.join(random.choice('0123456789') for _ in range(10))

# Fonction pour charger les comptes utilisateurs.
# Le fichier "comptes.txt" utilise désormais le format suivant :
# nom:prenom:date_naissance:telephone:adresse:numero_compte:solde
def charger_comptes():
    comptes = {}
    try:
        with open("comptes.txt", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                parts = ligne.strip().split(":")
                if len(parts) == 7:
                    nom, prenom, date_naissance, telephone, adresse, numero_compte, solde = parts
                    comptes[numero_compte] = {
                        "nom": nom,
                        "prenom": prenom,
                        "date_naissance": date_naissance,
                        "telephone": telephone,
                        "adresse": adresse,
                        "solde": float(solde)
                    }
    except FileNotFoundError:
        pass
    except ValueError:
        print("❌ Erreur de lecture des comptes.")
    return comptes

# Fonction pour sauvegarder les comptes utilisateurs
def sauvegarder_comptes(comptes):
    with open("comptes.txt", "w", encoding="utf-8") as fichier:
        for numero_compte, details in comptes.items():
            fichier.write(f"{details['nom']}:{details['prenom']}:{details['date_naissance']}:{details['telephone']}:{details['adresse']}:{numero_compte}:{details['solde']}\n")

# Fonction pour créer un compte utilisateur  
def creer_compte():
    nom = input("👤 Entrez votre nom : ").strip().upper()
    prenom = input("👤 Entrez votre prénom : ").strip().capitalize()
    date_naissance = input("📅 Entrez votre date de naissance (JJ/MM/AAAA) : ").strip()
    telephone = input("📞 Entrez votre numéro de téléphone : ").strip()
    adresse = input("🏠 Entrez votre adresse : ").strip()
    if not (nom and prenom and date_naissance and telephone and adresse):
        print("❌ Veuillez remplir tous les champs.")
        return None, None
    
    comptes = charger_comptes()
    # Vérifier si un compte avec ce numéro de téléphone existe déjà
    for compte in comptes.values():
        if compte["telephone"] == telephone:
            print("❌ Un compte avec ce numéro de téléphone existe déjà.")
            return None, None
    
    # Création du mot de passe
    while True:
        mot_de_passe = getpass.getpass("🔑 Créez un mot de passe (au moins 8 caractères et un chiffre) : ").strip()
        if len(mot_de_passe) < 8 or not any(char.isdigit() for char in mot_de_passe):
            print("❌ Mot de passe trop faible. Il doit contenir au moins 8 caractères et un chiffre.")
        else:
            print("✅ Mot de passe enregistré avec succès !")
            break

    # Génération d'un numéro de compte unique
    numero_compte = generer_numero_compte()
    while numero_compte in comptes:
        numero_compte = generer_numero_compte()
    
    # Enregistrement du compte dans le dictionnaire comptes
    comptes[numero_compte] = {
        "nom": nom,
        "prenom": prenom,
        "date_naissance": date_naissance,
        "telephone": telephone,
        "adresse": adresse,
        "solde": 0
    }
    
    # Hacher le mot de passe et sauvegarder dans passwords_secure.txt
    mot_de_passe_hache = hacher_mot_de_passe(mot_de_passe)
    try:
        with open("passwords_secure.txt", "a", encoding="utf-8") as fichier:
            fichier.write(f"{numero_compte}:{mot_de_passe_hache}\n")
    except FileNotFoundError:
        with open("passwords_secure.txt", "w", encoding="utf-8") as fichier:
            fichier.write(f"{numero_compte}:{mot_de_passe_hache}\n")
    
    sauvegarder_comptes(comptes)
    
    print(f"✅ Compte créé avec succès ! Votre numéro de compte est : {numero_compte}")
    print("⚠️ IMPORTANT: Notez bien votre numéro de compte, vous en aurez besoin pour vous connecter.")
    
    return numero_compte, mot_de_passe

# Fonction pour vérifier le mot de passe d'un numéro de compte
def verifier_credentials(numero_compte, mot_de_passe):
    try:
        with open("passwords_secure.txt", "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                parts = ligne.strip().split(":", 1)
                if len(parts) == 2:
                    nc, mdp_hache = parts
                    if nc == numero_compte and verifier_mot_de_passe(mot_de_passe, mdp_hache):
                        return True
        return False
    except FileNotFoundError:
        return False
    except ValueError:
        print("❌ Erreur de lecture des mots de passe.")
        return False

# Fonction pour changer le mot de passe
def changer_mot_de_passe(numero_compte):
    try:
        # Charger tous les mots de passe
        mots_de_passe = {}
        with open("passwords_secure.txt", "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                parts = ligne.strip().split(":", 1)
                if len(parts) == 2:
                    nc, mdp_hache = parts
                    mots_de_passe[nc] = mdp_hache
        
        # Demander l'ancien mot de passe
        ancien_mdp = getpass.getpass("🔑 Entrez votre mot de passe actuel : ").strip()
        if not verifier_credentials(numero_compte, ancien_mdp):
            print("❌ Mot de passe incorrect.")
            return False
        
        # Demander et vérifier le nouveau mot de passe
        while True:
            nouveau_mdp = input("🔑 Entrez votre nouveau mot de passe (au moins 8 caractères et un chiffre) : ").strip()
            if len(nouveau_mdp) < 8 or not any(char.isdigit() for char in nouveau_mdp):
                print("❌ Mot de passe trop faible. Il doit contenir au moins 8 caractères et un chiffre.")
            else:
                break
        
        # Hacher le nouveau mot de passe
        nouveau_mdp_hache = hacher_mot_de_passe(nouveau_mdp)
        mots_de_passe[numero_compte] = nouveau_mdp_hache
        
        # Mettre à jour le fichier des mots de passe
        with open("passwords_secure.txt", "w", encoding="utf-8") as fichier:
            for nc, mdp_hache in mots_de_passe.items():
                fichier.write(f"{nc}:{mdp_hache}\n")
        
        print("✅ Mot de passe modifié avec succès !")
        return True
    
    except FileNotFoundError:
        print("❌ Fichier de mots de passe non trouvé.")
        return False
    except ValueError:
        print("❌ Erreur lors de la modification du mot de passe.")
        return False

# Fonction d'accès avec numéro de compte et mot de passe
def acces():
    essais = 3
    while essais > 0:
        numero_compte = input("🔢 Entrez votre numéro de compte : ").strip()
        mot_de_passe = input("🔑 Entrez votre mot de passe : ").strip()
        
        if verifier_credentials(numero_compte, mot_de_passe):
            print("✅ Accès autorisé !")
            return numero_compte
        else:
            essais -= 1
            print(f"❌ Numéro de compte ou mot de passe incorrect. Essais restants : {essais}")
            if essais == 0:
                print("🚫 Accès refusé. Veuillez patienter 10 secondes avant de réessayer.")
                time.sleep(10)
                essais = 3  # Réinitialisation des essais
    
    return None

# Fonction pour enregistrer les transactions dans un fichier texte
def enregistrer_transactions():
    with open("transactions.txt", "a", encoding="utf-8") as fichier:
        for transaction in transactions:
            fichier.write(transaction + "\n")
    transactions.clear()

# Fonction pour ajouter une transaction avec la date et l'heure
def ajouter_transaction(numero_compte, description):
    maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = f"{maintenant} - Compte {numero_compte} - {description}"
    transactions.append(transaction)
    enregistrer_transactions()
    print(f"✅ {transaction}")

# Fonction pour faire un premier dépôt
def premier_depot(numero_compte):
    while True:
        montant = input("💰 Faites un premier dépôt : ").strip()
        try:
            montant = float(montant)
        except ValueError:
            print("❌ Veuillez entrer un montant valide.")
            continue

        if montant <= 0:
            print("❌ Le montant saisi doit être supérieur à 0")
        else:
            ajouter_transaction(numero_compte, f"Premier dépôt : +{montant} € | Solde restant : {montant} €")
            return montant

# Fonction pour gérer les transactions (retrait, dépôt)
def effectuer_transaction(numero_compte, solde, type_operation):
    montant = input(f"💸 Combien voulez-vous {type_operation} ? ").strip()
    try:
        montant = float(montant)
    except ValueError:
        print("❌ Veuillez entrer un montant valide.")
        return solde

    if montant <= 0:
        print("❌ Le montant doit être supérieur à zéro.")
    elif type_operation == "retirer" and montant > solde:
        print("❌ Vous n'avez pas assez d'argent sur votre compte.")
    elif type_operation == "retirer" and montant > 2000:
        print("❌ Retrait limité à 2000 € par transaction.")
    else:
        solde = solde - montant if type_operation == "retirer" else solde + montant
        signe = "-" if type_operation == "retirer" else "+"
        ajouter_transaction(numero_compte, f"{type_operation.capitalize()} : {signe}{montant} € | Solde restant : {solde} €")

    return solde

# Fonction pour vérifier le solde
def verifier_solde(solde):
    print(f"💰 Votre solde actuel est de : {solde} €")

# Fonction pour afficher l'historique des transactions d'un compte spécifique
def historique_transactions(numero_compte):
    print(f"\n📜 Historique des transactions pour le compte {numero_compte} :")
    try:
        with open("transactions.txt", "r", encoding="utf-8") as fichier:
            transactions_list = fichier.readlines()
            compte_transactions = [t for t in transactions_list if f"Compte {numero_compte}" in t]
            if not compte_transactions:
                print("Aucune transaction enregistrée pour ce compte.")
            else:
                for transaction in compte_transactions:
                    print(transaction.strip())
    except FileNotFoundError:
        print("❌ Aucun historique trouvé.")

# Fonction pour récupérer un mot de passe oublié
def recuperer_mot_de_passe():
    numero_compte = input("🔢 Entrez votre numéro de compte : ").strip()
    comptes = charger_comptes()
    
    if numero_compte not in comptes:
        print("❌ Ce numéro de compte n'existe pas.")
        return
    
    nom = comptes[numero_compte]["nom"]
    prenom = comptes[numero_compte]["prenom"]
    print(f"👤 Le compte appartient à : {nom} {prenom}")
    print("🔐 Création d'un nouveau mot de passe requis.")
    
    while True:
        nouveau_mdp = input("🔑 Créez un nouveau mot de passe (au moins 8 caractères et un chiffre) : ").strip()
        if len(nouveau_mdp) < 8 or not any(char.isdigit() for char in nouveau_mdp):
            print("❌ Mot de passe trop faible. Il doit contenir au moins 8 caractères et un chiffre.")
        else:
            break
    
    # Charger les mots de passe existants
    mots_de_passe = {}
    try:
        with open("passwords_secure.txt", "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                parts = ligne.strip().split(":", 1)
                if len(parts) == 2:
                    nc, mdp_hache = parts
                    mots_de_passe[nc] = mdp_hache
    except FileNotFoundError:
        pass
    
    nouveau_mdp_hache = hacher_mot_de_passe(nouveau_mdp)
    mots_de_passe[numero_compte] = nouveau_mdp_hache
    
    with open("passwords_secure.txt", "w", encoding="utf-8") as fichier:
        for nc, mdp_hache in mots_de_passe.items():
            fichier.write(f"{nc}:{mdp_hache}\n")
    
    print("✅ Mot de passe réinitialisé avec succès !")

# Menu principal
def menu_principal():
    print("\n🏦 Bienvenue à la Banque Python !")
    print("1️⃣ Créer un compte")
    print("2️⃣ Accéder à mon compte")
    print("3️⃣ Mot de passe oublié")
    print("4️⃣ Quitter")
    
    while True:
        choix = input("🔢 Que voulez-vous faire ? ").strip()
        if choix in ["1", "2", "3", "4"]:
            return choix
        print("❌ Veuillez entrer un choix valide (1, 2, 3 ou 4).")

# Programme principal
while True:
    choix_principal = menu_principal()
    
    if choix_principal == "1":
        numero_compte, _ = creer_compte()
        if numero_compte:
            input("Appuyez sur Entrée pour continuer...")
    
    elif choix_principal == "2":
        numero_compte = acces()
        if not numero_compte:
            print("❌ Échec de connexion.")
            continue
        
        comptes = charger_comptes()
        if numero_compte not in comptes:
            print("❌ Ce compte n'existe pas ou a été supprimé.")
            continue
        
        user_details = comptes[numero_compte]
        print(f"👤 Bienvenue, {user_details['nom']} {user_details['prenom']} !")
        solde = user_details["solde"]
        
        # Premier dépôt uniquement si le solde est nul
        if solde == 0:
            solde = premier_depot(numero_compte)
            comptes[numero_compte]["solde"] = solde
            sauvegarder_comptes(comptes)
        
        # Menu du compte utilisateur
        while True:
            print("\n📋 Menu du compte")
            print("1️⃣ Retirer de l'argent")
            print("2️⃣ Déposer de l'argent")
            print("3️⃣ Vérifier le solde")
            print("4️⃣ Changer de mot de passe")
            print("5️⃣ Voir l'historique des transactions")
            print("6️⃣ Retour au menu principal")
            
            choix = input("🔢 Que voulez-vous faire ? ").strip()
            
            if choix == "1":
                solde = effectuer_transaction(numero_compte, solde, "retirer")
                comptes[numero_compte]["solde"] = solde
                sauvegarder_comptes(comptes)
            elif choix == "2":
                solde = effectuer_transaction(numero_compte, solde, "déposer")
                comptes[numero_compte]["solde"] = solde
                sauvegarder_comptes(comptes)
            elif choix == "3":
                verifier_solde(solde)
            elif choix == "4":
                changer_mot_de_passe(numero_compte)
            elif choix == "5":
                historique_transactions(numero_compte)
            elif choix == "6":
                print("👋 Retour au menu principal...")
                break
            else:
                print("❌ Veuillez entrer un choix valide.")
    
    elif choix_principal == "3":
        recuperer_mot_de_passe()
    
    elif choix_principal == "4":
        print("👋 Merci d'avoir utilisé notre banque. Au revoir !")
        break
