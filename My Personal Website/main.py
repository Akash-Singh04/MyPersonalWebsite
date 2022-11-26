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

@app.route('/tindog')
def tindog():
    return render_template("tindog.html")
    
@app.route('/lofisongplayer')
def lofisongplayer():
    return render_template("lofi-song-player.html")


if __name__=="__main__":
    app.run()
