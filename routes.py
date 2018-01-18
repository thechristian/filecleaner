from dupEntries import checkForDuplicateInRows, checkDuplicateInCol
from compareFiles import checkFile
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore
from flask_login import current_user as current_user
from database import db_session, init_db
from models import User, Role
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
from utils import upload_folder, allowed_filecsv, allowed_filexl, allowed_files, collectSheets, email_folder
from flask_mail import Mail
from forms import ExtendedRegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
size = app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # upload file size allowed 3MB
app.config['uploadFolder'] = 'uploads'
SheetNameError = "Sheet name not provided"
FileNotSupportedError = "Error! File not supported. Upload the appropriate file type."
FileSizeError = "Error! File size too big. Check file and try again"
ColumnNameError = "Column name not provided"
#flask security

app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = 'salt'
app.config['SECURITY_SEND_REGISTER_EMAIL']  = False
# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session,User, Role)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    init_db()
    user_datastore.create_user(email='sbk@sbk.com', password='sbk',username='sbk2')
    db_session.commit()

def uploadedFiles():
    # list of files in upload folder
    userfolder = email_folder(current_user.email)
    upath = os.path.join(app.config['uploadFolder'], userfolder,'')
    if not os.path.exists(upath):
        os.makedirs(upath)
    uploaded = [f for f in os.listdir(upath)]
    uploadedFiles = {}
    for item in uploaded:
        path = os.path.join(app.config['uploadFolder'], userfolder, item)
        if os.path.isdir(path):
            uploadedFiles[item] = [f for f in os.listdir(path)]
        else:
            uploadedFiles['LEVEL'] = item
    return uploadedFiles

@app.route("/")
@login_required
def main():
    return render_template('index.html')  # web interface - form

@app.route("/file-manager", methods=['GET', 'POST'])
@login_required
def filemanager():
    return jsonify(files=uploadedFiles())

@app.route("/file-data", methods=['GET','POST'])
@login_required
def get_file_data():
    # for example getting excel sheets

    try:
        # get file path
        fine_file = str(request.args.get('string').strip()) # fine file name
        userfolder = email_folder(current_user.email)
        file_location = os.path.join(app.config['uploadFolder'], userfolder, fine_file)
        # call function to return requested file data
        data = collectSheets(file_location)
        return jsonify(data=data,status=True)
    except Exception as e:
        return jsonify(status=False,e=e)


@app.route("/compare")
@login_required
def compare():
    return render_template('compare.html')  # web interface - form

@app.route('/compare-files', methods=['POST'])
@login_required
def compare_files():
    # str = pprint.pformat(request.files['cfield'])
    #return Response(str, mimetype="text/text")

    if request.form.get('comparefiles'):
        compf2 = request.files['dataFile2']  # get file name from web interface
        filename2 = secure_filename(compf2.filename)
        userfolder = email_folder(current_user.email)
        upfname2 = os.path.join(app.config['uploadFolder'], userfolder, get_random_id() + 'compf2-' + filename2)

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
@login_required
def upload_file():
    if request.method == 'POST':    # checking if its a post method
        f1 = request.files['newdataFile1']  # get file name from web interface
        filename = secure_filename(f1.filename)
        time = datetime.datetime.now().time().isoformat().split('.')[0]
        userfolder = email_folder(current_user.email)
        upfname1 = os.path.join(upload_folder(app.config['uploadFolder'], userfolder), time + "." +filename)
        f1.save(upfname1)
        return jsonify(upstatus=True)
    else:
        return jsonify(upstatus=False)

@app.route('/File-Cleaner', methods=['GET', 'POST'])  # getting all methods from the form
@login_required
def clean_file():
    if request.method == 'POST':    # checking if its a post method
        filename = str(request.form.get('dataFile1').strip())  # get file name from web interface
        sheetname = str(request.form.get('sheetname').strip())
        userfolder = email_folder(current_user.email)
        dfile = os.path.join(app.config['uploadFolder'], userfolder, filename)

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
        userfolder = email_folder(current_user.email)
        # if the user checked to perform row duplication
        if row_dupes:
            if allowed_files(dfile):
                sheetname = sheetname
                if sheetname == "":
                    return SheetNameError
                else:
                    #let checkForDuplicateInRows return path to prepared file
                    result = checkForDuplicateInRows(dfile, sheetname, userfolder)
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
                    result = checkDuplicateInCol(dfile, sheetname, colname, userfolder)
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
                    result = emailvalidator(dfile, sheetname, colname, userfolder)
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
@login_required
def download_file():
    dfile = request.args.get('file')
    dfile_name = dfile.split('/')[-1]
    return send_file(dfile,as_attachment=True,attachment_filename=dfile_name)
