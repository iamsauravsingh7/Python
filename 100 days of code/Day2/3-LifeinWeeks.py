age = input("What is your current age? ")
age_as_int = int(age)
life = 90 - age_as_int
days = life * 365
weeks = life * 52
months =  life * 12
message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)