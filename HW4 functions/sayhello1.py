def sayhello(name, hour):
    if hour >= 0 and hour <= 6:
        time = 'night'
    elif hour >= 7 and hour <= 11:
        time = 'morning'
    elif hour >= 12 and hour <= 17:
        time = 'day'
    elif hour >= 18 and hour <= 23:
        time = 'evening'
    return f"Good {time}, {name}"


print(sayhello( "John", 13 ))
