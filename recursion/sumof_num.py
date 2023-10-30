#program to calculate the sum of a list of numbers.

def list_sum(num_List):
    # Base case: if the list has only one element, return that element
    if len(num_List) == 1:
        return num_List[0]
    else:
        # Recursive case: add the first element to the sum of the rest of the list
        return num_List[0] + list_sum(num_List[1:])
        
# Example usage of the function
reuslt = list_sum([2, 4, 5, 6, 7])

print(reuslt)