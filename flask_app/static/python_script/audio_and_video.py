#### IMPORTS ####
import os
import subprocess
import shutil
import contextlib
import time

from pytubefix import YouTube
#from pytubefix.cli import on_progress

from .itag_finder import audio_itag_finder, video_itag_finder
from .audio_only import nettoyage_audio_quality



def audio_et_video_download(yt, title,video_quality,audio_quality):

    audio =  int(nettoyage_audio_quality(audio_quality))
    video =  int(nettoyage_video_quality(video_quality))
    #Mise en place des variables
    categorie = "Video"

    filename_video_working = "video.mp4"
    
    filename_audio_working = "audio.webm"

    filename_audio_video_merged = "final_video.mp4"
    titre = f"{title}.mp4"
    
    path_folder_src = "/NOMORE_YOUTUBE/Media/Working_folder/"
    path_folder_code = "/NOMORE_YOUTUBE/Code"
    source_path = path_folder_src + filename_audio_video_merged
    destination_path = f"/NOMORE_YOUTUBE/Media/Video/{titre}"

   
    ffmpeg = f"ffmpeg -i {filename_video_working} -i {filename_audio_working} -c:v copy -c:a copy {filename_audio_video_merged} -y"

    # deplacement dans le dossier du travail

    os.chdir(path_folder_src)


    # Video
    
    ys = yt.streams.get_by_itag(video_itag_finder(yt,video))
    with contextlib.redirect_stderr(None):
        ys.download(filename=filename_video_working)
    print("Testo")


    # Audio
    ys = yt.streams.get_by_itag(audio_itag_finder(yt,audio))
    
    with contextlib.redirect_stderr(None):
        ys.download(filename=filename_audio_working)
    

    print("Téléchargement de la vidéo et de  l'audio terminé !")

####--####
    print(os.listdir(path_folder_src))

    # Merge des deux fichiers
    subprocess.run(ffmpeg, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(source_path,destination_path,filename_audio_video_merged,titre ,"STOOOOP")
    # Deplacement du fichier video final dans le dossier de destination
    

    #shutil.move(source_path, destination_path)
    os.rename(source_path,destination_path)
    # suppression des fichiers temporaires
    os.remove(filename_audio_working)
    os.remove(filename_video_working)


    os.chdir(path_folder_code)
 


    return print("Fin du traitement de la vidéo !")


def nettoyage_video_quality(video_quality):
    final = video_quality.split('p')[0]
    return final