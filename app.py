from flask import Flask, render_template
import time
from werkzeug.routing import BaseConverter

app = Flask(__name__, static_folder="static", template_folder="templates")

# Define a custom URL converter to strip the .html extension


class HTMLConverter(BaseConverter):
    def to_python(self, value):
        return value

    def to_url(self, value):
        return f"{value}.html"


# Add the custom converter to the app
app.url_map.converters['html'] = HTMLConverter


@app.route('/')
def ShredHead():
    return render_template('ShredHead.html')


@app.route('/loadingScreen')
def loadingScreen():
    return render_template('loadingScreen.html')


@app.route('/play')
def playScreen():
    return render_template('playScreen.html')

# Use the custom converter in your route


@app.route('/<html:page>')
def custom_pages(page):
    return render_template(page)


app.run(debug=True)
