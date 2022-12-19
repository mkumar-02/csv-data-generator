import datetime
import random

def dateGenerate(min_date, max_date, date_format):
    updatedFormat = date_format.replace('dd','%d').replace('mm','%m').replace('yyyy','%Y').replace('yy','%y')
    start_date = datetime.datetime.strptime(min_date, updatedFormat).date()
    end_date = datetime.datetime.strptime(max_date, updatedFormat).date()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    updateRandomDate = random_date.strftime(updatedFormat)
    return updateRandomDate


