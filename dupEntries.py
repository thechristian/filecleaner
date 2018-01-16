import os
import json
import pandas as pd
from utils import get_random_id,clear_output_folder
import xlsxwriter


def checkForDuplicateInRows(file_location, sname, userfolder):
    # str(sname)
    datafile = pd.read_excel(file_location, sname)
    df = pd.DataFrame(datafile)
    folder = os.path.join('dupcheck',userfolder,'')
    df['Is_Duplicated'] = df.duplicated()
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        pass
        #clear_output_folder(folder)
    dname = folder+'dupRowsChecked-' + get_random_id() + '.xlsx'
    writer = pd.ExcelWriter(dname, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sname, index=False)
    writer.save()
    return dname


def checkDuplicateInCol(upfname, sname, colname,userfolder):
    # str(upfname)
    datafile = pd.read_excel(upfname, sname)
    df = pd.DataFrame(datafile)
    folder = os.path.join('dupcheck',userfolder,'')
    if colname in df:
        col_entries = df.loc[:, colname]
        if not os.path.exists(folder):
            os.makedirs(folder)
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
