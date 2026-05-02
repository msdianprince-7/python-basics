# ==========================================
#         PYTHON BASICS PRACTICE
# ==========================================

# ---------- PRINT STATEMENTS ----------

print("Hello World")
print("Hello\nWorld")
print("Learning Python 🚀")


# ---------- VARIABLES ----------

name = "Priyansh"
age = 18
pi = 3.14

print("\n--- Variables ---")
print("My name is:", name)
print("My age is:", age)

print("Data Types:")
print(type(name))
print(type(age))
print(type(pi))


# ---------- ARITHMETIC OPERATORS ----------

a = 4
b = 2

print("\n--- Arithmetic Operators ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulo:", a % b)
print("Power:", a ** b)


# ---------- RELATIONAL OPERATORS ----------

print("\n--- Relational Operators ---")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a >= b :", a >= b)


# ---------- ASSIGNMENT OPERATORS ----------

a += 5
b *= 5

print("\n--- Assignment Operators ---")
print("Updated value of a:", a)
print("Updated value of b:", b)


# ---------- LOGICAL OPERATORS ----------

value = False

print("\n--- Logical Operators ---")
print("NOT value:", not value)

print("\nAND Operator:")
print((5 > 3) and (5 > 1))
print((5 < 3) and (5 > 1))
print((5 < 3) and (5 < 1))

print("\nOR Operator:")
print((5 > 3) or (5 > 1))
print((5 < 3) or (5 > 1))
print((5 < 3) or (5 < 1))


# ---------- TYPE CASTING ----------

num1 = 15
num2 = 10.5

total = num1 + num2

print("\n--- Type Casting ---")
print("Total:", total)
print("Type of total:", type(total))

new_total = int(total)

print("Converted Total:", new_total)
print("Type after conversion:", type(new_total))

num = "123"

print("String to Integer:", int(num))
print("String to Boolean:", bool(num))


# ---------- USER INPUT ----------

print("\n--- User Input ---")

user_name = input("Enter your name: ")

print("Welcome,", user_name)

first_number = int(input("Enter value of a: "))
second_number = int(input("Enter value of b: "))

average = (first_number + second_number) / 2

print("Average is:", average)


# ==========================================
#              END OF PROGRAM
# ==========================================