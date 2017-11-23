from dupEntries import checkForDuplicateInRows, checkDuplicateInCol
from compareFiles import checkFile
import re
import json
import pprint
from validate import emailvalidator #phonenumbvalidator
import os
from flask import Flask, render_template, request, Response, redirect, url_for, jsonify, send_file
from werkzeug.utils import secure_filename
import sys
import random
import datetime
import hashlib
import csv, _csv
from utils import upload_folder, allowed_filecsv, allowed_filexl, allowed_files, collectSheets


app = Flask(__name__)
size = app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # upload file size allowed 3MB
app.config['uploadFolder'] = 'uploads'
SheetNameError = "Sheet name not provided"
FileNotSupportedError = "Error! File not supported. Upload the appropriate file type."
FileSizeError = "Error! File size too big. Check file and try again"
ColumnNameError = "Column name not provided"

def uploadedFiles():
    # list of files in upload folder
    uploadedFiles = [f for f in os.listdir(os.path.join(app.config['uploadFolder'],''))]
    return uploadedFiles

@app.route("/")
def main():
    return render_template('index.html',files=uploadedFiles())  # web interface - form

@app.route("/files", methods=['GET', 'POST'])
def filescollect():
    return jsonify(files=uploadedFiles())

@app.route("/file-data", methods=['GET','POST'])
def get_file_data():
    # for example getting excel sheets
    print('here')

    try:
        # get file path
        fine_file = str(request.args.get('string').strip()) # fine file name
        file_location = os.path.join(app.config['uploadFolder'],fine_file)
        # call function to return requested file data
        data = collectSheets(file_location)
        return jsonify(data=data,status=True)
    except Exception as e:
        return jsonify(status=False,e=e)


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

# this would separately handle all file uploads
@app.route('/File-Upload',methods=['POST'])
def upload_file():
    if request.method == 'POST':    # checking if its a post method
        f1 = request.files['newdataFile1']  # get file name from web interface
        filename = secure_filename(f1.filename)
        time = datetime.datetime.now().time().isoformat().split('.')[0]
        upfname1 = os.path.join(upload_folder(app.config['uploadFolder']), time + "." +filename)
        f1.save(upfname1)
        return jsonify(upstatus=True)
    else:
        return jsonify(upstatus=False)

@app.route('/File-Cleaner', methods=['GET', 'POST'])  # getting all methods from the form
def clean_file():
    if request.method == 'POST':    # checking if its a post method
        filename = str(request.form.get('dataFile1').strip())  # get file name from web interface
        sheetname = str(request.form.get('sheetname').strip())
        dfile = os.path.join(app.config['uploadFolder'],filename)

        #return jsonify(filename = filename)
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
            if allowed_files(dfile):
                sheetname = sheetname
                if sheetname == "":
                    return SheetNameError
                else:
                    #let checkForDuplicateInRows return path to prepared file
                    result = checkForDuplicateInRows(dfile, sheetname)
                    stats['row_dupes']['status'] = True
                    stats['row_dupes']['result_path'] = result
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
                if allowed_files(dfile):
                    #let checkDuplicateInCol return path to prepared file
                    result = checkDuplicateInCol(dfile, sheetname, colname)
                    stats['col_dupes']['status'] = True
                    stats['col_dupes']['result_path'] = result
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
                if allowed_files(dfile):
                    # let emailvalidator return path to prepared file
                    result = emailvalidator(dfile, sheetname, colname)
                    stats['col_email']['status'] = True
                    stats['col_email']['result_path'] = result
                else:
                    return FileNotSupportedError
            else:
                return SheetNameError, ColumnNameError
        else:
            pass

        #return render_template('complete.html', res=stats)
        return jsonify(res=stats)

@app.route('/File-download', methods=['GET', 'POST'])  # download the requested file
def download_file():
    dfile = request.args.get('file')
    dfile_name = dfile.split('/')[-1]
    return send_file(dfile,as_attachment=True,attachment_filename=dfile_name)
