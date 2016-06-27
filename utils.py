import random
from datetime import datetime


ALLOWED_EXTENSIONS = set(['csv', 'txt', 'xlsx', 'xls'])

def get_random_id():
	'''
	Generate a random ID (from specs) to be used in naming the user files.
	likely to be removed soon
	@return String 
	'''
	for i in xrange(1):
		# get date and time
	    timer = datetime.now()
	    # geting time and date without spaces
	    timeAndDate = timer.isoformat()
	    # removing unused string from the date and time
	    fullTime = timeAndDate.split(".")[0]
	    # generate a random number to make the time unigue
	    randomNumber = '%04.4f' % random.random()
	    # add time and date to the random number
	    finalTimeAndDate = '-'.join([fullTime, randomNumber])	

	return finalTimeAndDate

def allowed_file(filename):
	'''
	Return true if file type is part of the allowed list of files
	@return Boolean
	'''
	#TODO: 
	# Make proper check here. Allow xlsx and xls files also. 
	# Might have to do some conversion to .csv first
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS