# ==========================================
#           FUNCTIONS IN PYTHON
# ==========================================


# ---------- SIMPLE FUNCTION ----------

print("\n--- Simple Function ---")


def hello():
    print("Hello")


hello()


# ---------- FUNCTION WITH RETURN VALUE ----------

print("\n--- Sum Function ---")


def add(a, b):
    return a + b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum is:", result)


# ---------- DEFAULT PARAMETERS ----------

print("\n--- Average Function ---")


def average(a, b, c=1):
    """
    c is a default parameter.
    If no value is passed, c will take value 1.
    """
    return (a + b + c) / 3


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

avg = average(a, b, c)

print("Average is:", avg)


# ---------- LAMBDA FUNCTION ----------

print("\n--- Lambda Function ---")

sum_lambda = lambda a, b, c: a + b + c

print("Lambda Sum:", sum_lambda(a, b, c))


# ---------- FACTORIAL FUNCTION ----------

print("\n--- Factorial Function ---")


def factorial(number):
    fact = 1

    for i in range(1, number + 1):
        fact = fact * i

    return fact


number = int(input("Enter a number: "))

print("Factorial is:", factorial(number))


# ==========================================
#            END OF PROGRAM
# ==========================================