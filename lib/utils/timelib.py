import os
import time

def current_epoch():
    return int(time.time())

def date_to_epoch(dateString, strFormat="%Y-%m-%d"):
    return time.mktime(time.strptime(dateString, strFormat))

def epoch_to_date(t, strFormat="%Y-%m-%d"):
    return time.strftime(strFormat, time.localtime(t))
