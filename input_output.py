import json
from decimal import Decimal
import fileinput
import filecmp

bills={'rent':1100, 'internet': 45, 'dramafever': 10, 'car': 465, 'utilities': 225, 'phones': 345, 'netflix': 14}
extras=['gcc', 'paypal', 'j_phone', 'g_phone', 'a_phone', 'v_phone', 'p_training', 'p_boarding']
new_bal = 0

for line in fileinput.input():
    bill, amount = line.split()
    if bill in extras:
        with open ('extras.json') as handle:
            parsed = json.load(handle)
            if parsed[bill] > float(amount):
                new_bal = float(parsed[bill]) - float(amount)
                print('this here bill {} is {} and the amount your paying is {} so you still owe {}'.format(bill, parsed[bill], float(amount), new_bal))
                parsed[bill] = new_bal
                with open('temp.json', 'a') as extra_write:
                    json.dump(parsed, extra_write)
                print(parsed)

    else:
        print('reg bill')



print(json.dumps(bills, ensure_ascii=False))
with open('bills.json', 'w') as f:
    json.dump(bills, f)

with open('bills.json', 'r') as handle:
    parsed = json.load(handle)
    parsed['car'] == 450
    print(parsed['car'])
with open('temp.json', 'r') as handle:
    parsed = json.load(handle)
    print(parsed)
