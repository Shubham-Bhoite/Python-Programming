# time.time():
import time
print(time.time())


# time.sleep():
import time
print("Start:", time.time())
time.sleep(4)
print("End:", time.time())

# time.strftime():
import time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
