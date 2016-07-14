import pandas as pd
import xlsxwriter


def checkForDuplicate(location, sheetname):
    str(sheetname)
    datafile = pd.read_csv(location)
    df = pd.DataFrame(datafile)

    df['Is_Duplicated'] = df.duplicated()
    noduplicates = df.loc[df['Is_Duplicated'] == False]
    duplicates = df.loc[df['Is_Duplicated'] == True]
    del noduplicates['Is_Duplicated']
    writer1 = pd.ExcelWriter('noduplicates/noduplicates.xlsx', engine='xlsxwriter')
    noduplicates.to_excel(writer1, sheet_name=sheetname, index=False)
    writer1.save()
    # noduplicates.to_csv('noduplicates/noduplicates.csv', index=False, encoding='utf-8')
    del duplicates['Is_Duplicated']
    writer2 = pd.ExcelWriter('duplicates/duplicates.xlsx', engine='xlsxwriter')
    duplicates.to_excel(writer1, sheet_name=sheetname, index=False)
    writer2.save()
    #duplicates.to_csv('duplicates/duplicates.csv', index=False, encoding='utf-8')
