import json

def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Define an unsorted dictionary
python_dict = {'a': 2, 'b': 1, 'c': 3}

# Sort the dictionary by values
sorted_dict = sort_dict_by_values(python_dict)

# Convert sorted dictionary to JSON
json_data_sorted_values = json.dumps(sorted_dict, indent=4)

print(json_data_sorted_values)
