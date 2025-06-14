age = 16
cost = 12.5
name = "Calin Marcu"
is_valid = True

print("Age is " , age)
print("Age is " +str(age))
print(f"Age is {age}")

mesaj = "Salut , " + name + " cu varsta de " + str(age) 
print(mesaj)

complex_message = f"""
Age is {age}
Cost is {cost} and name is {name}
Is User Valid {is_valid}
"""

print(complex_message)
