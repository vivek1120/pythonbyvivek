import json

# sample json data
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'


# Convert the Python dictionary to a JSON string
json_string = json.loads(json_obj)

print(json_string)


