from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")

def home():

    n="Namya"
    a=13

    return render_template("index.html", name=n, age=a)

@app.route("/father")

def home2():

    n="Papa"
    a=100

    return render_template("index.html", name=n, age=a)

@app.route("/mother")

def home3():

    n="Mumma"
    a=101

    return render_template("index.html", name=n, age=a)

@app.route("/friend")

def home4():

    n="Bhumi"
    a=13

    return render_template("index.html", name=n, age=a)


app.run(debug=True)
