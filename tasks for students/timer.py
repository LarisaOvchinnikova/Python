import time
start = time.time()
for i in range(10):
    time.sleep(1)
    print(i)
end = time.time() - start
print("Time spent", round(end, 3))