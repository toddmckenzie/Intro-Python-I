"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

date1 = input("please enter month")
date2 = input("please enter a year")
today = datetime.today()

# def days(*args):
#     print(args)
#     if len(args) == 1 and args[0] == '':
#          print(calendar.prmonth(today.year, today.month))
#     elif len(args) == 1:
#         datez=[]
#         for i in args:
#             datez.append(i)
#         if len(datez) == 1:
#             print(calendar.prmonth(today.year, int(args[0])))
#         elif len(datez) == 2:
#             print(calendar.prmonth(datez[1], datez[0]))
#         else: 
#             print("Wrong format given. Enter month, year")    
#     else:
#         print("Wrong format given. Enter month, year")

def days(*args):
  if date1 == '':
    print(calendar.prmonth(today.year, today.month))
  elif date1 != '' and date2 == '':
    print(calendar.prmonth(today.year, int(date1)))
  elif date1 != '' and date2 != '':
    print(calendar.prmonth(int(date2), int(date1)))
  else:
    print("Wrong format given.")

days(date1, date2)
