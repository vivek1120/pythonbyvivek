array = [1,2,-3,-5,0,2,0,-6]


def plusmines(arr):
    positive = 0
    negative = 0
    zero = 0
    for arr in array:
        if arr > 0:
            positive = positive + 1
        if arr < 0:
            negative +=1
        if arr == 0:
            zero += 1

    var = len(array) / positive
    var2 = len(array) / negative
    var3 = len(array) / zero
    print(f"{var:.6f}")
    print(f"{var2:.6f}")
    print(f"{var3:.6f}")
    
plusmines(array)

