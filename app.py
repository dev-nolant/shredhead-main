from flask import Flask, render_template
import time

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route('/')
def ShredHead():
    return render_template('ShredHead.html')


@app.route('/loadingScreen')
def loadingScreen():
    return render_template('loadingScreen.html')


app.run(debug=True, port='8080')
