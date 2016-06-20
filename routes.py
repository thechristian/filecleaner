from flask import Flask, render_template, request, redirect, url_for
from dupEntries import checkForDuplicate
from utils import get_random_id, allowed_file
import os
import sys

import csv, _csv

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024 #upload file size allowed 3MB

@app.route("/")
def main():
    return render_template('index.html')  # web interface - form

# i dont think it allowing a GET on a POST route is necessary 
@app.route('/upload', methods=['POST'])
def upload_file():
    finalTimeAndDate = get_random_id()
    filepath = os.path.join('uploaded', 'userFile.csv-' + finalTimeAndDate)
    if request.method == 'POST': 	# checking if its a post method
        f = request.files['dataFile'] 	# get file name from web interface
        if f and allowed_file(f.filename):
            #filepath = os.path.join('uploaded', 'userFile.csv-' + finalTimeAndDate)
            # os.rename('userFile.csv', 'userFile.csv-' + finalTimeAndDate)
            f.save(filepath)   # save file to destination
            checkForDuplicate(filepath)     # calling the check4duplicate function

            newfilesize = os.path.getsize('newfiles/newFile.csv') # file size in bytes from separated entries
            uploadedfilesize = os.path.getsize(filepath) # file size from uploaded user file
            if newfilesize == uploadedfilesize:
                return render_template('noduplicate.html')
            else:
                return render_template('success.html')
        else:
            return "Error! File not supported."