def add_time(start, duration, day=None):
    # Create a dictionary to store all the days of the week
    days_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

    # Do a check to see if day is set
    # If set you want to iterate in the dict and find the matching key
    matching_key = None
    if day is not None:
        day = day.lower().capitalize()
        for k, v in days_dict.items():
            if day == v:
                matching_key = k

    # Need to split extract as it comes in the following format "Xx:YY ZZ"
    # Xx representing hours, YY minutes and ZZ the meridiem.
    start_time = start.split()
    start_hour = int(start_time[0].split(":")[0])
    start_minutes = int(start_time[0].split(":")[1])
    start_meridien = start_time[1].upper() # just in case there are upper & lower test cases

    # Convert the start time to 24-hour format
    start_hour_24hr_format = start_hour

    if start_meridien == "AM" and start_hour == 12:
        start_hour_24hr_format = 0
    elif start_meridien == "AM":
        start_hour_24hr_format = start_hour
    elif start_meridien == "PM" and start_hour != 12:
        start_hour_24hr_format += 12
    elif start_meridien == "PM" and start_hour == 12:
        start_hour_24hr_format = 12

    # Need to split the duration time, it comes in the following format
    # XX:YY where XX represent the hours to be added or an arbitrary int 0+
    # and YY is the minutes to be added
    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    # Add the start_hour in 24hr format number and duration hour together
    new_hours = start_hour_24hr_format + duration_hour
    new_minutes = start_minutes + duration_minutes

    # Do a check to see if we have more minutes than an hour, if we do
    # add an hour to the general clock and subtract the minutes to represent the clock accurately
    if new_minutes > 60:
        new_hours = new_hours + 1
        new_minutes = new_minutes - 60

    # Need to convert the new_hours and new_minutes to days, hrs, minutes format
    added_days = new_hours // 24
    added_hours = new_hours % 24
    added_minutes = new_minutes % 60

    # Need to fix the meridien
    if added_hours < 12:
        new_meridien = "AM"
    else:
        new_meridien = "PM"

    # Need to convert the time back into 12-hour format
    hours = added_hours % 12
    if hours == 0:
        hours = 12

    # Need to get the day it is if it was set and how many days it would have been since
    # But how
    if matching_key is not None:
        amount_of_days = added_days % 7
        diff_days = matching_key + amount_of_days
        diff_days = diff_days % 7
        which_day = days_dict.get(diff_days)

    # return the result to see if we're doing the right thing
    if day is None and added_days == 0:
        return f"{hours}:{new_minutes:02d} {new_meridien}"
    elif day is not None and added_days == 0:
        return f"{hours}:{new_minutes:02d} {new_meridien}, {days_dict.get(matching_key)}"
    elif day is None and added_days == 1:
        return f"{hours}:{new_minutes:02d} {new_meridien} (next day)"
    elif day is not None and added_days == 1:
        return f"{hours}:{new_minutes:02d} {new_meridien}, {which_day} (next day)"
    elif day is None and added_days >= 2:
        return f"{hours}:{new_minutes:02d} {new_meridien} ({added_days} days later)"
    elif day is not None and added_days >= 2:
        return f"{hours}:{new_minutes:02d} {new_meridien}, {which_day} ({added_days} days later)"
    elif day is None and (start_meridien == "PM" and new_meridien == "AM") and added_days == 0:
        return f"{hours}:{new_minutes:02d} {new_meridien} (next day)"


# print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02"))
print(add_time("8:16 PM", "466:02", "Tuesday"))
# print(add_time("9:15 PM", "5:30"))
# print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
# # print(add_time("2:59 AM", "24:00"))
# print(add_time("11:55 AM", "3:12"))
# print(add_time("9:15 PM", "5:30"))
# print(add_time("3:30 PM", "2:12"))
# print(add_time("9:15 PM", "5:30"))