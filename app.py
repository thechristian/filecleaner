from dupEntries import checkForDuplicate
from compareFiles import checkFile
import os
from flask import Flask, render_template, request, redirect, url_for
import sys
import random
import datetime
import hashlib
import csv, _csv

app = Flask(__name__)
size = app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024 #upload file size allowed 3MB
messsage1 = hashlib.sha256()   # calling hash function to use
messsage2 = hashlib.sha256()


ALLOWED_EXTENSIONS = set(['csv', 'txt'])    #file extensions allowed

for i in xrange(1):
    timer = datetime.datetime.now()  # get date and time
    timeAndDate = timer.isoformat()  # getting time and date without spaces
    fullTime = timeAndDate.split(".")[0]  # removing unused string from the date and time
    randomNumber = '%04.4f' % random.random()  # generate a random number to make the time unigue
    finalTimeAndDate = '-'.join([fullTime, randomNumber])  # add time and date to the random number

# checking for appropriate file extensions


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def main():
    return render_template('index.html')  # web interface - form


@app.route('/checkduplicates', methods=['GET', 'POST'])  # getting all methods from the form
def upload_file():
    filepath = os.path.join('dupuploaded', 'userFile.csv-' + finalTimeAndDate)
    if request.method == 'POST': 	# checking if its a post method
        f = request.files['dataFile'] 	# get file name from web interface
        if f and allowed_file(f.filename):
            # filepath = os.path.join('uploaded', 'userFile.csv-' + finalTimeAndDate)
            # os.rename('userFile.csv', 'userFile.csv-' + finalTimeAndDate)
            f.save(filepath)   # save file to destination
            checkForDuplicate(filepath)     # calling the check4duplicate function

            newfilesize = os.path.getsize('newfiles/newFile.csv')  # file size in bytes from separated entries
            uploadedfilesize = os.path.getsize(filepath)  # file size from uploaded user file
            if newfilesize == uploadedfilesize:
                return render_template('noduplicate.html')
            else:
                return render_template('success.html')

        else:
            return "Error! File not supported."


# comparing files

@app.route('/comparefiles', methods=['GET', 'POST'])  # getting all methods from the form
def uploadfiles():
    if request.method == 'POST':
        f1 = request.files['dataFile1']  # get file name from web interface
        f2 = request.files['dataFile2']  # get file name from web interface

        if size:
            filepath1 = os.path.join('compareuploaded', 'userfile1-' + finalTimeAndDate)  # file saving destination and a file name with date
            filepath2 = os.path.join('compareuploaded', 'userfile2-' + finalTimeAndDate)
            f1.save(filepath1)  # save file to destination
            f2.save(filepath2)

            # file1 = raw_input("Enter a file name 1: ")  # taking a file names
            # file2 = raw_input("Enter a file name 2: ")
            openfile1 = open(filepath1, mode='r')  # opening file in read mode
            openfile2 = open(filepath2, mode='r')
            content1 = openfile1.read()  # reading the content of the file
            content2 = openfile2.read()
            messsage1.update(content1)  # passing the content of the file to the hash function
            messsage2.update(content2)
            hashed1 = messsage1.hexdigest()  # generating the hash value of the file content
            hashed2 = messsage2.hexdigest()
            hashfile1 = open('hashes/hashvalue1', 'w')  # creating a file to save the hash values
            hashfile2 = open('hashes/hashvalue2', 'w')
            hashfile1.write(hashed1)  # saving the hash values to the file
            hashfile2.write(hashed2)

            # comparing hashes of the files to give the appropriate response
            if hashed1 == hashed2:
                return render_template('same.html')

            else:
                return render_template('different.html')
        else:
                    return "Error! File size too big. Check file and try again"



                    # return render_template('success.html')

# newfilesize = os.path.getsize('newfiles/newFile.csv')
# uploadedfilesize = os.path.getsize(filepath)
# if newfilesize == uploadedfilesize:
#     render_template('noduplicate.html')
# else:
#     render_template('success.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
