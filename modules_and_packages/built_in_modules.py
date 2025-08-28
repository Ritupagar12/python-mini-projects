import math, random, datetime, statistics, itertools, secrets, os, pathlib

nums = [3, 5, 9, 12]

print("sqrt(9) = ", math.sqrt(9))
print("randint 1-6 = ", random.randint(1, 6))
print("today = ", datetime.date.today())
print("mean = ", statistics.mean(nums))
print("pairs from nums = ", list(itertools.combinations(nums, 2)))
print("secure token = ", secrets.token_hex(8))
print("cwd exists? ", pathlib.Path(os.getcwd()).exists())

# math module
print(math.e)
print(math.radians(90))
print(math.degrees(math.pi/2))
print(math.sin(math.radians(90)))
print(math.cos(math.radians(0)))
print(math.tan(math.radians(45)))
print(math.log(10))
print(math.log10(100))
print(math.exp(2))
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.ceil(4.2))
print(math.floor(4.8))

# random module
print(random.random())              # float 0-1
print(random.randint(1,10))         # integer 1-10
print(random.randrange(1, 10, 2))   # step value
print(random.choice([1, 2, 3]))     # choose one
print(random.shuffle([1, 2, 3])     # shuffle list

# os module

## os.mkdir("folder")  # create directory
## os.chdir("folder")  # change directory
## os.getcwd()         # current working directory
## os.rmdir("folder")  # remove directory
## os.listdir()        # list files/folders

