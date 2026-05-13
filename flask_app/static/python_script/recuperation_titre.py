from pytubefix import YouTube
#from pytubefix.cli import on_progress

def verification_url(url: str):
    print("hello your link is : ",url)
    print("Section une: Validation de l'URL & recuperation du titre")
    if "&list" not in url:
        print("URL Validée :", url)
        pass
    else:
        url = modification_url(url)
        print("Nettoyage de l'URL")
    return url

def modification_url(url):
    is_valid = "&list" in url
    if is_valid:
        url = url.split("&list")[0]
        return url
    else:
        return url


def recuperation_titre(yt):
    
    title = yt.title
    print(f"Titre de la vidéo : {title}")
    return title
    