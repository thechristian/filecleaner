from dupEntries import checkForDuplicate
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')	#web interface - form


@app.route('/upload', methods=['GET', 'POST'])	#getting all methods from the form
def upload_file():
    if request.method == 'POST': 	#checking if its a post method
        f = request.files['dataFile'] 	#get file name from web interface
        filepath = os.path.join('uploaded', 'newfile')	# file saving destination and a file name
        f.save(filepath) # save file to destination
        checkForDuplicate(filepath) 

if __name__ == "__main__":
    app.debug = True
    app.run()
