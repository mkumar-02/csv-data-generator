import datetime
import random

def dateGenerate(min_date, max_date):
    format = "%Y/%m/%d"
    start_date = datetime.datetime.strptime(min_date, format).date()
    end_date = datetime.datetime.strptime(max_date, format).date()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)


    return random_date
