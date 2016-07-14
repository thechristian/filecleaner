import pandas as pd


def checkForDuplicate(location):
    datafile = pd.read_csv(location)
    df = pd.DataFrame(datafile)

    df['Is_Duplicated'] = df.duplicated()
    noduplicates = df.loc[df['Is_Duplicated'] == False]
    duplicates = df.loc[df['Is_Duplicated'] == True]
    del noduplicates['Is_Duplicated']
    noduplicates.to_csv('noduplicates/noduplicates.csv', index=False, encoding='utf-8')
    del duplicates['Is_Duplicated']
    duplicates.to_csv('duplicates/duplicates.csv', index=False, encoding='utf-8')
