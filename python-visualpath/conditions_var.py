'''
This script will implement the knowledge on
condition and different datatypes.
'''
print("This IT Organization has various skill sets.")
print("Find out match.")

print("Enter Capitalised Values: ")

DevOps = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
Development = ("java", "NodeJS", ".net" "AngularJS", "Python")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":"1024"}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code":"1218"}

usr_skill = input("Enter your desired skill:")
#print(user_skill)

#Check in the database if we have this skill
if usr_skill in DevOps:
    print(f"we have {usr_skill} in DevOps Team.")
elif (usr_skill in Development):
    print(f"we have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print (f"We have contract employees with {usr_skill} skill.")
else:
    print("Skill is not available")
    print("Please check if you have entered value in capatalize or check the spelling.")