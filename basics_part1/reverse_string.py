def reverse_string(input):
    #using slicing method
    reversed = input[::-1]
    return reversed
result = reverse_string("vivek")


#using loop
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

#using list
def reverse_string(input_string):
    char_list = list(input_string)
    print(char_list)
    char_list.reverse()
    print(type(char_list))
    reversed_string = ''.join(char_list)
    print(type(reversed_string))
    return reversed_string



