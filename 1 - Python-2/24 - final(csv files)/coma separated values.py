import csv
from collections import namedtuple

data = []

with open("baby_names.csv") as names_file:
    reader = csv.DictReader(names_file)
    #print(reader.fieldnames)
    Record = namedtuple("Record", reader.fieldnames)
    print(reader.fieldnames)

    for line in reader:
        #print(line)
        for key, value in line.items():
            try:
                line[key] = int(value)
            except:
                continue

        row = Record(**line)
        data.append(row)

boy_alphabet = (sorted(data, key=lambda row: row.boy_name)[:5])
print(boy_alphabet)