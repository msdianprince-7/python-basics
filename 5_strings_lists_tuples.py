# ==========================================
#         STRINGS AND LISTS IN PYTHON
# ==========================================


# ---------- STRINGS ----------

print("\n--- String Examples ---")

first_name = "priyansh"
last_name = "nandwana"

# Length of string
print("Length of last name:", len(last_name))

# String concatenation
print("Full Name:", first_name + " " + last_name)

# Accessing characters
print("First character:", first_name[0])

# Loop through string
print("\nCharacters in first name:")

for i in range(len(first_name)):
    print(first_name[i])

# String slicing
print("\n--- String Slicing ---")

print(first_name[0:5])     # start index to end index (end not included)
print(first_name[3:])      # from index 3 till end
print(first_name[:5])      # from start till index 5
print(first_name[-4:-1])   # negative indexing


# ---------- STRING FORMATTING ----------

print("\n--- String Formatting ---")

number = 10

print("The number is {}".format(number))

a = 10
b = 20

total = a + b

# Format-based formatting
print("The sum of {}, {} is {}".format(a, b, total))

# Index-based formatting
print("The sum of {1}, {0} is {2}".format(a, b, total))

# Named formatting
print("The value of {a} and {b}".format(a=10, b=20))

# f-string formatting
x = 5
y = 10

print(f"The sum of {x} and {y} is {x + y}")


# ---------- LISTS ----------

print("\n--- List Examples ---")

# Lists are mutable
marks = [88, 89, 100, 20]

print("Original List:", marks)

# Append element
marks.append(123)

# Insert element
marks.insert(1, 122)

print("Updated List:", marks)

# Sort list
marks.sort()

print("Sorted List:", marks)

# Reverse list
marks.reverse()

print("Reversed List:", marks)


# ---------- LOOP THROUGH LIST ----------

print("\nElements in List:")

for value in marks:
    print(value)


# ---------- FIND INDEX OF ELEMENT ----------

print("\n--- Find Index of 100 ---")

index = 0

for value in marks:
    if value == 100:
        print("Index of 100 is:", index)
        break

    index += 1


# ==========================================
#            END OF PROGRAM
# ==========================================