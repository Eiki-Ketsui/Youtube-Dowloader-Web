from pytubefix import YouTube


def audio_itag_finder(yt):
    dicitagbis = {}
# liste de tous les itag audio disponibles pour la vidéo.
    for stream in yt.streams.filter(mime_type="audio/webm").order_by('abr').desc():
        stream_quality_sound_int = int(str(stream.abr).replace("kbps", ""))

# Selection de tous les itag audio au dessus de 10 kbps pour la vidéo.
        if stream_quality_sound_int >= 10 and stream.mime_type == "audio/webm":
            if stream_quality_sound_int not in dicitagbis:
                dicitagbis[stream_quality_sound_int] = [stream.itag]
            else:
                dicitagbis[stream_quality_sound_int].append(stream.itag)
        else:
            pass

# Lister des itag audio qui surpasse le seuil de 10 kbps en ordre décroissant, on choisira le premier et ainsi de suite..

    listedicitagbis = list(dict(sorted(dicitagbis.items(), key=lambda item: item[0], reverse=True)))
    itag_audio = dicitagbis[listedicitagbis[0]]
    ys = yt.streams.get_by_itag(itag_audio[0])
    return itag_audio[0]




def video_itag_finder(yt):
   
    dicitag = {}
    # Selection de tous les itag video au dessus de 144p pour la vidéo.

    for stream in yt.streams.filter(adaptive=True).order_by('resolution').desc():
        stream_resolution_int = int(str(stream.resolution).replace("p", ""))
        if stream_resolution_int >= 144 and stream.mime_type == "video/mp4":
            if stream_resolution_int not in dicitag:
                dicitag[stream_resolution_int] = [stream.itag]
            else:
                dicitag[stream_resolution_int].append(stream.itag)
        else:
            pass
    # Lister des itag video qui surpasse le seuil de 144p en ordre décroissant, on choisira le premier et ainsi de suite..
    listedicitag = list(dict(sorted(dicitag.items(), key=lambda item: item[0], reverse=True)))


    itag_video = dicitag[listedicitag[0]]

    ys = yt.streams.get_by_itag(itag_video[0])
    return itag_video[0]

