import json


with open('manager_sales.json') as f:
    data = json.load(f)
o=0     
for i in data:
    c=0
    for g in i["cars"]:
        c+=g['price']
    if c>o:
        o = c
        name = i['manager']['first_name']
        l_name = i['manager']['last_name']

print(o,name,l_name)