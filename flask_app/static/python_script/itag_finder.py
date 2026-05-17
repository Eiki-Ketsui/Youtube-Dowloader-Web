from pytubefix import YouTube


def audio_itag_finder(yt,qualitychoosed):
    dictionnaire = recuperation_tableau_data(yt,"musique")
    dicitagbis = {}
    print(qualitychoosed,"musique")
    value = selection_version_choisis(dictionnaire,qualitychoosed,"musique")
# liste de tous les itag audio disponibles pour la vidéo.
    if value == "abs":
        print("il n'y a pas la qualité demandé")
        selection_autre_meilleur_version(dictionnaire,qualitychoosed)
    else:
        print("la qualité ",qualitychoosed,"existe au itag ", value)
        return value

    exit()

    for stream in yt.streams.filter(mime_type="audio/webm").order_by('abr').desc():
        stream_quality_sound_int = int(str(stream.abr).replace("kbps", ""))

# Selection de tous les itag audio au dessus de a la qualité choisis pour la vidéo.
        if stream_quality_sound_int == qualitychoosed and stream.mime_type == "audio/webm":

            if stream_quality_sound_int == qualitychoosed and stream.mime_type == "audio/webm":
                
                if stream_quality_sound_int not in dicitagbis:
                    dicitagbis[stream_quality_sound_int] = [stream.itag]

  

# Lister des itag audio qui surpasse le seuil de 10 kbps en ordre décroissant, on choisira le premier et ainsi de suite..

    listedicitagbis = list(dict(sorted(dicitagbis.items(), key=lambda item: item[0], reverse=True)))
    print(dicitagbis)
    itag_audio = dicitagbis[listedicitagbis[0]]
    ys = yt.streams.get_by_itag(itag_audio[0])
    print("itag AUDIO  choisis :", itag_audio[0])
    return itag_audio[0]




def video_itag_finder(yt,qualitychoosed):
    dictionnaire = recuperation_tableau_data(yt,"video")
    print(qualitychoosed,"video")
    value = selection_version_choisis(dictionnaire,qualitychoosed,"video")
    if value == "abs":
        print("il n'y a pas la qualité demandé")
        selection_autre_meilleur_version(dictionnaire,qualitychoosed)

    else:
        print("la qualité ",qualitychoosed,"existe au itag ", value)
        return value
    # Selection de tous les itag video au dessus de 144p pour la vidéo.
    exit()
    for stream in yt.streams.filter(adaptive=True).order_by('resolution').desc():
        stream_resolution_int = int(str(stream.resolution).replace("p", ""))
        if stream_resolution_int == qualitychoosed and stream.mime_type == "video/mp4":
            dicitag[stream_resolution_int] = [stream.itag]

    # Lister des itag video qui surpasse le seuil de 144p en ordre décroissant, on choisira le premier et ainsi de suite..
    listedicitag = list(dict(sorted(dicitag.items(), key=lambda item: item[0], reverse=True)))
    print(dicitag)


    itag_video = dicitag[listedicitag[0]]

    ys = yt.streams.get_by_itag(itag_video[0])
    print("itag AUDIO  choisis :",  itag_video[0])

    return itag_video[0]



#etape 1 Récuperer tout les données  que ça soit video ou audio.
def recuperation_tableau_data(yt,typeofstream):
    dictionnaire = {}
    print("HELLO RECUPERATIONTABLEAUDATA FONCTION")

    if typeofstream == "musique":
        for stream in yt.streams.filter(mime_type="audio/webm").order_by('abr').desc():
            dictionnaire[stream.abr] = [stream.itag][0]

            print(stream,'musique')
    
    elif  typeofstream == "video":
        for stream in yt.streams.filter(adaptive=True).order_by('resolution').desc():
            dictionnaire[stream.resolution] = [stream.itag][0]
            
    print(dictionnaire)
    return dictionnaire
  
#etape 2 Faire un programme pour selectionner la version choisis.
def selection_version_choisis(dictionnaire, qualitychoosed,typedestream):
    if typedestream == "musique":
        qualitychoosed = str(qualitychoosed) +"kbps"
    if typedestream == "video":
        qualitychoosed = str(qualitychoosed) +"p"

    for key,value in dictionnaire.items():
        if key == qualitychoosed:
            return value
        else:
            print(key == qualitychoosed,key,qualitychoosed)

    return "abs"
#etape 3 Si aucune version correspond a la version choisis ,choisir la meilleurs version equivalente (exemple 4k non dispo -> 1080p / 720p non dispo -> 480p)
def selection_autre_meilleur_version(dictionnaire,qualitychoosed):
    tableauqualityvideo=[2160,1440,1080,720,480,360,240,144];
    tableauqualityaudio=[160,50];


    print(qualitychoosed, "in ",tableauqualityvideo)
    print(qualitychoosed in tableauqualityvideo)
    print(qualitychoosed, "in ",tableauqualityaudio)
    print(qualitychoosed in tableauqualityaudio)
    print("audio", qualitychoosed)
    print(dictionnaire,qualitychoosed)
    tableau = []
    for key, value in dictionnaire.items():
        print(key)
        tableau.append(key)
    tableau.sort()
    tableau.reverse()
    print("la qualité la plus proche est : " ,tableau[0])

#CONCEPT A POUSSER.
#array = [1, 3, 5, 7, 9]
#element = 5
#print(element in array)