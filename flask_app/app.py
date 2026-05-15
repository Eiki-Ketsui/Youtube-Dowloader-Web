from flask import Flask,flash,request,render_template,url_for,send_file,redirect
from markupsafe import escape

from pytubefix import YouTube

from static.python_script.recuperation_titre import verification_url,recuperation_titre
from static.python_script.audio_and_video import audio_et_video_download
from static.python_script.audio_only import audio_only_download

app = Flask(__name__)
app.secret_key = "Sachin"

@app.route("/")
def index():
    return redirect(url_for("youtube_downloader"))
   
@app.route("/youtube_downloader",methods=['GET', 'POST'])
def youtube_downloader():
    
   

    if request.method == 'POST':
        return "The login form has been submitted"

    elif request.method == 'GET':
        download_type = "Video"
        url = request.args.get('url', 'value')
        
        video_quality = request.args.get('type', 'value')
        
        audio_quality = request.args.get('type2', 'value')
        print(audio_quality)
        if url == "value" or url == "":
            flash("Veuillez entrer une URL valide !")

            return render_template('index.html')

        else:
            pass
        url = verification_url(url)
    
    
        yt = YouTube(url)

        title = recuperation_titre(yt)
        #redirect(url_for("chargement"))
        if download_type == "Video":

            audio_et_video_download(yt, title)
            flash(f"Tu as bien telecharger {title} en mp4")
            return redirect(url_for("youtube_downloader"))

        elif download_type == "Musique":
            audio_only_download(yt,title)
            flash(f"Tu as bien telecharger {title} en mp3")
            return redirect(url_for("youtube_downloader"))


        

    return render_template('index.html')


@app.route("/chargement")
def chargement():
    return render_template('chargement.html')
   






@app.route('/stream')
def stream_file():
    name_fichier = "test.mp4"
    path_dossier = "/NOMORE_YOUTUBE/Media/Video/"
    path = path_dossier + name_fichier

    return send_file(
        path,
        as_attachment=False,
        mimetype='video/mp4'
    )
    '''

@app.route('/stream')
def stream_file():
    name_fichier = "test.mp4"
    path_dossier = "/NOMORE_YOUTUBE/Media/Video/"
    path = path_dossier + name_fichier

    return send_file(
        path,
        as_attachment=False,
        mimetype='video/mp4'
    )
'''
@app.route('/download')
def download_file():
    name_fichier = "test.mp4"
    path_dossier = "/NOMORE_YOUTUBE/Media/Video/"
    path = path_dossier + name_fichier
    
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')