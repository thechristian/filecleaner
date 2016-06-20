import os
from flask import Flask, render_template, request, redirect, url_for
import sys
from dupFiles import checkFile
import random
import datetime
import hashlib

app = Flask(__name__)
size = app.config['MAX_CONTENT_LENGTH'] = (3 * 1024 * 1024)  # upload file size allowed 3MB

messsage1 = hashlib.sha256()   # calling hash function to use
messsage2 = hashlib.sha256()

for i in xrange(1):
    timer = datetime.datetime.now()  # get date and time
    timeAndDate = timer.isoformat()  # geting time and date without spaces
    fullTime = timeAndDate.split(".")[0]  # removing unused string from the date and time
    randomNumber = '%04.4f' % random.random()  # generate a random number to make the time unigue
    finalTimeAndDate = '-'.join([fullTime, randomNumber])  # add time and date to the random number

@app.route("/")
def main():
    return render_template('uploadfile.html')	 # web interface - form


@app.route('/upload', methods=['GET', 'POST'])	 # getting all methods from the form
def uploadfiles():
    if request.method == 'POST':
        f1 = request.files['dataFile1']  # get file name from web interface
        f2 = request.files['dataFile2']  # get file name from web interface

        if size:
            filepath1 = os.path.join('uploaded', 'userfile1-' + finalTimeAndDate)   # file saving destination and a file name with date
            filepath2 = os.path.join('uploaded', 'userfile2-' + finalTimeAndDate)  # file saving destination and a file name with date
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
            hashfile1.write(hashed1)    # saving the hash values to the file
            hashfile2.write(hashed2)

            # comparing hashes of the files to give the appropriate response
            if hashed1 == hashed2:
                return render_template('same.html')

            else:
                return render_template('different.html')
        else:
            return "Error! File size too big. Check file and try again"
        #checkFile(filepath1, filepath2)


if __name__ == "__main__":
    app.debug = True
    app.run()

