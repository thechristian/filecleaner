from dupEntries import checkForDuplicateInRows, checkDuplicateInCol
from compareFiles import checkFile
import re
import pprint
from validate import emailvalidator, phonenumbvalidator
import os
from flask import Flask, render_template, request, Response, redirect, url_for
from werkzeug.utils import secure_filename
import sys
import random
import datetime
import hashlib
import csv, _csv
from utils import get_random_id, allowed_filecsv, allowed_filexl, allowed_files


app = Flask(__name__)
size = app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # upload file size allowed 3MB
app.config['uploadFolder'] = 'uploads'
SheetNameError = "Sheet name not provided"
FileNotSupportedError = "Error! File not supported. Upload the appropriate file type."
FileSizeError = "Error! File size too big. Check file and try again"
ColumnNameError = "Column name not provided"


@app.route("/")
def main():
    return render_template('index.html')  # web interface - form

@app.route("/compare")
def compare():
    return render_template('compare.html')  # web interface - form

@app.route('/compare-files', methods=['POST'])
def compare_files():
    # str = pprint.pformat(request.files['cfield'])
    #return Response(str, mimetype="text/text")

    if request.form.get('comparefiles'):
        compf2 = request.files['dataFile2']  # get file name from web interface
        filename2 = secure_filename(compf2.filename)
        upfname2 = os.path.join(app.config['uploadFolder'], get_random_id() + 'compf2-' + filename2)

        if size:
            compf2.save(upfname2)
            # checkFile(upfname1, upfname2)
            hashvalue1, hashvalue2, = checkFile(upfname1, upfname2)
            if hashvalue1 == hashvalue2:
                return render_template('same.html')
            else:
                return render_template('different.html')
        else:
            return FileSizeError


@app.route('/File-Cleaner', methods=['GET', 'POST'])  # getting all methods from the form
def upload_file():
    if request.method == 'POST':    # checking if its a post method
        f1 = request.files['dataFile1']  # get file name from web interface
        filename = secure_filename(f1.filename)
        upfname1 = os.path.join(app.config['uploadFolder'], get_random_id() + filename)
        f1.save(upfname1)

        #prepare actions
        row_dupes = request.form.get('check_dup_in_rows')
        col_dupes = request.form.get('dupInCols')
        col_email = request.form.get('emails')
        stats = {
            'row_dupes':{
                'status': False,
            },
            'col_dupes':{
                'status': False,
            },
            'col_email':{
                'status': False,
            }
        }

        # if the user checked to perform row duplication
        if row_dupes:
            if f1 and allowed_files(f1.filename):
                sheetname = request.form['sheetname']
                if sheetname == "":
                    return SheetNameError
                else:
                    checkForDuplicateInRows(upfname1, sheetname)
                    stats['row_dupes']['status'] = True
            else:
                return FileNotSupportedError
        # if not just go on
        else:
            pass
        
        # if the user checked to perform column duplication check, if not pass
        if col_dupes:
            sheetname = request.form['sheetname']
            colname = request.form['dupcolname']
            if sheetname != "" and colname != "":
                if f1 and allowed_files(f1.filename):
                    checkDuplicateInCol(upfname1, sheetname, colname)
                    stats['col_dupes']['status'] = True
                else:
                    return FileNotSupportedError
            else:
                return SheetNameError, ColumnNameError
        else:
            pass
        
        # if the user checked to perform email verification, and provides particular email column
        # if not, pass
        if col_email:
            sheetname = request.form['sheetname']
            colname = request.form['emailcol']
            if sheetname != "" and colname != "":
                if f1 and allowed_files(f1.filename):
                    emailvalidator(upfname1, sheetname, colname)
                    stats['col_email']['status'] = True
                else:
                    return FileNotSupportedError
            else:
                return SheetNameError, ColumnNameError
        else:
            pass

        return render_template('complete.html', res=stats)
