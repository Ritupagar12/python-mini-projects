import datetime

#ask user for thir name
name = input("What is your name?  ")

#get today's date
today = datetime.date.today()  

#greet the user
print(f"Hello, {name}! Today is {today}. Have a great day!")

#datetime.datetime.now().time() #To add current time
