from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = '123'
@app.route("/dingdonghello")
def index():
    flash("What is your name?")
    return render_template("index.html")

@app.route("/greet",methods=["POST", "GET"])
def greet():
    flash("Ding Dong Hello " + str(request.form['name_input']) + ", you idiot!")
    return render_template("lastpage.html")
    