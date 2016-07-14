from dupEntries import checkForDuplicate
from compareFiles import checkFile
import re
from validate import emailvalidator, phonenumbvalidator
import os
from flask import Flask, render_template, request, redirect, url_for
import sys
import random
import datetime
import hashlib
import csv, _csv
from utils import get_random_id
from convertocsv import excel2csv

app = Flask(__name__)
size = app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # upload file size allowed 3MB

ALLOWED_EXTENSIONS = set(['csv','xls', 'xlsx'])    # file extensions allowed


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def main():
    return render_template('index.html')  # web interface - form


@app.route('/File-Cleaner', methods=['GET', 'POST'])  # getting all methods from the form
def upload_file():
    filepath1 = os.path.join('uploads', 'frmxl2csv-' + get_random_id())
    if request.method == 'POST':    # checking if its a post method
        f1 = request.files['dataFile1']  # get file name from web interface
        if request.form.get('checkdup'):
            try:
                f1.save(filepath1)  # save file to destination
                sheetname = request.form['sheetname']
                csvfile = excel2csv(filepath1, sheetname)
                if csvfile and allowed_file(csvfile):
                    checkForDuplicate(csvfile, sheetname)     # calling the check4duplicate function

                    noduplicatefilesize = os.path.getsize('noduplicates/noduplicates.xlsx')  # file size in bytes from separated entries
                    uploadedfilesize = os.path.getsize(filepath1)  # file size from uploaded user file
                    if noduplicatefilesize == uploadedfilesize:
                        return render_template('noduplicate.html')
                    else:
                        return render_template('success.html')

                else:
                    return "Error! File not supported. Upload the appropriate file type."
            except:
                return "Sheet name not given!"

        if request.form.get('comparefiles'):
            compf1 = request.files['dataFile1']  # get file name from web interface
            comp2 = request.files['dataFile2']  # get file name from web interface
            compfilepath1 = os.path.join('uploads', 'compUserFile1-' + get_random_id())
            compfilepath2 = os.path.join('uploads', 'compUserFile2-' + get_random_id())

            if size:
                compf1.save(compfilepath1)  # save file to destination
                comp2.save(compfilepath2)
                hashvalue1, hashvalue2, = checkFile(compfilepath1, compfilepath2)
                if hashvalue1 == hashvalue2:
                    return render_template('same.html')

                else:
                    return render_template('different.html')
            else:
                return "Error! File size too big. Check file and try again"

        elif request.form.get('emails'):
            try:
                sheetname = request.form['sheetname']
                csvfile = excel2csv(filepath1, sheetname)
                # f1.save(filepath1)  # save file to destination
                col = request.form['emailcol']
                emailvalidator(csvfile, col)
                # change to anything later
                return "nice"
            except:
                return "Sheet name not given!"
        else:
            return "No options selected."

