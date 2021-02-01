# GestionImmobilière

Dans le cadre d’un projet de création d’une application web de gestion immobilière, on nous demande de créer un ensemble de microservices. Ces microservices doivent permettre à un utilisateur de renseigner un bien immobilier avec les caractéristiques suivantes : nom, description, type de bien, ville, pièces, caractéristiques des pièces, propriétaire) et de consulter les autres biens disponibles sur la plateforme. 

## Pour commencer

L'API REST suivante a été codé en python avec l'environnement de developpement Pycharm de JetBrain. Le Framework est Flask et j'utilise le Command Prompt d'Anaconda. Je n'ai pas utilisé de SGBD comme MongoDB pour faciliter la création de l'app, j'ai donc créé une BDD à la main.

### Pré-requis

Avec de lancer l'application il est necessaire d'installer Flask, de créer un environnement de travail python 3.8.

- Installer Flask : https://flask.palletsprojects.com/en/1.1.x/installation/#installation
- Installer environnement virtuel : https://flask.palletsprojects.com/en/1.1.x/installation/#installation

Si besoin :
- Installer Anaconda : https://www.anaconda.com/

### Installation

Pour installer les packages :

* Avec le Command Prompt à l'emplacement de votre projet :

Executez la commande ``pip install flask-restful``

Executez la commande ``pip install flask-bcrypt``

Executez la commande ``pip instll flask-jwt-extended``

Pour créer la base de donnée :

* Dans le dossier database du projet :

Run le fichier ``build_database.py``

Pour lancer le server en local :

* Avec le Command Prompt à l'emplacement de votre projet :

Executez la commande ``set FLASK_APP=app.py`` sur Windows ou ``export FLASK_APP=app.py`` sur Linux

Executez la commande ``set ENV_FILE_LOCATION=./.env`` sur Windows ou ``export ENV_FILE_LOCATION=./.env`` sur Linux

Executez la commande ``flask run``

## Démarche pour tester le programme sur Postman

Dans le navigateur web ou Postman:

* Création des Users (SignUp):

``POST http://127.0.0.1:5000//api/auth/signup`` avec comme body :
<br/>``{``
<br/>``    "lname": "Parra",``
<br/>``    "fname": "Morgan",``
<br/>``    "birthday": "17/01/1994",``
<br/>``    "email": "morgan.parra@gmail.com",``
<br/>``    "password" : "carnaval72"``
<br/>``}
``
<br/>Puis
<br/>``
{``
<br/>``    "lname": "Rougerie",``
<br/>``    "fname": "Aurelien",``
<br/>``    "birthday": "18/02/1995",``
<br/>``    "email": "aurelien.rougerie@gmail.com",``
<br/>``    "password" : "cocorico12"``
<br/>``}
``
<br/>Puis
<br/>``
{``
<br/>``    "lname": "James",``
<br/>``    "fname": "Brock",``
<br/>``    "birthday": "19/03/1996",``
<br/>``    "email": "brock.james@gmail.com",``
<br/>``    "password" : "balerine42"``
<br/>``}
``
<br/>Puis
<br/>``
{``
<br/>``    "lname": "Lopez",``
<br/>``    "fname": "Camille",``
<br/>``    "birthday": "20/04/1997",``
<br/>``    "email": "camille.lopez@gmail.com",``
<br/>``    "password" : "asm63"``
<br/>``}
``

* Ce qu'il est possible de faire sans être loger :

Possible de regarder la liste des utilisateurs (sans les mot-de-passe):

``GET http://127.0.0.1:5000//api/Users``

Possible de regarder la liste des biens :

``GET http://127.0.0.1:5000//api/Goods``

Possible de rechercher un bien particulier (par id) :

``GET http://127.0.0.1:5000//api/Goods/1``

Possible de rechercher un bien particulier (par id, type, city, rooms, owner) :

``GET http://127.0.0.1:5000//api/Goods?city=Lyon``

Pas possible de creer un bien particulier :

