import os
import json
import pandas as pd
from utils import get_random_id,clear_output_folder
import xlsxwriter


def checkForDuplicateInRows(file_location, sname):
    # str(sname)
    datafile = pd.read_excel(file_location, sname)
    df = pd.DataFrame(datafile)

    df['Is_Duplicated'] = df.duplicated()
    folder = 'dupcheck/username/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        pass
        #clear_output_folder(folder)
    dname = folder+'dupRowsChecked-' + get_random_id() + '.xlsx'
    writer = pd.ExcelWriter(dname, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sname, index=False)
    writer.save()
    return dname


def checkDuplicateInCol(upfname, sname, colname):
    # str(upfname)
    datafile = pd.read_excel(upfname, sname)
    df = pd.DataFrame(datafile)
    if colname in df:
        col_entries = df.loc[:, colname]
        folder = 'dupcheck/username/'
        if not os.path.exists(folder):
            os.mkdir(folder)
        else:
            pass
            #clear_output_folder(folder)
        dname = folder+'dupColChecked-' + get_random_id() + '.xlsx'
        writer = pd.ExcelWriter(dname, engine='xlsxwriter')
        df.loc[:, 'Duplicated ' + colname] = col_entries.duplicated()
        df.to_excel(writer, sheet_name=sname, index=False)
        writer.save()
        return dname
    else:
        return "Column name does not exist"
