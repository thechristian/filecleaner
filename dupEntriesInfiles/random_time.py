import random
import datetime

def findTimeAndDate():
    for i in xrange(1):
        timer = datetime.datetime.now()
        timeAndDate = timer.isoformat()
        fullTime = timeAndDate.split(".")[0]
        randomNumber = '%04.4f' % random.random()
        finalTimeAndDate = '-'.join([fullTime, randomNumber])
