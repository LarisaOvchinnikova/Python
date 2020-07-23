from collections import namedtuple

Workout = namedtuple("Workout", ["day", "routine", "timing"])
one_workout = Workout('Monday', 'Chest+biceps', 45)
print(f"On {one_workout[0]} I train {one_workout[1]} during {one_workout[2]} minutes")
print(f"On {one_workout.day} I train {one_workout.routine} during {one_workout.timing} minutes")


workouts = [('Monday', 'Chest+biceps', '45'),
            ('Tuesday', 'Back+triceps', '45'),
            ('Wednesday', 'Core', '30'),
            ('Thursday', 'Legs', '55'),
            ('Friday', 'Shoulders', '45'),
            ('Saturday', 'Rest', '0'),
            ('Sunday', 'Rest', '0')]

all_workouts = [Workout(*el) for el in workouts]
print(all_workouts)
