from collections import namedtuple
all_workouts = []
days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders Rest Rest'.split()
timings = '45 45 30 55 45 0 0'.split()

Workout = namedtuple("Workout", ["day","routine","timing"])

for trio in zip(days, routines, timings):
    all_workouts.append(trio)

print(all_workouts)
workouts = [Workout(*el) for el in all_workouts]
print(workouts)