import random

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
vac_feedback(efficacy=34, vac="Unkonwn")

def time_activity(*args, **kwargs):
    '''
    Input: Multiple values for minutes, key=value pair activity
    output: Return sum of minutes + randon minute spect on a random activity
    '''
#    print(args, kwargs)
    min = sum(args) + random.randint(0, 60)
#    print(min)
    choice = random.choice(list(kwargs.keys()))
#    print(choice)
    print(f"You have to spend {min} Minutes for {kwargs[choice]}")

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
#    print(args)
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 min: ")
    print("Enjoy the party")

order_food("Salad", "Pizza", "Paneer Masala", "soup")

def time_activity(*args, **kwargs):
    '''
    Input: Multiple values for minutes, key=value pair activity
    output: Return sum of minutes + randon minute spect on a random activity
    '''
#    print(args, kwargs)
    min = sum(args) + random.randint(0, 60)
#    print(min)
    choice = random.choice(list(kwargs.keys()))
#    print(choice)
    print(f"You have to spend {min} Minutes for {kwargs[choice]}")

time_activity(10,20,10, hobby="Dance", sport="Boxing", fun="Driving", work="Devops")