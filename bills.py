#!/usr/bin/python3

import sys
import fileinput
import time
import datetime
from datetime import date
import json

now = datetime.date.today()
print(now, '\n')

total_cycle1 = 0
total_cycle2 = 0

print('Cycle 1 should include bills from dates after 13th of the month to the 25th. Cycle 2 should include bills that need to be paid after the 25th and before the 13th\n')

cycle = input("What cycle are we on? ")
cycle = int(cycle)
income = input("what was the amount of your paycheck? ")
income = int(income)
bank_balance = input("what is the amount in your account? ")
bank_balance = int(bank_balance)

total_income = income + bank_balance

with open('bills') as f:
    for line in f:
        bill, date, amt, institution = line.split()
        amt = int(amt)
        date = int(date)
        if cycle == 1:
            if date < 13:
                total_cycle1 = total_cycle1 + amt
                print(bill, date)
        else:
            if date >= 13:
                total_cycle2 = total_cycle2 + amt
                print(bill, date)

if cycle == 1:
    print(total_income - total_cycle1)
else:
    print(total_income - total_cycle2)
