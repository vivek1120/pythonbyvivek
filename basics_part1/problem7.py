list = [1,2,3,4,3,2,1,2,3,4,3,2,1,2,4,3,2,3,2,3,4,5,4,3,2,1,2,3,4,5]

def count_num(list):
    var = 0
    for lists in list:
        if lists == 4:
            var = var + 1
    return var

print(count_num(list))