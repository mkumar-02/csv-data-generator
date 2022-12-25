import datetime
import random

def generate_date(min_date, max_date, date_format):
    modify_format = date_format.replace('dd','%d').replace('mm','%m').replace('yyyy','%Y').replace('yy','%y')
    start_date = datetime.datetime.strptime(min_date, modify_format).date()
    end_date = datetime.datetime.strptime(max_date, modify_format).date()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    update_random_date_format = random_date.strftime(modify_format)
    return update_random_date_format


