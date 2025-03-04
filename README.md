# gestion_de_la_banque

## Système d'authentification utilisateur sécurisé

### Description

Cette fonctionnalité implémente un système de création et d'authentification de comptes utilisateurs offrant les fonctionnalités suivantes :

### Création de comptes

- Génération automatique d'un identifiant unique pour chaque nouvel utilisateur.
- Demande de définition d'un mot de passe sécurisé.
- Hachage du mot de passe pour un stockage sécurisé.

### Authentification

- Connexion via l'identifiant unique et le mot de passe.
- Accès sécurisé après une authentification réussie.

### Fonctionnalités clés

- Génération d'identifiants uniques (avec uuid).
- Hachage de mots de passe (avec hashlib).
- Processus d'authentification sécurisé.
