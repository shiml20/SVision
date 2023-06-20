from datetime import *


def str2time(str):
    return datetime.strptime(str, '%Y-%m-%d %H:%M:%S')


def time2str(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")
