from flask import Flask
from flask import request
from markupsafe import escape
from flask import url_for
from flask import render_template

app = Flask(__name__)

test = '/hello?name=<script>alert("bad")</script>"'

@app.route("/")
def index():
    return "<p>index page</p>"

@app.route('/youtube_downloader')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route("/helo")
def hello_world():
    return "<p>Hello, World!</p>"

#template
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route("/without_escape")
def hello_without_escape():
    name = request.args.get("name",test )
    return f"Hello, {name}!"

@app.route("/with_escape")
def hello_escape():
    name = request.args.get("name",test )
    return f"Hello, {escape(name)}!"

#variable
@app.route("/user/<username>")
def user_profile(username):
    return f'User: {escape(username)}' # escape c'est contre les prompt injection

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post: {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {escape(subpath)}'

# Converter types:
# string: accepts any text without a slash (default)
# int: accepts integers
# float: accepts positive floating-point values
# path: like string but also accepts slashes
# uuid: accepts UUID strings

# Unique URLs / Redirection Behavior

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "The login form has been submitted"
    else:
        return "The login page"


''' Alternative.
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
'''

@app.route('/profile')
def profile():
    return 'The profile page'

# URL Building


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='css/style.css'))

# Rendering Templates


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
