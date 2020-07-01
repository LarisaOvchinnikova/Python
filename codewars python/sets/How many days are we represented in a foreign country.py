# https://www.codewars.com/kata/58e93b4706db4d24ee000096/train/python
def days_represented(trips):
    x = set()
    for trip in trips:
        for date in range(trip[0], trip[1]+1):
            x.add(date)
    return len(x)