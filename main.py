from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exegesis')
def exegesis():
    return render_template('exegesis.html')

@app.route('/head')
def head():
    return render_template('head.html')

@app.route('/paragraph')
def paragraph():
    return render_template('paragraph.html')

if __name__ == '__main__':
    app.run()