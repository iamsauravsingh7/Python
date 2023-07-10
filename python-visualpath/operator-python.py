# Arthmetic Operators

x = 2
y = 5

total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = x / y
print(total)

total = x % y
print(total)

# Comparison Operators

a = 30
b = 60

out = a < b
print(out)

out = a > b
print(out)

out = a == b
print(out)

out = a != b
print(out)

out = a >= b
print(out)

out = a <= b
print(out)

# Assignment operators

c = 0
d = 1

c+= d # c = c+d
print(c)

c = 0
d = 1

c-= d # c = c-d
print(c)

# Logical Operators

#and (Both of the operant have to be true)
# or (Any one of the operant have to be true)

a = 40
b = 60

x = 2
y = 3

out = (a < b) or (x > y)
print(out)

out = (a < b) and (x < y)
print(out)

out = (a > b) and (x < y)
print(out)

out = not(a < b)
print(out)

# Membership Operator

first_tuple = ("IOT", "Devops", 47, 89, 1.4)

ans = "Devops" in first_tuple
print(ans)

ans = "ops" in "Devops"
print(ans)

ans = "Devops" not in first_tuple
print(ans)

ans = 67 in first_tuple
print(ans)

ans = 67 not in first_tuple
print(ans)

# Identity Operators

a = 12
b = 15
x = 34
y = 36

result = a is b
print(result)

report = x is not y
print(report)