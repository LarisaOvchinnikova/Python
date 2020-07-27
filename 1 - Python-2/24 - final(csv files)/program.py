import research

print("Weather research")

print("The hottest 5 days")
days = research.hot_days()
for i, day in enumerate(days[:5], start=1):
    print(f"{i}. {day.actual_max_temp} F on {day.date}")

print("The coldest 5 days")
days = research.hot_days()
for i, day in enumerate(days[:5], start=1):
    print(f"{i}. {day.actual_min_temp} F on {day.date}")

print("The wettest 5 days")
days = research.wet_days()
for i, day in enumerate(days[:5], start=1):
    print(f"{i}. {day.actual_precipitation} inch on {day.date}")