''' Write a python script to display the current date and time. First create variables to
   store date and time, then display date and time in proper format (like: 13-8-2022 and
   9:00 PM)'''
from datetime import datetime
today = datetime.today()
print("Current date and time :",today)
date = today.strftime("%d-%m-%Y and %I : %M %p")
print(date)
