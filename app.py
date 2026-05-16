import sys
sys.stdout.reconfigure(encoding='utf-8')

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("New Message Received")
    print(name, email, message)

    return redirect("/")

@app.route("/project/portfolio")
def portfolio_project():
    return render_template("portfolio_project.html")

@app.route("/project/todo")
def todo_project():
    return render_template("todo_project.html")


if __name__ == "__main__":
    app.run(debug=True)# my-portfolio-ruhulaminbd.com
