import random
import datetime

today = datetime.datetime.now()
year = (int(today.strftime("%Y")) - 18)
month = random.randint(1, 12)
day = random.randint(1, 28)

def generateDOB():
    return(datetime.date(random.randint(1901, year), month, day)).strftime("%m/%d/%Y")