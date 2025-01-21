Documentation : Code de Base Django - Intégration avec l'API Riot Games

Ce projet est un code de base développé avec Django qui intègre l’API de Riot Games pour fournir des fonctionnalités interactives liées aux données des joueurs de League of Legends.

⚠️ Important : Le token API fourni par Riot Games n’est valide que pendant 24 heures. Pensez à le régénérer régulièrement pour garantir le bon fonctionnement des requêtes.
Fonctionnalités principales :
1. Récupération des maîtrises de champions

    Objectif : Afficher les maîtrises des différents champions d’un joueur.
    Entrées requises :
        Nom d’utilisateur (summoner name).
        Tag utilisateur (region tag, ex : EUW, NA, etc.).
    Détails :
        Le système interroge l’API de Riot Games pour récupérer les données de maîtrises associées à un joueur, y compris les champions les plus joués et leurs scores.

2. Informations sur les 10 dernières parties

    Objectif : Fournir des statistiques détaillées sur les 10 dernières parties jouées par un utilisateur.
    Entrées requises :
        Nom d’utilisateur (summoner name).
        Tag utilisateur (region tag).
    Détails :
        Les informations incluent : résultats des matchs, performances (kills, deaths, assists), et rôles joués.
        Permet une analyse rapide des tendances et performances récentes du joueur.

Objectifs du projet :

    Offrir une interface simple et efficace pour interagir avec l’API de Riot Games.
    Faciliter l’analyse des performances d’un joueur à partir des données publiques disponibles via l’API.
    Fournir un point de départ extensible pour développer des fonctionnalités supplémentaires liées à League of Legends.

Prérequis et configuration :

    Clé API Riot Games :
        Obtenez une clé sur le portail des développeurs Riot Games.
        Remplacez l’ancienne clé dans le fichier de configuration dès que celle-ci expire (validité : 24 heures).

    Environnement Django :
        Installez les dépendances nécessaires :

        pip install django requests

    Fichier de configuration :
        Mettez à jour les paramètres suivants dans le fichier de configuration du projet :
            Clé API.
            Paramètres régionaux (si applicable).

Meilleures pratiques :

    Régénérer le token API toutes les 24 heures pour éviter les erreurs d’authentification.
    Gérer les erreurs d’API comme les requêtes dépassant les limites de taux (rate limiting) ou les entrées utilisateur invalides.
    Sécuriser la clé API en utilisant des variables d’environnement ou des fichiers protégés.

Conclusion :

Ce projet Django constitue une base solide pour explorer et utiliser les données de l’API Riot Games. Les fonctionnalités incluses permettent de visualiser les performances des joueurs et d’étudier leurs maîtrises de champions, tout en étant facilement extensible pour ajouter de nouvelles capacités.


Pour la partie Github:

La branche main est protégée pour garantir la stabilité, la sécurité et la qualité du code. Ces protections assurent que seules des modifications validées et sécurisées peuvent y être intégrées, tout en évitant les erreurs accidentelles ou les actions non autorisées.
Règles principales :

    Suppression de la branche interdite
        Objectif : Empêcher toute suppression accidentelle.
        Détail : Seuls les utilisateurs disposant de permissions spéciales peuvent supprimer cette branche.

    Exigence de Pull Requests
        Objectif : Vérifier les modifications avant de les fusionner.
        Détail : Toutes les modifications doivent passer par une pull request, être révisées et validées avant leur intégration dans main.

    Pushs forcés interdits
        Objectif : Préserver l'historique des commits et éviter les modifications non intentionnelles.
        Détail : Les pushs forcés sont bloqués pour garantir l'intégrité du code.

Objectifs de ces protections :

    Maintenir la qualité du code : En vérifiant chaque contribution via des pull requests.
    Préserver l'intégrité du dépôt : En bloquant les suppressions et les pushs forcés.
    Encourager la collaboration : En instaurant un processus de révision systématique pour chaque changement.

Ces règles assurent que la branche main, cœur du projet, reste stable, fonctionnelle, et protégée contre les erreurs humaines ou malveillantes, tout en favorisant un travail d'équipe structuré et efficace.