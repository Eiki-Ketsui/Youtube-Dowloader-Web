#### IMPORTS ####
from pytubefix import YouTube

import os
import subprocess
import contextlib

from .itag_finder import audio_itag_finder



def audio_only_download(yt, title,audio_quality):

    ## variables
    audio = int(nettoyage_audio_quality(audio_quality))
    categorie = "Musique"

    dossier_destination = "/NOMORE_YOUTUBE/Media/Musique/"
    dossier_travail = "/NOMORE_YOUTUBE/Code"

    titre_musique = f"{title}.webm"


    #### Selection du itag parmis les streams disponibles pour la meilleurs qualité de l'audio ####
    ys = yt.streams.get_by_itag(audio_itag_finder(yt,audio))

    ####Changement du répertoire pour aller sur le dossier music ####

    os.chdir(dossier_destination)

    #### Téléchargement de la musique ####
    with contextlib.redirect_stderr(None):
        ys.download()

    

    # retour dans le dossier de travail
    os.chdir(dossier_travail)

    return print("Fin de téléchargement de la musique !")


def nettoyage_audio_quality(audio_quality):
    final = audio_quality.split('kbps')[0]
    return final