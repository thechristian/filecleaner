from dupEntries import checkForDuplicate
import os
from flask import Flask, render_template, request, redirect, url_for
import sys
import random
import datetime

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024 #upload file size allowed 3MB

ALLOWED_EXTENSIONS = set(['csv','txt '])    #file extensions allowed

for i in xrange(1):
    timer = datetime.datetime.now()  # get date and time
    timeAndDate = timer.isoformat()  # geting time and date without spaces
    fullTime = timeAndDate.split(".")[0]  # removing unused string from the date and time
    randomNumber = '%04.4f' % random.random()  # generate a random number to make the time unigue
    finalTimeAndDate = '-'.join([fullTime, randomNumber])  # add time and date to the random number

#checking for appropriate file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def main():
    return render_template('index.html')	#web interface - form

@app.route('/upload', methods=['GET', 'POST'])	#getting all methods from the form
def upload_file():
    if request.method == 'POST': 	#checking if its a post method
        f = request.files['dataFile'] 	#get file name from web interface
        if f and allowed_file(f.filename):
            filepath = os.path.join('uploaded', 'userFile.csv-' + finalTimeAndDate)	# file saving destination and a file name with date
            #os.rename('userFile.csv', 'userFile.csv-' + finalTimeAndDate)
            f.save(filepath) # save file to destination
            checkForDuplicate(filepath)
        else:
            return "Error! Check file extension and upload again."
    return render_template('success.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
