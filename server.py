from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__,static_folder='static')
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/transfer", methods= ["GET","POST"])
def returnFile():
    if request.method == "POST":
        data = request.form["data"]
        print("fjdslkfjdsl")
        return "fdsafsd"
    return render_template("QuestionAnswer.html")
# @app.route("/ask", methods= ["GET","POST"])
# def checkData():
#     if request.method == "POST":
#         data = request.form["data"]
#         print(data)
#         return render_template("QuestionAnswer.html")