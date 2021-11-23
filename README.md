# storefront
on crée un dossier dans notre arboressence et on se place dedans.
on lance la commande :
pip install pipenv : installe les dépendances de notre application dans un environnement virtuel
pour que les dépendances de notre application ne crachent pas avec les dépendances d'autres programmes.

pipenv install django : On va installer django dans notre environnement virtuel. pipenv crée aussi deux
fichiers : Pipfile et Pipfile.lock

lancer la commande code . pour ouvrir vscode depuis le dossier ou on est.

pipenv shell : activate this virtual environement

django-admin est un utilitaire qui vient avec django
on peut lancer django-admin pour voir toutes les commandes qu'on peut utiliser
lancer la commande django-admin startproject nom_projet : django va créer un projet dans un autre
dossier appelé nom_projet qu'on vient de crée, et pour éviter la création de ce dossier encore
on rajoute un point à la fin de la commande. [éviter la redandance] 
django-admin startproject storefront . :

dans l'arboressence crée on trouve asgi.py et wsgi.py : pour le déploiement, we don't care about them right
now.
manage.py : this is a wrapper about django.py instead of django.py we will use manage.py
exemple : run django-admin runserver ==> ne marche pas, django-admin ne connait pas encore la config
de notre projet. 
==> on peut lancer la commande python manage.py runserver ou bien si on lance python manage.py
on voit qu'elle contient tous les commandes comme django-admin
python manage.py runserver [9000] => le port on peut le mettre optionnellement. par défaut 8000


pipenv --venv : retourne le chemin vers le dossier environnement de développement python
le copier coller dans vscode comand+shift+p : interprer path ==>
Ajouter a vscode le chemin vers l'interpreteur virtuel crée 
ouvrir le terminal dans vscode et ce dernier active directement l'environnement de développement.
py manage.py runserver 


py manage.py startapp playground : création d'une nouvelle application nommé playground,
la première application crée est une application d'administration.

tous les app crées ont exactement la même structure.

dans le dossier migrations : on trouve tout le nécessaire pour la génération des bases de données.
module admin : comment l'interface admin va être représenté.
module apps.py : là où on configure le module : le nom ne reflète pas ce que le module fait.
c'est mieux de l'appeler config


!!!! Configure Urls !!!!!!!!!!
dans l'application playground :
on commence par la vue :
from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def say_hello(request):
    # pull data from db
    # Transform
    # Send email
    return response('<p>Hello World</p>')

tres simple
ensuite creer un fichier urls.py
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URLConf
URLPatterns = [
    path('playgroung/hello', views.say_hello)
]

apres aller dans le rojet pricipal : urls.py
suivre les consignes 

django debug toolbar
pip install django-debug-toolbar

add this on INSTALLED APP on settings.py
'debug_toolbar',

add a line in urlpatterns on
path('__debug__/', include(debug_toolbar.urls))

'debug_toolbar.middleware.DebugToolbarMiddleware',

add on middleware'debug_toolbar.middleware.DebugToolbarMiddleware',

add also
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
anywhere

************************************************************************
			   Models == > les modèles
************************************************************************
utlisés pour enregistrer et lire les données.

1- Introduction to data modeling.
2- Building an e-commerce data model.
3- Organizing models in apps.
4- coding model classes.



Création des app:
py manage.py startapp store
py manage.py startapp tags

add those created apps in settings.py INSTALLED_APPS

Setting Up the Database
1- Creating migrations.
2- Running migrations.
3- Reversing migrations.
4- Populating the database.

Supported Database engines

SQlite : low database
PostgreSQL <== |Most Common
MySQL <==      |Most Common
MariaDB
Oracle
MS SQL Server

in the Terminal : py manage.py makemigrations

dans la relation OneToOne, et on the delete
there is -- cascade - null - default et protect


py manage.py migrate

py manage.py sqlmigrate store 0003

how to undo last migration

py manage.py migrate store 0003
et ..
supprimer manuellement le code rajouté et le fichier de migration

ou bien utiliser le git et revenir à la dernière version avant de faire le commit

pour voir les versions : 
git log --oneline

connect djando to mysql
download a package named mysqlclient
--> pipenv install mysqlclient
le probleme ici c'est un probleme de version vu que j'utilisait python 3.10
donc j'ai du désinstaller 3.10 et installer 3.9.9
une petite modification faite sur le pipfile (version)
lancer la commande pipenv et voir ce qu'elle peut faire
pipenv --rm 
pipenv check
pipenv --venv 3.9.9 
et ça marche ==> ensuite pipenv install mysqlclient

