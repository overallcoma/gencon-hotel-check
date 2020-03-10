import datetime
import os


def string_to_bool(truefalse):
    if truefalse == "true":
        return True
    if truefalse == "false":
        return False


def all_dates_list(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    delta = end - start
    date_range = []
    for date in range(delta.days + 1):
        day = start + datetime.timedelta(days=date)
        day = datetime.datetime.strftime(day, "%Y, %m, %d").replace(' 0', ' ')
        date_range.append(day)
    return date_range


def string_to_list(string):
    string = string.replace(" ", "")
    list_return = []
    if "," in string:
        list_return = string.split(",")
    else:
        list_return.append(string)
    return list_return


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
