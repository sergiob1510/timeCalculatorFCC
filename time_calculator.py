def add_time(start, duration, day="Osvaldo"):

    #Empty lists for later use
    starting_time = list()
    starting_clock = list()
    starting_period = list()
    added_time = list()
    days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    #Handling time
    starting_time = start.split()
    starting_clock = starting_time[0].split(":")
    starting_period = starting_time[1]
    added_time = duration.split(":")

    #Working with minutes
    minutes_added = int(starting_clock[1]) + int(added_time[1])
    if minutes_added >= 60 :
        result_minutes = int(minutes_added % 60)
        minutes_to_hours = int(minutes_added / 60)
    else:
        result_minutes = minutes_added
        minutes_to_hours = 0

    #Working with hours
    hours_added = int(starting_clock[0]) + int(added_time[0]) + minutes_to_hours
    if hours_added >= 12 :
        result_hours = int(hours_added % 12)
        hours_to_periods = int(hours_added / 12)
    else:
        result_hours = hours_added
        hours_to_periods = 0

    #Now the period
    if starting_period == "AM":
        period = 0
    else:
        period = 1

    final_period = period + hours_to_periods
    if final_period % 2 == 0:
        indicator_of_period = "AM"
    else:
        indicator_of_period = "PM"

    if hours_added > 12 and hours_added < 24:
        if starting_period == "AM":
            indicator_of_period = "PM"
        else:
            indicator_of_period = "AM"


    #Working with days...
    days = int(final_period / 2)
    if days < 1:
        day_message = day
    elif days >= 1 and days < 2:
        day_message = "(next day)"
    else:
        day_message = "(" + str(days) + " days later)"

    #Returning data
    if result_minutes < 10:
        result_minutes = "0" + str(result_minutes)
    if result_hours == 0:
        result_hours = 12
    day = day.capitalize()
    if days < 1 and day not in days_of_the_week:
        returning_data = str(result_hours) + ":" + str(result_minutes) + " " + str(indicator_of_period)
    elif days < 1 and day in days_of_the_week:
        returning_data = str(result_hours) + ":" + str(result_minutes) + " " + str(indicator_of_period) + ", " + day_message
    elif day not in days_of_the_week:
        returning_data = str(result_hours) + ":" + str(result_minutes) + " " + str(indicator_of_period) + " " + day_message
    else:
         if day in days_of_the_week:
            if day == "Monday" and days <= 6:
                day = days - 1
                day = days_of_the_week[day]
            elif day == "Monday" and days > 6:
                day = (days % 7) - 1
                day= days_of_the_week[day]
            elif day == "Tuesday" and days <= 5:
                day = days
                day = days_of_the_week[day]
            elif day == "Tuesday" and days > 5:
                day = (days % 7)
                if day == 6:
                  day =  day % 6
                day = days_of_the_week[day]
            elif day == "Wednesday" and days <= 4:
                day = 2 + days
                day = days_of_the_week[day]
            elif day == "Wednesday" and days > 4:
                day = (days % 7) + 2
                if day == 5:
                  day = day % 5
                day = days_of_the_week[day]
            elif day == "Thursday" and days <= 3:
                day= 3 + days
                day = days_of_the_week[day]
            elif day == "Thursday" and days > 3:
                day = (days % 7) + 3
                if day == 4:
                  day = day % 4
                day = days_of_the_week[day]
            elif day == "Friday" and days <= 2:
                day = 4 + days
                day = days_of_the_week[day]
            elif day == "Friday" and days > 2:
                day = (days % 7) + 4
                if day == 3:
                  day = day % 3
                day = days_of_the_week[day]
            elif day == "Saturday" and days <= 1:
                day = 5 + days
                day = days_of_the_week[day]
            elif day == "Saturday" and days > 1:
                day = (days % 7) + 5
                if day == 2:
                  day = day % 2
                day = days_of_the_week[day]


            returning_data = str(result_hours) + ":" + str(result_minutes) + " " + str(indicator_of_period) + ", " + str(day) + " " + str(day_message)

    return (returning_data)