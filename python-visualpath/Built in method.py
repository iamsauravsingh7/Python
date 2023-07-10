# String Build in Method/function
'''
message = "corona vaccine is ready to use, most of them are more than 90% effective."
Message = message.capitalize()
#print(message.capitalize())
print(Message)

# dir() function

print(dir([]))
print(dir(()))
print(dir({}))
print(dir(""))

print(message.upper())
print(message.islower())
print(message.isupper())

print(message.find("ready"))
print(message[18:24])
print(message.find("not"))

seql= ("192","168", "40", "90")
print(".".join(seql))
print("-".join(seql))
print("/".join(seql))

mountain = ["Everest", "Himalaya", "Sahyadri", "Alps", "K2", "Mt Hood"]
print(mountain)

mountain.append("Oregon mount")
print(mountain)

mountain.extend(["Mt Rainer", "Satpuda"])
print(mountain)

mountain.insert(2, "Mt Abu")
print(mountain)

mountain.pop(5)
print(mountain)'''

cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":"1024"}
print(cntr_emp1.keys())
print(cntr_emp1.values())
print(cntr_emp1.clear())
