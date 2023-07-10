# Variable length arguments *args (Non keyword arguments)
'''
def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
#    print(args)
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 min: ")
    print("Enjoy the party")

order_food("Salad", "Pizza", "Paneer Masala", "soup")
'''
# Variable length arguments *kwargs (Keyword arguments)
import random
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