import csv
import os
import sys
import random
import datetime

filename = open('excel.csv', 'r') #opening the file in read mode
#filecontent.split('\n')         #spliting each line of the file
newLines = list()		# list for holding new entries
dupLines = list()		# list for holding duplicate entries


def checkForDuplicate():
    for line in filename:
        if line not in newLines:
            newLines.append(line)     # adding to the newLine list
            noDuplicate = open('newFile', 'w')  #creating a new file to save entries without duplicate
            noDuplicate.write(''.join(newLines))  # writing to the new file
            noDuplicate.close()		# closing the file after writing
        elif line in newLines:      #checking if each line entry already exist in the newline list
            dupLines.append(line)	# adding to the dupLines list
            duplicated = open('duplicate', 'w')     #creating a new file to save duplicate entries
            duplicated.write(''.join(dupLines))   # writing to the new file
            duplicated.close()  # closing the file after writing

    for i in xrange(1):
        timer = datetime.datetime.now()
        timeAndDate = timer.isoformat()
        fullTime = timeAndDate.split(".")[0]
        randomNumber = '%04.4f' % random.random()
        finalTimeAndDate = '-'.join([fullTime, randomNumber])
    os.rename('duplicate', 'duplicate-' + finalTimeAndDate)
    os.rename('newFile', 'newFile-' + finalTimeAndDate)
    print "All done - new files saved without duplicate"

checkForDuplicate()