oooook
test la connexion :
1 - rajouter le path de mysql dans les variables d'environnement c:\Wamp64 ...
tester --> mysql -u root -p 

generate random dummy values : mockaroo.com


ORM SECTION 51%


import the code given by Mosh Hamedani
modify the DATABASE section in setting.py file
pipenv install to create a virtual environment.
pipenv shell to activate the virtual environment.
python manage.py migrate to create the database.

ALTER DATABASE `storefront` CHARACTER SET utf8;

exemple Product.objects --> retourne un manager object
--> c'est une interface sur la base de données.
--> contient beaucoup de méthodes pour la manipulation de la base de données.
--> méthodes pour ajout - mises à jour - modifications .. de données.
Entity.objects
.all() --> getting all objects.
.get() --> getting a single object.
.filter() --> filtering data

la plupart de ces méthodes retournent un query-set 
Product.objects.all()
nous n'aurons pas un liste de products mais nous aurons un
query_set = Product.objects.all()
pour transformer ce query_set en objet, il y a des méthodes une desquels:
1- 
for product in query_set:
	print(product)

2- autre méthode : conversion en une liste.
list(query_set) ==> ce query_set sera évalué

3- accés direct à un élément :
query_set[0]
ou bien 
query_set[0:5] --> accés aux 5 premiers éléments.

après le query_set sera évalué.

mais pourquoi?
la solution c'est de prévenir le chargement de beaucoup de valeur en mémoire depuis la base de données
et prenons le cas où on a un traitement complexe par exemple:
query_set.filter().filter().order_by()

ça n'empêche qu'il y a des méthodes qui retournent des valeurs uniques tel que Product.objects.count()

queryset = Product.objects.filter(unit_price__range=(20, 30))
--> filtre les données en rangée d'unité de prix entre 20 et 30 
--> la présentation est unit_price (l'attribut) suivi de __ suivi de mot clé.

autre chose :
on peut travailler avec les collections :
queryset = Product.objects.filter(collection__id__range=(1,2,3))

autre exemple : on veut chercher les produits qui contiennet coffee en titre:
queryset = Product.objects.filter(title__contains='coffee')
queryset = Product.objects.filter(title__icontains='coffee') : ignore case.
queryset = Product.objects.filter(title__startswith='coffee')
queryset = Product.objects.filter(title__endswith='coffee')

exemple pour les dates:
queryset = Product.objects.filter(last_update__year=2021)

exemple test null:
queryset = Product.objects.filter(description__isnull=True)

examples of the exercice:
Customers with .com accounts
==> queryset = Customer.objects.filter(email__icontains='.com')

Collections that don’t have a featured product
==> queryset = Collection.objects.filter(featured_product__isnull=True)

Products with low inventory (less than 10)
==> queryset = Product.objects.filter(inventory__lt=10)

Orders placed by customer with id = 1
==> queryset = Order.objects.filter(customer__id=1)

Order items for products in collection 3
==> queryset = OrderItem.objects.filter(product_collection__id=3)


COMPLEX LOOKUPS USING Q OBJECTS
we attempt to search Products : inventory < 10 and price < 20
multiple solutions :
1- queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
2- queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)  ==> and

Comment faire des requetes personnalisés : en utilisant la classe Q de django.db.models
exemple OR au 

queryset = Product.objects.filter(
        Q(inventory__lt=10) | Q(unit_price__lt=20))  ==> OR

on peut fair & aussi
queryset = Product.objects.filter(
        Q(inventory__lt=10) & Q(unit_price__lt=20))  ==> AND
mais on retourne au même résultat, il est préférable de faire comme l'exemple précédent
(ajouter plusieurs filtres)

autre exemple:
queryset = Product.objects.filter(
        Q(inventory__lt=10) & ~Q(unit_price__lt=20))  ==> AND NOT

==============================================================================================

Si maintenant on est dans le cas ou on veut comparer deux champs, attribut dans la même requête.
on utilise la classe F de django.db.models
queryset = Product.objects.filter(inventory=F('unit_price'))
autre exemple
queryset = Product.objects.filter(inventory=F('collection__id'))


==============================================================================================
					SORTING DATA
==============================================================================================

queryset = Product.objects.order_by('title')

inverser l'ordre
queryset = Product.objects.order_by('-title')

