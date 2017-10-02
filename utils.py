import random
from datetime import datetime
import pandas as pd
from pandas import DataFrame
# import xlrd
# import xlwt
import csv
import os

ALLOWED_EXTENSIONSxl = set(['xls', 'xlsx'])    # file extensions allowed
ALLOWED_EXTENSIONS = set(['xls', 'xlsx', 'csv'])    # file extensions allowed
ALLOWED_EXTENSIONScsv = set(['csv'])


def allowed_filexl(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONSxl

def allowed_files(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def allowed_filecsv(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONScsv


def get_random_id():

    for i in xrange(1):
        # get date and time
        timer = datetime.now()
        # geting time and date without spaces
        timeAndDate = timer.isoformat()
        # removing unused string from the date and time
        fullTime = timeAndDate.split(".")[0]
        # generate a random number to make the time unigue
        randomNumber = '%04.4f' % random.random()
        # add time and date to the random number

        today_folder = '-'.join([fullTime,randomNumber])
    return today_folder

def upload_folder(uploadFolder):
    # I am thinking we could group files in folders according to date
    # and use time as the random string
    for i in xrange(1):
        # get date and time
        timer = datetime.now()
        # geting time and date without spaces
        # removing unused string from the date and time
	    #fullTime = timeAndDate.split(".")[0]
        # generate a random number to make the time unigue
	    #randomNumber = '%04.4f' % random.random()
        # add time and date to the random number


        #get only time without unused string
        #
        #time = timer.time().isoformat().split('.')[0]
        #append time during upload
        #
        # get only date
        date = timer.date().isoformat()
        # date/time
        today_folder = os.path.join(uploadFolder,date)
        if not os.path.exists(today_folder):
            os.mkdir(os.path.join(today_folder))
    return today_folder


def excel_to_csv(fname, sname):
    file_name = str(fname)
    reading_Excel = pd.ExcelFile(file_name)
    sheet_list = reading_Excel.sheet_names
    if sname in sheet_list:
        # file_name = str(fname)
        worksheet_name = str(sname)
        file_contents = pd.read_excel(fname, worksheet_name)
        file_path = os.path.join('uploads', 'frmxl2csv-' + get_random_id() + '.csv')
        file_contents.to_csv(file_path, index=False)
    else:
        return "Sheet does not exist."
    return file_path

def collectSheets(file_location):
    datafile = pd.read_excel(file_location,sheetname=None)
    sheets = datafile.keys()
    return sheets
