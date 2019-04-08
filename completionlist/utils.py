from datetime import datetime
import time


def from_dt(dt):
    return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S").timestamp()


def dt_of_timestamp(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def now():
    return int(time.time())
