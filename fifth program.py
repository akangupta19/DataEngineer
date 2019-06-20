import calendar
'''
yy = 2019
mm = 6

print(calendar.month(yy, mm))
'''
'''
y = int(input("Input the year : "))
m = int(input("Input the month : "))
d = int(input("Input the day : "))
print(calendar.month(y, m,d))
'''


cal = calendar.month(2019, 6,20)
print ("Here is the calendar:")
print (cal)