from datetime import datetime as dt

def get_timestamp():
    unformatted_time=dt.now()
    formatted_time=unformatted_time.strftime("%Y%m%d%H%M%S")
    return formatted_time