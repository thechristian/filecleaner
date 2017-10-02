import os
import json
import pandas as pd
from utils import get_random_id
import xlsxwriter


def checkForDuplicateInRows(file_location, sname):
    # str(sname)
    datafile = pd.read_excel(file_location, sname)
    df = pd.DataFrame(datafile)

    df['Is_Duplicated'] = df.duplicated()

    writer = pd.ExcelWriter('dupcheck/dupRowsChecked-' + get_random_id() + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sname, index=False)
    writer.save()
    return True


def checkDuplicateInCol(upfname, sname, colname):
    # str(upfname)
    datafile = pd.read_excel(upfname, sname)
    df = pd.DataFrame(datafile)
    if colname in df:
        col_entries = df.loc[:, colname]
        writer = pd.ExcelWriter('dupcheck/dupColChecked-' + get_random_id() + '.xlsx', engine='xlsxwriter')
        df.loc[:, 'Duplicated ' + colname] = col_entries.duplicated()
        df.to_excel(writer, sheet_name=sname, index=False)
        writer.save()
        return True
    else:
        return "Column name does not exist"
