import csv
from collections import namedtuple
# https://github.com/fivethirtyeight  файлы csv на разные темы
def parse_row(row):
    for key, value in row.items():
        if value.isdigit():
            row[key] = int(value)
        else:
            try:
                row[key] = float(value)
            except ValueError:
                continue

    return Record(**row)

data = []

with open("KIND.csv") as file:
    reader = csv.DictReader(file)
    Record = namedtuple("Record", reader.fieldnames)

    for line in reader:
        #print(line)
        new_record = parse_row(line)
        data.append(new_record)

#print(data[0])
def hot_days():
    return sorted(data, key=lambda row: row.actual_max_temp, reverse=True)

def cold_days():
    return sorted(data, key=lambda row: row.actual_min_temp)

def wet_days():
    return sorted(data, key=lambda row: row.actual_precipitation, reverse=True)

print(hot_days()[:4])

print(cold_days()[:4])

print(wet_days()[:4])