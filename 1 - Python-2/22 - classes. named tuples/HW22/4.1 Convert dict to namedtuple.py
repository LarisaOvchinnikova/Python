from collections import namedtuple

def convert(obj):
    Workout = namedtuple("Workout", ["day", "routine", "timing"])
    return Workout(*obj.values())

workout_dct = {
    'day': "Monday",
    'routine': 'Chest+biceps',
    'timing': 55}

print(convert(workout_dct))

