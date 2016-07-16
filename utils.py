import random
from datetime import datetime


ALLOWED_EXTENSIONSxl = set(['xls', 'xlsx'])    # file extensions allowed
ALLOWED_EXTENSIONScsv = set('csv')


def allowed_filexl(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONSxl


def allowed_filecsv(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONScsv


def get_random_id():
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