from pytubefix import YouTube
#from pytubefix.cli import on_progress
import time 

import io, contextlib



def Selection_url(url):

    print("Section une: Validation de l'URL & recuperation du titre")
    if "&list" not in url:
        print("URL Validée :", url)
        pass
    else:
        url = modification_url(url)
        print("Nettoyage de l'URL")


    yt = YouTube(url)

    return yt

def modification_url(url):
    is_valid = "&list" in url
    if is_valid:
        url = url.split("&list")[0]
        return url
    else:
        return url


def Selection_title(yt):
    print("Récupération du titre")
    title = yt.title
    print(f"Titre de la vidéo : {title}")
    return title
