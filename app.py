from flask import Flask, render_template
from gitmojithis import GithubRepo

app = Flask(__name__)

@app.route('/')
def home():
    stats = GithubRepo().scan('https:/github.com/krzystof/gitmojilint')
    if not stats.exists():
        return render_template('404.html')
    return render_template('home.html', stats = stats)