ajouter d'autres critères de sort
queryset = Product.objects.order_by('unit_price','-title')
==> ordonner par prix croissant et titre décroissant

queryset = Product.objects.order_by('unit_price','-title').reverse()
==> inverser la direction du sort
==> .reverse() faire le sort selon le unit_price en ordre décroissant
    et le -tilte en ordre croissant.

un autre exemple:
queryset = Product.objects.filter(collection__id=1).order_by('unit_price')

si on veut sort du résultat et uniquement avoir le premoer résultat.
==> queryset = Product.objects.order_by('unit_price')[0]
--> dans cette implémentation nous n'allons pas avoir un queryset
parcequ'on a accés à un élément individuel.
queryset = Product.objects.order_by('unit_price'): juste là, on a un queryset
mais si on rajoute[0] on aura un objet.donc ==> nous devons renommer 
le queryset à product.
et encore nous devons changer la ligne suivante en :
return render(request, 'hello.html', {'name': 'Amine', 
	'product': product})

changer de ce fait le template en hello.html
==> pour s'en passer de tout ça, on utilisera une autre méthode de objects.
product = Product.objects.earliest('unit_price')
tenir en compte que la méthode sort_by retourne un queryset
la méthode earliest() et latest() retournent des objets.

==============================================================================================
			LIMITING RESULTS
==============================================================================================
l'objectif ici est d'éviter l'affichage de plusieurs résultat dans la même 
page, on va réduire le nombre de résultats.

queryset = Product.objects.all()[:5] ==> limiter le résultat en 5. 0, 1, 2, 3, 4
queryset = Product.objects.all()[5:10] ==> commencer de 5 à 9

==============================================================================================
			Selecting Fields to Query
=============================================================================
queryset = Product.objects.values('id','title') ==> les autres fields comme
description ou autre n'ont pas d'importance, on veut selement afficher par
exemple les deux attributs id et titre.

autre exemple :
queryset = Product.objects.values('id','title','collection__title')==>
en utilisant les __ on peut accéder les attributs en relation avec la 
collection .
==> cet exemple est traduit par un inner join
!! dans cette méthode, au lieu d'avoir des instances d'objets on va avoir 
des dictionnaires.
dans le template hello.html, au lieu d'afficher product.tilte
--> afficher product
une autre méthode 
queryset = Product.objects.values_list('id','title','collection__title')
==> le résultat est un tuple de 3 valeurs

exercice : select products that have been ordered 
and sort them by title
from store.models import Product, OrderItem


def say_hello(request):
    queryset = OrderItem.objects.values('product_id')	

==> le résultat est une liste qui contient des doublons
on rajoute la méthode distinct à la fin pour élliminer les doublons

queryset = OrderItem.objects.values('product_id').distinct()

maintenant on selectionner tous les produits avec les id de tt 
à l'heure.

la solution sera donc
queryset = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')


==============================================================================================
			DEFERRING FIELDS
==============================================================================================

sélectionner uniquement les valeurs id et title de project
queryset = Product.objects.only('id','title')

différence entre values et only
only : spécifeir les fields qu'on veut lire de la base de données.
avec only => on a des instances comme résultat de la base de données.
avec values => on a des dictionnaires comme résultat de la base de données.

on utilise only uniquement quand on sait ce qu'on est entrain de faire surtout lors
de l'extraction d'un nombre important de données (base pleine).


une méthode contraire à only()
queryset = Product.objects.defer('description')




===================================================================
			SELECTING RELATED OBJECTS
===================================================================
Si on veut charger diffrents objets ensemble

queryset = Product.objects.all()

dans le html :
{{ product.title }} - {{ product.collection.title }}

l'orm dans ce cas va appeler uniquemant la table product.
si on appelle titre de collection, il va prendre beaucoup de temps pour charger
ce qu'on veut.
==> la solution est d'invoquer les tables en relation avec cette dernière.
queryset = Product.objects.select_related('collection').all()

autre exemple si la table contient une relation one to many (product - promotion)
queryset = Product.objects.prefetch_related('promotions').all()
--> une requète pour lire tous les colonnes de la table produit (jointure entre
les deux table produit et promotions).
--> une autre requête pour lire les promotions selon chaque prduit

autre exemple:
on veut charger tous les produits avec leurs promotions et collections.

Product.objects.prefetch_related('promotions').select_related('collection').all()
l'ordre n'a pas d'importance

exercice =
Get the last 5 orders with their customer and items (incl product)






























