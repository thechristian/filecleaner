import csv, glob
import pandas as pd
import os
import sys
import random
from pandas import DataFrame

newLines = list()		# list for holding new entries
dupLines = list()		# list for holding duplicate entries


def checkForDuplicate(location):
    files = glob.glob(location)
    for eachfile in files:
        filename = open(eachfile, 'r')

        for line in filename:
            if line not in newLines:
                newLines.append(line)     # adding to the newLine list
                noDuplicate = open('newfiles/newFile.csv', 'w')  # creating a new file to save entries without duplicate
                df = pd.DataFrame(newLines)
                df.to_csv(noDuplicate)

            elif line in newLines:      # checking if each line entry already exist in the newline list
                dupLines.append(line)	 # adding to the dupLines list
                duplicated = open('duplicatefiles/duplicate.csv', 'w')   # creating a new file to save duplicate entries
                df = pd.DataFrame(dupLines)
                df.to_csv(duplicated)
