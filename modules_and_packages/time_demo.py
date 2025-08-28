import time

print("Current Time: ", time.ctime())

print("Countdown starting...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("Blast Off!")
