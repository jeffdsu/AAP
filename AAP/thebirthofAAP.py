from flask import Flask, render_template
from AAP import AAP

app = Flask(__name__)

@app.route("/user")
def createUser():
    return render_template("AAP.html")

@app.route("/")
def hello():
    return render_template("AAP.html")

if __name__ == "__main__":
    yourFriendAAP = AAP ()
    app.run()