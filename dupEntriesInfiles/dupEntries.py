import csv

filename = open('samplecsv', 'r') #opening the file in read mode
#filecontent.split('\n')         #spliting each line of the file
newLines = list()		# list for holding new entries
dupLines = list()		# list for holding duplicate entries
def checkForDuplicate():
    for line in filename:
        if line not in newLines:
            newLines.append(line)     # adding to the newLine list
            noDuplicate = open('newFile.csv', 'w')  #creating a new file to save entries without duplicate
            noDuplicate.write(''.join(newLines))  # writing to the new file
            #noDuplicate.close()		# closing the file after writing
        elif line in newLines:      #checking if each line entry already exist in the newline list
            dupLines.append(line)	# adding to the dupLines list
            duplicated = open('duplicate.csv', 'w')     #creating a new file to save duplicate entries
            duplicated.write(''.join(dupLines))   # writing to the new file
            #duplicated.close()  # closing the file after writing
    print "All done - new files saved without duplicate"

checkForDuplicate()
