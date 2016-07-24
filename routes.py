from dupEntries import checkForDuplicatexl, checkForDuplicatecsv
from compareFiles import checkFile
import re
from validate import emailvalidator, phonenumbvalidator
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys
import random
import datetime
import hashlib
import csv, _csv
from utils import get_random_id, allowed_filecsv, allowed_filexl, excel_to_csv


app = Flask(__name__)
size = app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # upload file size allowed 3MB
app.config['uploadFolder'] = 'uploads'

@app.route("/")
def main():
    return render_template('index.html')  # web interface - form


@app.route('/File-Cleaner', methods=['GET', 'POST'])  # getting all methods from the form
def upload_file():
    if request.method == 'POST':    # checking if its a post method
        f1 = request.files['dataFile1']  # get file name from web interface
        if request.form.get('check_dup_in_rows'):
            if f1 and allowed_filexl(f1.filename):
                filename = secure_filename(f1.filename)
                upfname = os.path.join(app.config['uploadFolder'], get_random_id() + filename)
                f1.save(upfname)
                sheetname = request.form['sheetname']
                if sheetname == "":
                    return " Sheet name not given!"
                else:
                    csvfile = excel_to_csv(upfname, sheetname)
                    checkForDuplicatexl(csvfile, sheetname)

                noduplicatefilesize = os.path.getsize('noduplicates/noduplicates.xlsx')  # file size in bytes from separated entries
                uploadedfilesize = os.path.getsize(csvfile)  # file size from uploaded user file
                if noduplicatefilesize == uploadedfilesize:
                    return render_template('noduplicate.html')
                else:
                    return render_template('success.html')

            elif f1 and allowed_filecsv(f1.filename):
                filename = secure_filename(f1.filename)
                upfname = os.path.join(app.config['uploadFolder'], get_random_id() + filename)
                f1.save(upfname)
                checkForDuplicatecsv(upfname)

                noduplicatefilesize = os.path.getsize('duplicates/duplicates.csv')
                uploadedfilesize = os.path.getsize(upfname)
                if noduplicatefilesize == uploadedfilesize:
                    return render_template('noduplicate.html')
                else:
                    return render_template('success.html')

            else:
                return "Error! File not supported. Upload the appropriate file type."

        if request.form.get('comparefiles'):
            compf1 = request.files['dataFile1']  # get file name from web interface
            compf2 = request.files['dataFile2']  # get file name from web interface
            filename1 = secure_filename(compf1.filename)
            filename2 = secure_filename(compf2.filename)
            upfname1 = os.path.join(app.config['uploadFolder'], get_random_id() + 'compf1-' + filename1)
            upfname2 = os.path.join(app.config['uploadFolder'], get_random_id() + 'compf2-' + filename2)

            if size:
                compf1.save(upfname1)  # save file to destination
                compf2.save(upfname2)
                hashvalue1, hashvalue2, = checkFile(upfname1, upfname2)
                if hashvalue1 == hashvalue2:
                    return render_template('same.html')

                else:
                    return render_template('different.html')
            else:
                return "Error! File size too big. Check file and try again"

        elif request.form.get('emails'):
            sheetname = request.form['sheetname']

            if sheetname != "":
                if f1 and allowed_filexl(f1.filename):
                    filename = secure_filename(f1.filename)
                    upfname = os.path.join(app.config['uploadFolder'], get_random_id() + filename)
                    f1.save(upfname)
                    csvfile = excel_to_csv(upfname, sheetname)  # set path properly
                    col = request.form['emailcol']
                    emailvalidator(csvfile, col)
                else:
                    return "File not supported!"
                # change to anything later
            else:
                return "Sheet name not given!"
            return "nice"
        else:
            return "No options selected."

