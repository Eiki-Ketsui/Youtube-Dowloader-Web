from flask import Flask
from flask import request
from markupsafe import escape
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index</p>"

@app.route("/youtube_downloader",methods=['GET', 'POST'])
def youtube_downloader():
    
   

    if request.method == 'POST':
        data = request.form['url']
        print(data)
        return "The login form has been submitted"
    elif request.method == 'GET':
        searchword = request.args.get('url', 'value')
        print(searchword)
        return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')