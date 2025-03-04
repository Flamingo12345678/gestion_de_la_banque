# Banque Python - Application Bancaire en Python

## Description

Cette application en Python simule une banque avec des fonctionnalités essentielles telles que la création de comptes, la gestion des transactions (dépôts et retraits), la vérification du solde, la récupération du mot de passe et l'affichage de l'historique des transactions. Les informations des utilisateurs sont stockées de manière sécurisée, avec des mots de passe hachés.

## Fonctionnalités

- 💼 **Créer un compte utilisateur** avec nom, prénom, date de naissance, téléphone et adresse.
- 🔐 **Authentification sécurisée** avec un mot de passe haché.
- 💎 **Gestion du solde** : retrait et dépôt d'argent.
- 📈 **Historique des transactions** accessible pour chaque utilisateur.
- 🔒 **Changement et récupération de mot de passe**.

## Prérequis

- Python 3.x

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers du projet :
   ```bash
   git clone https://github.com/Flamingo12345678/gestion_de_la_banque
   cd gestion_de_la_banque
   ```
2. Assurez-vous d'avoir Python installé.
3. Exécutez le script principal :
   ```bash
    banque.py
   ```

## Utilisation

### 1. Lancer l'application

Lorsque vous démarrez l'application, vous verrez le menu principal avec les options suivantes :

- **1️⃣ Créer un compte**
- **2️⃣ Accéder à un compte**
- **3️⃣ Mot de passe oublié**
- **4️⃣ Quitter**

### 2. Créer un compte

- Entrez vos informations personnelles.
- Choisissez un mot de passe sécurisé.
- Un numéro de compte unique sera généré.
- Un premier dépôt est requis après la création du compte.

### 3. Se connecter

- Entrez votre numéro de compte et votre mot de passe.
- Accédez aux options de gestion du compte.

### 4. Menu

Après ces étapes ci-dessus, vous verrez un autre menu pour accéder aux autres parties du programme :

- **1️⃣ Retirer de l'argent**
- **2️⃣ Déposer de l'argent**
- **3️⃣ Vérifier le solde**
- **4️⃣ Changer de mot de passe**
- **5️⃣ Voir l'historique des transactions**
- **6️⃣ Retour au menu principal**

### 5. Effectuer des transactions

- Dépôt et retrait avec des limites définies.
- Affichage du solde actuel.
- Historique des transactions consultable.

### 5. Sécurité

- Les mots de passe sont hachés et stockés de manière sécurisée.
- Trois tentatives de connexion sont autorisées avant un délai d'attente de 10 secondes.

## Fichiers Importants

- **banque.py** : Code principal de l'application.
- **comptes.txt** : Stocke les informations des utilisateurs.
- **passwords_secure.txt** : Stocke les mots de passe hachés.
- **transactions.txt** : Contient l'historique des transactions.

## Contributions

Les contributions sont les bienvenues ! Forkez le projet et proposez des améliorations via des Pull Requests.

## Licence

Ce projet est sous licence MIT. Vous pouvez le modifier et le redistribuer librement.

## Auteur

Ernest Evrard YOMBI - Flamingo12345678
