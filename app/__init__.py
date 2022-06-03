import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/fellow/<name>')
def show_profile(name):
    return render_template('index.html', title=name, url=os.getenv("URL"))

