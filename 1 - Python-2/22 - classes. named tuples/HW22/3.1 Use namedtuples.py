from collections import namedtuple

Workout = namedtuple("Workout", ["day", "routine", "timing"])
one_workout = Workout('Monday', 'Chest+biceps', 45)
print(f"On {one_workout[0]} I train {one_workout[1]} during {one_workout[2]} minutes")
print(f"On {one_workout.day} I train {one_workout.routine} during {one_workout.timing} minutes")



