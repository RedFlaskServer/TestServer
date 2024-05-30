from flask import Flask, redirect, request, render_template, send_file
from pickles import get_pickle, dump_pickle

app = Flask(__name__)

names = []

@app.route('/pygame')
def home():
    return render_template('pygame_index.html')

@app.route('/game')
def game():
    return send_file('pygame_pngs/game_output.png', mimetype='image/png')

@app.route("/redirect-external", methods=["GET"])
def redirect_external():
    return redirect("https://bonk.io/", code=302)


@app.route("/redirect-internal", methods=["GET"])
def redirect_internal():
    return redirect("/users", code=302)


@app.route("/users", methods=["GET"])
def landing():
    names_disp = get_pickle("names.pickle")
    return f"{names_disp}"\
            '<br>'\
            '<br>'\
            '<a href="/">Menu</a>'

@app.route("/greetings")
def greet():
    return  'Hello There'\
            '<br>'\
            '<br>'\
            '<a href="/">Main</a>'

@app.route('/r', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       names.append(f"{first_name} {last_name}")
       dump_pickle("names.pickle", names)
       return   f'Your name is {first_name} {last_name}'\
                '<br>'\
                '<br>'\
                '<a href="/users">See Users</a>'
    return render_template("form.html")

cheeses = []
@app.route('/login', methods =["GET", "POST"])
def cheesey():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       cheeses.append(f"{first_name} {last_name}")
       dump_pickle("cheese.pickle", cheeses)
       return   f'Your username is {first_name} and password is {last_name}'\
                '<br>'\
                '<br>'\
                # '<a href="/users">See Users</a>'
    return render_template("cheese.html")


@app.route("/", methods=["GET"])
def index():
    return '<a href="/redirect-internal">Internal redirect</a>' \
           '<br>' \
           '<a href="/redirect-external">External redirect</a>'\
           '<br>'\
           '<a href="/greetings">Say Hi</a>'\
           '<br>'\
           '<a href="https://google.com">Google</a>'\
           '<br>'\
           '<a href="/r">test</a>'\
           '<br>'\
           '<a href="/login">give pass</a>'\
           '<br>'\
           '<a href="/pygame">pygame</a>'\
           '<br>'



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4080)
