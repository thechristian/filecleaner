from dupEntries import checkForDuplicate
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['dataFile']
        filepath = os.path.join('uploaded', 'newfile')
        f.save(filepath)
        print type(f)
        checkForDuplicate(filepath)

if __name__ == "__main__":
    app.debug = True
    app.run()
