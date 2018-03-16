#!/usr/bin/python3

import sys
import fileinput
import time
import datetime
from datetime import date

income = 2429.84
leftover = 0
rbills = 0
ebills = 0
ubills = 0
total_bills = 0

bills={'rent':1100, 'internet': 45, 'dramafever': 10, 'car': 465, 'utilities': 225, 'phones': 345, 'netflix': 14, 'HBO': 15}
extras={"p_training": 200, "p_boarding": 75, "paypal": 4000, "gcc": 5500.0, "j_phone": 298, "g_phone": 490, "a_phone": 375, "v_phone": 674}

f= ['rent', 'internet']
s=[]
t=[]
now = datetime.date.today()
report_name = 'BReport ' + str(now)
print (report_name)

with open(report_name, 'w') as report:
    print(report_name, '\n', file=report)
    for line in fileinput.input():
        bill, amount = line.split()
        if bill in bills:
            rbills += float(amount)
            if float(bills[bill]) != float(amount):
                print('{} is budgeted for ${} and the bill is actually ${}. You saved ${}'.format(bill, bills[bill], amount, float(bills[bill])- float(amount)), file=report)
        elif bill in extras:
            ebills += float(amount)
            if float(extras[bill]) != float(amount):
                print('The amount you owe for {} is ${}. You have made a payment for ${}. Your new balance is {}'.format(bill, extras[bill], amount, float(extras[bill])- float(amount)), file=report)
                new_balance = float(extras[bill]) - float(amount)
                extras[bill] = new_balance
        else:
            print('You have an unaccounted for bill: {} ${}'.format(bill, amount), file=report)
            ubills += float(amount)
    total_bills = ebills + rbills + ubills
    leftover = income - total_bills
    print('The total extra bills this pay period are: ${}'.format(ebills), file=report)
    print('The total unaccounted for bills this pay period are: ${}'.format(ubills), file=report)
    print('The total bills for this period are {}. You have leftover {}'.format(total_bills, leftover), file=report)
