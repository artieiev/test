import json

with open('group_people.json','r') as file:
    t = json.load(file)
   
for i in t:
    c = 0
    for j in i['people']:
        if j['gender'] =='Female' and j['year'] > 1977:
            c+=1
    print(c)