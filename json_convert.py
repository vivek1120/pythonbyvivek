import json

data ={
    "name": "vivke",
    "age":20,
    "sex":"male"
}

jsonfile = json.dumps(data)

print(type(jsonfile))


dictfile = json.loads(jsonfile)

print(type(dictfile))


print("name: ",jsonfile["name"])

