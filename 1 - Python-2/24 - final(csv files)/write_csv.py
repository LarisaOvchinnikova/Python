import csv
with open("babynamesranking2006.txt") as file:
    data = file.readlines()

    with open("parsed_names.csv", "w") as csvfile:
        fields = "rank,boy_name,boy_number,girl_name,girl_number".split(",")
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for line in data:
            print(line)
            line = line.split()
            print(line)
            # line[2] = "".join(line[2].split(","))
            # line[4] = "".join(line[4].split(","))
            writer.writerow(dict(zip(fields, line)))
