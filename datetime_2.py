from datetime import datetime, time, date, timedelta

datetime_now = datetime.now()
datetime_yesterday = datetime_now - timedelta(days=1)
datetime_30days_earlier = datetime_now - timedelta(days=30)

datetime_now = datetime_now.strftime('%d/%m/%Y')
datetime_yesterday = datetime_yesterday.strftime('%d/%m/%Y')
datetime_30days_earlier = datetime_30days_earlier.strftime('%d/%m/%Y')

date_string = '01/01/25 12:10:03.234567'
date_string_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
date_string_dt = date_string_dt.strftime('%d/%m/%y %H:%M:%S.%f')

print (datetime_yesterday)
print (datetime_now)
print (datetime_30days_earlier)
print (date_string_dt)
