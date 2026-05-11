#### IMPORTS ####
import os
import subprocess
import shutil
import contextlib

from pytubefix import YouTube
#from pytubefix.cli import on_progress

from .itag_finder import audio_itag_finder, video_itag_finder



def audio_et_video_download(yt, title):

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
    ys = yt.streams.get_by_itag(video_itag_finder(yt))
    with contextlib.redirect_stderr(None):
        ys.download(filename=filename_video_working)
    

    # Audio
    ys = yt.streams.get_by_itag(audio_itag_finder(yt))
    with contextlib.redirect_stderr(None):
        ys.download(filename=filename_audio_working)

   
    print("Téléchargement de la vidéo et de  l'audio terminé !")

####--####

    # Merge des deux fichiers
    subprocess.run(ffmpeg, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("\n\n\n")
    print(source_path)
    # Deplacement du fichier video final dans le dossier de destination
    shutil.move(source_path, destination_path)

    # suppression des fichiers temporaires
    os.remove(filename_audio_working)
    os.remove(filename_video_working)


    os.chdir(path_folder_code)
 


    return print("Fin du traitement de la vidéo !")


