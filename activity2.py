import random
import time
def randomdate(startdate,enddate):
    print(f"print random date between{startdate} to {enddate}")
    randomgenerator=random.random()
    date_format="%m/%d/%Y"
    start_time=time.mktime(time.strptime(startdate,date_format))
    end_time=time.mktime(time.strptime(enddate),date_format)
    random_time=start_time+randomgenerator*(end_time-start_time)
    random_date=time.strftime(date_format,time.localtime(random_time))
    return random_date,random_time
print(f"random date is {randomdate("4/6/2017","1/1/2025")}")