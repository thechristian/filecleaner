import pandas as pd
import xlrd
import xlwt
import csv
from utils import get_random_id
import os


def excel2csv(exlfilename, exlsheetname):
    workbook = xlrd.open_workbook(exlfilename)
    worksheet = workbook.sheet_by_name(exlsheetname)
    csvfile = os.path.join('uploads', 'frmxl2csv-' + get_random_id())
    dataframe = pd.DataFrame(worksheet)
    dataframe.to_csv(csvfile)

    return csvfile
