import json

with open('paid.json', 'w') as f:
    new ={
      "rent": False,
      "internet": False,
      "dramafever": False,
      "car": False,
      "utilities": False,
      "phones": False,
      "netflix": False,
      "hbo": False,
      "gcc": False,
      "spotify": False,
      "navient": False
    }
    print(new, file=f)
