import json
from decimal import Decimal

bills={'rent':1100, 'internet': 45, 'dramafever': 10, 'car': 465, 'utilities': 225, 'phones': 345, 'netflix': 14}
print(bills['rent'])

print(json.dumps(bills, ensure_ascii=False))
with open('bills.json', 'w') as f:
    json.dump(bills, f)
