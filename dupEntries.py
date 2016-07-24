import pandas as pd
import xlsxwriter

dup_col_numbers = []

def checkForDuplicatexl(file_location, sname):
    str(sname)
    datafile = pd.read_csv(file_location)
    df = pd.DataFrame(datafile)

    df['Is_Duplicated'] = df.duplicated()
    noduplicates = df.loc[df['Is_Duplicated'] == False]
    duplicates = df.loc[df['Is_Duplicated'] == True]
    del noduplicates['Is_Duplicated']
    writer1 = pd.ExcelWriter('noduplicates/noduplicates.xlsx')
    noduplicates.to_excel(writer1, sheet_name=sname, index=False)
    writer1.save()
    del duplicates['Is_Duplicated']
    writer2 = pd.ExcelWriter('duplicates/duplicates.xlsx', engine='xlsxwriter')
    duplicates.to_excel(writer1, sheet_name=sname, index=False)
    writer2.save()


def checkForDuplicatecsv(file_location):
    datafile = pd.read_csv(file_location)
    df = pd.DataFrame(datafile)

    df['Is_Duplicated'] = df.duplicated()
    noduplicates = df.loc[df['Is_Duplicated'] == False]
    duplicates = df.loc[df['Is_Duplicated'] == True]
    del noduplicates['Is_Duplicated']
    noduplicates.to_csv('noduplicates/noduplicates.csv', index=False, encoding='utf_16')
    del duplicates['Is_Duplicated']
    duplicates.to_csv('duplicates/duplicates.csv', index=False, encoding='utf_16')


def checkDuplicateInCol(file_location, col_name):
    i = 0
    dup_Entry_col_numbers = []
    str(file_location)
    data_file = pd.read_csv(file_location, index_col=False)
    if col_name in data_file:
        col_entries = data_file.loc[:, col_name]
        col_entries['Is_Duplicated'] = col_entry.duplicated()
        for entry in col_entries['Is_Duplicated']:
            if entry == True:
                i = i + 1
                index = str(i)
                dup_Entry_col_numbers.append(index)

        dup_Entry_col_file = open('duplicates/duplicateColNumbers.csv', 'w')
        Dataframe = pd.DataFrame(dup_Entry_col_numbers, columns=["Duplicated Column Entry Numbers"])
        Dataframe.to_csv(dup_Entry_col_file, index=False)

    else:
        return "Column name does not exist"


