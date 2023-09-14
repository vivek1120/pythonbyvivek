import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(type(python_obj))
print(type(json_obj))


