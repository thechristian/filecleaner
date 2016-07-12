import random
from datetime import datetime


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