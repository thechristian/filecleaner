'''
Created on Jul 5, 2016

@author: ebo
'''
import csv, glob
import datetime
import os
import sys
import random


class DuplicateChecker(object):
	"""docstring for DuplicateChecker"""
	def __init__(self, filetype='csv', location=None):
		'''
		Constructor
		'''
		self.location = location

	def checkForDuplicate(self):
		newLines = []
		dupLines = []

	    files = glob.glob(self.location)
	    for eachfile in files:
	        filename = open(eachfile, 'r')

	        for line in filename:
	            if line not in newLines:
	                newLines.append(line)     # adding to the newLine list
	                noDuplicate = open('newfiles/newFile.csv', 'w')  # creating a new file to save entries without duplicate
	                noDuplicate.write(''.join(newLines))  # writing to the new file
	                noDuplicate.close()		# closing the file after writing
	            elif line in newLines:      # checking if each line entry already exist in the newline list
	                dupLines.append(line)	 # adding to the dupLines list
	                duplicated = open('static/duplicates/duplicate.csv', 'w')   # creating a new file to save duplicate entries
	                duplicated.write(''.join(dupLines))   # writing to the new file
	                duplicated.close()  # closing the file after writing
	    for i in xrange(1):
	        timer = datetime.datetime.now() 	# get date and time
	        timeAndDate = timer.isoformat()		# getting time and date without spaces
	        fullTime = timeAndDate.split(".")[0]    # removing unused string from the date and time
	        randomNumber = '%04.4f' % random.random()   # generate a random number to make the time unigue
	        finalTimeAndDate = '-'.join([fullTime, randomNumber]) 	# add time and date to the random number	


