import pandas as pd
import xlsxwriter


def checkForDuplicatexl(location, sname):
    str(sname)
    datafile = pd.read_csv(location)
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


def checkForDuplicatecsv(location):
    datafile = pd.read_csv(location)
    df = pd.DataFrame(datafile)

    df['Is_Duplicated'] = df.duplicated()
    noduplicates = df.loc[df['Is_Duplicated'] == False]
    duplicates = df.loc[df['Is_Duplicated'] == True]
    del noduplicates['Is_Duplicated']
    noduplicates.to_csv('noduplicates/noduplicates.csv', index=False, encoding='utf_16')
    del duplicates['Is_Duplicated']
    duplicates.to_csv('duplicates/duplicates.csv', index=False, encoding='utf_16')
