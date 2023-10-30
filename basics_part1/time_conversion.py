def convert_to_military_time(time_str):
    hours, minutes, am_pm = time_str[:-2], time_str[-5:-3], time_str[-2:]
    
    if am_pm == 'PM' and hours != '12':
        hours = str(int(hours) + 12)
    elif am_pm == 'AM' and hours == '12':
        hours = '00'
    
    return f"{hours}:{minutes}"

print(convert_to_military_time(1))