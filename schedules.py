#!/usr/bin/python3

import sys
import fileinput
import time
import datetime
from datetime import date
import json

schedules={}
with open('schedules.json', 'r') as f:
    schedules = json.load(f)

now = datetime.date.today()
today = str(now)
month = today[5] + today[6]
day = today[8] + today[9]
day_num = int(day)

report_name = 'BReport ' + str(now)

print (report_name)

with open(report_name, 'a') as report:
    print('\nBSchedule',str(now), '\n', file=report)
    for line in fileinput.input():
        bill, amount = line.split()
        if bill in schedules:
            if schedules[bill] < day_num:
                late = day_num - schedules[bill]
                print('The bill: {}, was due on {}/{} are you paying the next months bill? If not it is {} days late.'.format(bill,month,   schedules[bill], late), file=report)
            else:
                early = schedules[bill] - day_num
                print('You are {} days early paying {}'.format(early, bill), file=report)
        else:
            print('The bill: {} is not in your scheduled bills? Do you need to add it?'.format(bill), file=report)
    print('These are the bills that should have been paid by now:', file=report)
    for key, value in schedules.items():
        if value < day_num:
            print(key, value, file=report)
    print('These are the upcoming bills:', file=report)
    for key, value in schedules.items():
        if value > day_num:
            print(key, value, file=report)
    print('These bills are due now!:', file=report)
    for key, value in schedules.items():
        if value == day_num:
            print(key, value, file=report)
