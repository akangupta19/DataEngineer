import datetime
from datetime import date
def differ_days(date1, date2):

    a = date1
    b = date2
    return (a-b).days


print(differ_days((date(2019,3,16)), date(2019,3,10)))
