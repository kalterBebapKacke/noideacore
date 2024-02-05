import datetime
from dateutil.relativedelta import relativedelta


def format_now(date):
    datetime_object = datetime.datetime.strptime(date, '%y-%m-%d %H:%M:%S')
    return datetime_object
def format_all(date):
    datetime_object = datetime.datetime.strptime(date, '%d-%m-%y %H:%M:%S')
    return datetime_object

def format(date):
    datetime_object = datetime.datetime.strptime(date, '%d-%m-%y')
    return datetime_object

def current():
    now = datetime.datetime.now()
    return now

def add(date, months:int=0, days:int=0, years:int=0, minutes:int=0, seconds:int=0, hours:int=0):
    if months != 0:
        return date + relativedelta(months=months)
    if days != 0:
        return date + relativedelta(days=days)
    if years != 0:
        return date + relativedelta(years=years)
    if minutes != 0:
        return date + relativedelta(minutes=minutes)
    if seconds != 0:
        return date + relativedelta(seconds=seconds)
    if hours != 0:
        return date + relativedelta(hours=hours)




