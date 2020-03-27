# ForumTNAH

Le ForumTNAH est une application web permettant des discussions entre anciens étudiants du master Technologies Numériques Appliquées à l'Histoire de l'Ecole nationale des Chartes, et les étudiants actuels. Ce forum a été crée par Maxime Challon.

## Description des fonctionnalités du ForumTNAH

Plusieurs fonctionnalités sont proposées:
* publication de messages visibles par tous, avec possibilité de commentaires
* indexation des messages et recherche de messages par thème
* création de comptes utilisateurs donnant la possibilité de renseigner ses expériences, ses compétences, ses liens (mail, GitHub, LinkedIn) et des informations sur la scolarité à l'EnC
* possibilité de saisie en MarkDown des messages et des commentaires
* possibilité d'envoyer des messages privés

## Développement de l'application

Ce projet a été réalisé dans le cadre de l'évaluation du cours Python. Il est développé avec le langage Python3 et le framework Flask. Son graphisme est réalisé grâce au framework Bootstrap.

## Lancement du ForumTNAH

* Installer Python3
* Cloner ce dépôt Git: `git clone https://github.com/MaximeChallon/ForumTNAH.git`; rentrer dedans
* Installer, configurer et lancer un environnement virtuel avec Python3: `virtualenv -p python3 env` pour l'installation, `source env/bin/activate` pour le lancement
* Installer les requirements.txt: `pip install -r requirements.txt`
* Lancer l'application avec la commande `python3 run.py`
