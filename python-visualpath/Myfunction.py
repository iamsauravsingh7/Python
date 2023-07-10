#defining function
"""
def add(argument1, argument2):
    total = (argument1) + (argument2)
    return total

#calling function
out = add(2,3)
print(out)
print(add(10,30))
def adder(argument1, argument2):
    total = (argument1) + (argument2)
    print(total)

#adder(10,50)
print(adder(10,50))

def summ(arg):
    x = 0 
    for i in arg:
        x = x + i
    return x
out = summ([1,2,3])
print(out)

# Default arguments
def greetings(msg="Morning"):
    print(f"Good{msg}")
    print("Welcome ot the function")

greetings()
greetings("Evening")"""

# Keywords Arguments 
def vac_feedback(vac,efficacy):
    print(f"{vac} vacation is having {efficacy} % efficacy.")
    if (efficacy >50) and (efficacy <=75):
        print("Seems not so effective, Needs more trial.")
    elif (efficacy >75) and (efficacy <90):
        print("can consider this vaccine.")
    elif efficacy >=90:
        print("Sure enough to take the shot")
    else:
        print("Needs many more trials")

vac_feedback("Prizer", 95)
vac_feedback("Unkonwn", 45)
vac_feedback(efficacy=34, vac="Unkonwn") # if you know the name of the argument then order is not important


