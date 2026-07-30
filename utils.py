from datetime import datetime


def current_time():
    return datetime.now().strftime("%H:%M:%S")


def current_date():
    return datetime.now().strftime("%Y-%m-%d")
