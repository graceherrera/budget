import json

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}
data_copy={}

json_str = json.dumps(data)

data = json.loads(json_str)


# Reading data back
with open('data.json', 'r') as f:
     data = json.load(f)
     data_copy = data


data_copy.update({'name': 'GRACE'})
print(data_copy)

# Writing JSON data
with open('data.json', 'w') as f:
     json.dump(data_copy, f)
