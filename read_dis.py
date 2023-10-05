def read_file(file_loc):
    try:
        with open(file_loc, 'r') as reffer:
            actual_content = reffer.read()
            print(actual_content)
    except Exception as e:
        print(f"{e}")

location = "/home/vivek/developer/TypingSpeedTes/typing_speed_test.py"
read_file(location)