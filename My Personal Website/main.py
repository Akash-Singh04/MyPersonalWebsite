from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
app = Flask(__name__)
bootstrap = Bootstrap4(app)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/blogwebsite')
def blogwebsite():
    return render_template("blogwebsite.html")

@app.route('/tinderbot')
def tinderbot():
    return render_template("tinder-bot.html")

@app.route('/twitterbot')
def twitterbot():
    return render_template("twitter-bot.html")

@app.route('/aiimagegenerator')
def aiimagegenerator():
    return render_template("aiimagegenerator.html")

    
@app.route('/lofisongplayer')
def lofisongplayer():
    return render_template("lofi-song-player.html")


@app.route('/sleepsense')
def sleepsense():
    return render_template("sleepsense.html")



if __name__=="__main__":
    app.run(debug=True)