``POST http://127.0.0.1:5000//api/Goods`` avec comme body :
<br/>``{``
<br/>``    "name": "Petite Hute",``
<br/>``    "description": "Une petite hute bien chaleureuse",``
<br/>``    "city": "Monaco",``
<br/>``    "type": "Hute",``
<br/>``    "rooms": 1,``
<br/>``    "feature": "1 piece ronde"``
<br/>``}
``

Pas possible modifier/supprimer un bien, modifier/supprimer un utilisateur :

``PUT http://127.0.0.1:5000//api/Goods/1`` avec comme body :
<br/>``{``
<br/>``    "name": "Petite Hute",``
<br/>``    "description": "Une petite hute bien chaleureuse",``
<br/>``    "city": "Monaco"``
<br/>``}
``

``DELETE http://127.0.0.1:5000//api/Goods/1``

``PUT http://127.0.0.1:5000//api/Users/1`` avec comme body :
<br/>``{``
<br/>``    "lname": "Gabart",``
<br/>``    "fname": "Francois",``
<br/>``    "birthday": "21/05/1998"``
<br/>``}
``

``DELETE http://127.0.0.1:5000//api/Users/1``

* Loger un User (Login avec clé de hashage):

``POST http://127.0.0.1:5000//api/auth/login`` avec comme body :
<br/>``{``
<br/>``    "email": "morgan.parra@gmail.com",``
<br/>``    "password" : "carnaval72"``
<br/>``}
``

A partir de maintenant, pour rester identifié avec Morgan Parra copier le token reçu en réponse. Dans vos prochaines requètes, ajouter dans "Authentification" de Postman le token et selectionner dans TYPE ``bearer token``


* Ce qu'il est possible de faire en étant loger :

Possible de regarder toutes les données de son profil mais pas des autres (Morgan Parra a l'id 1) :

``GET http://127.0.0.1:5000//api/Users/1`` ==> OK

``GET http://127.0.0.1:5000//api/Users/2`` ==> KO

Possible de modifier/supprimer toutes les données de son profil mais pas des autres (Morgan Parra a l'id 1) :

``PUT http://127.0.0.1:5000//api/Users/1`` avec body :
<br/>``{``
<br/>``    "lname": "Gabart",``
<br/>``    "fname": "Francois",``
<br/>``    "birthday": "21/05/1998"``
<br/>``}
``

``PUT http://127.0.0.1:5000//api/Users/2`` avec body :
<br/>``{``
<br/>``    "lname": "Gabart",``
<br/>``    "fname": "Francois",``
<br/>``    "birthday": "21/05/1998"``
<br/>``}
``

Possible de creer un bien :

``PUT http://127.0.0.1:5000//api/Goods/1`` avec body :
<br/>``{``
<br/>``    "name": "Petite Hute",``
<br/>``    "description": "Une petite hute bien chaleureuse",``
<br/>``    "city": "Monaco",``
<br/>``    "type": "Hute",``
<br/>``    "rooms": 1,``
<br/>``    "feature": "1 piece ronde"``
<br/>``}
``

Possible de modifier/supprimer toutes les données de ses bien mais pas des autres (Morgan Parra a le bien 1 et 2) :

``PUT http://127.0.0.1:5000//api/Goods/1`` avec body :
<br/>``{``
<br/>``    "name": "Petite Hute",``
<br/>``    "description": "Une petite hute bien chaleureuse",``
<br/>``    "city": "Monaco"``
<br/>``}
``

``PUT http://127.0.0.1:5000//api/Goods/3`` avec body :
<br/>``{``
<br/>``    "name": "Petite Hute",``
<br/>``    "description": "Une petite hute bien chaleureuse",``
<br/>``    "city": "Monaco"``
<br/>``}
``

## Fabriqué avec

_Choix technologiques :_
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Framework Flask (back-end)
* [Pycharm](https://www.jetbrains.com/fr-fr/pycharm/) - Environnement de développement
* [Anaconda](https://www.anaconda.com/) - Command Prompt


## Versions

Liste des versions : [Cliquer pour afficher](https://github.com/Oiures/GestionImmobiliere/tags)

## Auteurs

* **Augustin Bodet** 




