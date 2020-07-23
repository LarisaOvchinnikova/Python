from collections import namedtuple

Workout = namedtuple("Workout", ["day", "routine", "timing"])


workouts = [('Monday', 'Chest+biceps', '45'),
            ('Tuesday', 'Back+triceps', '45'),
            ('Wednesday', 'Core', '30'),
            ('Thursday', 'Legs', '55'),
            ('Friday', 'Shoulders', '45'),
            ('Saturday', 'Rest', '0'),
            ('Sunday', 'Rest', '0')]

all_workouts = [Workout(*el) for el in workouts]
print(all_workouts)
