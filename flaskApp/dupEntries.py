import csv, glob
import datetime
import os
import sys
import random

newLines = list()		# list for holding new entries
dupLines = list()		# list for holding duplicate entries


def checkForDuplicate(location):
    files = glob.glob(location)
    for eachfile in files:
        filename = open(eachfile, 'r')

        for line in filename:
            if line not in newLines:
                newLines.append(line)     # adding to the newLine list
                noDuplicate = open('newfiles/newFile.csv', 'w')  #creating a new file to save entries without duplicate
                noDuplicate.write(''.join(newLines))  # writing to the new file
                noDuplicate.close()		# closing the file after writing
            elif line in newLines:      #checking if each line entry already exist in the newline list
                dupLines.append(line)	# adding to the dupLines list
                duplicated = open('duplicatefiles/duplicate.csv', 'w')     #creating a new file to save duplicate entries
                duplicated.write(''.join(dupLines))   # writing to the new file
                duplicated.close()  # closing the file after writing
    for i in xrange(1):
        timer = datetime.datetime.now() 	#get date and time
        timeAndDate = timer.isoformat()		#geting time and date without spaces
        fullTime = timeAndDate.split(".")[0]	#removing unused string from the date and time
        randomNumber = '%04.4f' % random.random()	# generate a random number to make the time unigue
        finalTimeAndDate = '-'.join([fullTime, randomNumber]) 	#add time and date to the random number
    os.rename('duplicatefiles/duplicate.csv', 'duplicatefiles/duplicate.csv-' + finalTimeAndDate) 	#rename the output file with finalTimeAndDate
    os.rename('newfiles/newFile.csv', 'newfiles/newFile.csv-' + finalTimeAndDate)		#same
   # print "All done -  Entries separated from duplicates and saved separately"

