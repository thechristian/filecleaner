import pandas as pd
from pandas import DataFrame
import xlrd
import xlwt
import csv
from utils import get_random_id
import os


def excel2csv(x, y):
    exlfilename = str(x)
    exlsheetname = str(y)
    df = pd.read_excel(exlfilename, exlsheetname)
    csvfileloc = os.path.join('uploads', 'frmxl2csv-' + get_random_id() + '.csv')
    df.to_csv(csvfileloc, index=False)
    return csvfileloc

