# GestionImmobilière

Dans le cadre d’un projet de création d’une application web de gestion immobilière, on nous demande de créer un ensemble de microservices. Ces microservices doivent permettre à un utilisateur de renseigner un bien immobilier avec les caractéristiques suivantes : nom, description, type de bien, ville, pièces, caractéristiques des pièces, propriétaire) et de consulter les autres biens disponibles sur la plateforme. 

## Pour commencer

L'API REST suivante a été codé en python avec l'environnement de developpement Pycharm de JetBrain. Le Framework est Flask et j'utilise le Command Prompt d'Anaconda.

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

Pour lancer le server en local :

* Avec le Command Prompt à l'emplacement de votre projet :

Executez la commande ``set FLASK_APP=app.py`` sur Windows ou ``export FLASK_APP=app.py`` sur Linux

Executez la commande ``set ENV_FILE_LOCATION=./.env`` sur Windows ou ``export ENV_FILE_LOCATION=./.env`` sur Linux

Executez la commande ``flask run``

## Démarche pour tester le programme sur Postman

Dans le navigateur web ou Postman:

* Création des Users (SignUp):

Entrer l'URL ``POST http://127.0.0.1:5000//api/auth/signup`` avec comme body :
``
{
    "lname": "Parra",
    "fname": "Morgan",
    "birthday": "17/01/1994",
    "email": "morgan.parra@gmail.com",
    "password" : "carnaval72"
}
``
Puis
``
{
    "lname": "Rougerie",
    "fname": "Aurelien",
    "birthday": "18/02/1995",
    "email": "aurelien.rougerie@gmail.com",
    "password" : "cocorico12"
}
``
Puis
``
{
    "lname": "James",
    "fname": "Brock",
    "birthday": "19/03/1996",
    "email": "brock.james@gmail.com",
    "password" : "balerine42"
}
``
Puis
``
{
    "lname": "Lopez",
    "fname": "Camille",
    "birthday": "20/04/1997",
    "email": "camille.lopez@gmail.com",
    "password" : "asm63"
}
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




