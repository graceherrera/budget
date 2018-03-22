#!/usr/bin/python3

import sys
import fileinput
import time
import datetime
from datetime import date
import json

income = 0
leftover = 0
rbills = 0
ebills = 0
ubills = 0
total_bills = 0

bills={}
extras={}
temp={}
bank=0
paycheck=0
print('What was your paycheck amount?')
paycheck=float(input())
print('What was your checking balance?')
bank=float(input())
income = bank + paycheck

now = datetime.date.today()
report_name = 'BReport ' + str(now)
print ('Your report: {} should now be ready to read'.format(report_name))

with open('extra.json', 'r') as f:
    temp = json.load(f)
    extras= temp
with open('bills.json', 'r') as f:
    temp = json.load(f)
    bills = temp

with open(report_name, 'w') as report:
    print(report_name, '\n', file=report)
    print('Your total income with paycheck and balance is {}'.format(income), file=report)
    for line in fileinput.input():
        bill, amount = line.split()
        if bill in bills:
            rbills += float(amount)
            if float(bills[bill]) != float(amount):
                print('{} is budgeted for ${} and the bill is actually ${}. You saved ${}. Should you reassess the balance assigned to this bill.'.format(bill, bills[bill], amount, float(bills[bill])- float(amount)), file=report)
        elif bill in extras:
            ebills += float(amount)
            if float(extras[bill]) != float(amount):
                print('The amount you owe for {} is ${}. You have made a payment for ${}. Your new balance is {}'.format(bill, extras[bill], amount, float(extras[bill])- float(amount)), file=report)
                new_balance = float(extras[bill]) - float(amount)
                extras.update({bill: new_balance})
        else:
            print('You have an unaccounted for bill: {} ${}'.format(bill, amount), file=report)
            ubills += float(amount)
    total_bills = ebills + rbills + ubills
    leftover = income - total_bills
    print('The total extra bills this pay period are: ${}'.format(ebills), file=report)
    print('The total unaccounted for bills this pay period are: ${}'.format(ubills), file=report)
    print('The total bills for this period are {}. You have leftover {}'.format(total_bills, leftover), file=report)
with open('extra.json', 'w') as f:
    json.dump(extras, f)
