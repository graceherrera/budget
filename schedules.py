#!/usr/bin/python3

import sys
import fileinput
import time
import datetime
from datetime import date

schedules={'rent': 1, 'internet': 5, 'dramafever': 9, 'car': 22, 'utilities': 23, 'phones': 11, 'netflix': 14, 'HBO':17, 'gcc':15}

now = datetime.date.today()
today = str(now)
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
                print('Has this bill: {}, been paid already? If not it is {} days late.'.format(bill, late), file=report)
            else:
                early = schedules[bill] - day_num
                print('Yay you are {} days early paying {}'.format(early, bill), file=report)
        else:
            print('The bill: {} is not in your scheduled bills? Do you need to add it?'.format(bill), file=report)
