from datetime import datetime
f = open("messages.txt")
loglines = f.readlines()
#print(loglines)
f.close()


def convert_to_datetime(line):
    timestamp = line.split()[1]
    print(timestamp)
    date_str = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(timestamp, date_str)

def time_between_shutdowns(loglines):
    shutdown_entries = [line for line in loglines if "Shutdown initiated" in line]
    print(shutdown_entries)
    # shutdown_times = shutdown_entries[0]
    # print(shutdown_times)
    # print(convert_to_datetime(shutdown_times))
    shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
    print(shutdown_times)
    return max(shutdown_times) - min(shutdown_times)


print(time_between_shutdowns(loglines))