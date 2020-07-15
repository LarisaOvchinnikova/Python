from datetime import datetime

f = open("messages.txt")
log_lines = f.readlines()
print(log_lines)
f.close()

def convert_to_datetime(string):
    time = string.split()[1]
    #print(time)
    return datetime.strptime(time, '%Y-%m-%dT%H:%M:%S')

def time_between_shutdowns(log_lines):
    shutdown_lst = [line for line in log_lines if "Shutdown initiated" in line]
    print(shutdown_lst)

    shutdown_times = [convert_to_datetime(string) for string in shutdown_lst]
    print(shutdown_times)
    return max(shutdown_times) - min(shutdown_times)


print(time_between_shutdowns(log_lines))