
# Youtube_FLASK_DOWNLOADER

Le projet a pour but de télécharger des vidéos directement grâce à une url , la meilleure version audio & vidéo est automatiquement sélectionnée.

Des tests ont été faits pour des vidéos de 2h minutes et l'audio / la vidéo marche , 

- à voir pour des tests plus longs dans un futur.

## Comment est formé Youtube_FLASK_DOWNLOADER

Ce projet utilise uniquement du python et majoritairement la bibliothèque : 

pytubefix afin de récupérer l'audio et la vidéo.

Flask pour l'interface web

L'utilisation de ffmpeg est nécessaire pour merge les pistes audio et vidéo lorsque l'on prend une plus grande qualité.


## Comment Lancer Youtube_CLI_DOWNLOADER

La totalité du projet tient sur un docker compose.

### Lancer le docker

docker compose up -d 

puis rentrer dans le container ; pour cela vous devez avoir le nom du container, pour trouver le nom :

docker ps

Vous prendrez l'id du container.

docker exec -it NOM_DU_CONTAINER bash

Vous atterrirez sur le dossier code.

Vous n'avez plus qu'à lancer le programme en lançant :

python3 main.py

on vous demandera si vous voulez une vidéo ou un audio , à vous de choisir ça , puis on vous demandera le lien de l'url , sachez que la meilleure qualité est toujours prise. Des fois, les vidéos sont uniquement disponibles en 360p.

Ensuite la vidéo sera envoyée dans le dossier Video et l'audio sera envoyé dans le dossier Musique.

Vous pouvez récupérer les fichiers grâce au bindmount.

Merci.
Bonne journée
