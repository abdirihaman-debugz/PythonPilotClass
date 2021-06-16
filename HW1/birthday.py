# importing date class from datetime module
from datetime import date
# creating the date object of today's date
todaysDate = date.today()
# gets the current year 
currentYear = todaysDate.year
#once you run the code you as the user should enter your birth year.
birthYear = input("Enter your birth year: ")

age = currentYear - birthYear

print (age)