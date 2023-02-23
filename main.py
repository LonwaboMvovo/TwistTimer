import time

input("start:")
start_time = time.time()

input("finish:")
end_time = time.time()

time_passed = round(end_time - start_time, 2)
print(time_passed)
