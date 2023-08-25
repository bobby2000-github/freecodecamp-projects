def add_time(start, duration, option=None):
#Get time and ending
    s_time, s_ending = start.split(" ")
    ending = s_ending
#Get hours and minutes of starting and duration time
    s_hour, s_minute = map(int, s_time.split(":"))
    d_hour, d_minute = map(int, duration.split(":"))
#Flip ending clock
    t_ending = {"AM": "PM", "PM" : "AM" }
#The minutes in the duration time will be a whole number less than 60
    if d_minute > 59:
        d_hour += 1
        d_minute -= 60
#Count days passed and got total minutes
    days_passed = (s_hour + d_hour + ((s_minute + d_minute) // 60)) // 24
#Count the minutes and Flip ending clock if hour equal eleven and endings in different stage
    minute = s_minute + d_minute
    if minute > 59 and s_hour == 11 and ending == "AM":
        minute -= 60
        s_hour += 1
        ending = t_ending[s_ending]

    if minute > 59 and s_hour == 11 and s_ending == "PM":
        minute -= 60
        s_hour += 1
        ending = t_ending[s_ending]
        days_passed += 1
#Count hours
    hour = (s_hour + d_hour) % 24
#check if it was zero we turn it to 12
    if hour == 0:
        hour = 12
#Check the ending stage
    if hour > 12 and s_ending == "AM":
        ending = t_ending[s_ending]
        hour -= 12

    if hour > 12 and s_ending == "PM":
        ending = t_ending[s_ending]
        hour -= 12
        days_passed += 1

#Set days of the week and check the option parameter whether in any stage
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    x = ""
    if option:
        day_index = (days_passed + days_of_week.index(option.capitalize())) % 7
        x = f", {days_of_week[day_index]}"
        if days_passed == 1:
            x = f"{x} (next day)"
            results = f"{hour}:{minute:02} {ending}"
            if x:
                results += f"{x}"
        elif days_passed > 1:
            x = f"{x} ({days_passed} days later)"
            results = f"{hour}:{minute:02} {ending}"
            if x:
                results += f"{x}"

    elif days_passed == 1:
        x = " (next day)"
    results = f"{hour}:{minute:02} {ending}"
    if x:
        results += f"{x}"
    elif days_passed > 1:
        x = f" ({days_passed} days later)"
    results = f"{hour}:{minute:02} {ending}"
    if x:
        results += f"{x}"
    
    return results
