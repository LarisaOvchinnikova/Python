def get_military(time):
    # time = "12:30 AM"
    time = time.split()  # ["12:30", "AM"]

    ampm = time[1]  # "AM"

    splited_time = time[0].split(":")  # ["12", "30"]

    hours = splited_time[0]  # "12"
    minutes = splited_time[1]  # "30"

    time = time[0]  # "12:30"

    if ampm.lower() == "am":
        if hours == '12':  # "11:00 am"
            return f"00:{minutes}"
        else:
            return f"{time}"

    if ampm.lower() == "pm":
        if hours == "12":
            return f"{time}"  # "01:40 PM" == "13:40"
        else:
            return f"{int(hours) + 12}:{minutes}"


# print(get_military("12:30 AM"))
