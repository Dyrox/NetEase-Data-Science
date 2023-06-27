
import datetime
import pytz

def convert_timestamp_to_date(timestamp):
    timestamp /= 1000
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    timezone = pytz.timezone('Asia/Shanghai')
    dt = dt.replace(tzinfo=pytz.utc).astimezone(timezone)
    date_str = dt.strftime("%Y-%m-%d")
    return date_str
