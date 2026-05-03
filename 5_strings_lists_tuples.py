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
#      TUPLES, DICTIONARIES AND SETS
# ==========================================


# ---------- TUPLES ----------

print("\n--- Tuples in Python ---")

# Tuples are immutable
# Created using ()

tuple_data = (1, 2, 3, 4, "abc", 4, 4, 4)

print("Tuple:", tuple_data)

print("Length of tuple:", len(tuple_data))

print("Element at index 2:", tuple_data[2])

print("Index of value 1:", tuple_data.index(1))

print("Count of 4:", tuple_data.count(4))


# Single value tuple
single_tuple = (1,)

print("Single Value Tuple:", single_tuple)


# ---------- DICTIONARIES ----------

print("\n--- Dictionaries in Python ---")

# Dictionaries are unordered key-value pairs

info = {
    "name": "priyansh",
    "class": 8,
    "subjects": ["maths", "science"],
    3.14: "PI"
}

print("Dictionary:", info)

# Access value using key
print("Name:", info["name"])

# Get all keys
print("Keys:", info.keys())

# Convert keys to list
print("Keys as List:", list(info.keys()))

# Get all values
print("Values:", info.values())

# Get key-value pairs
print("Items:", info.items())

# Safe access using get()
print("Get Name:", info.get("name"))

# Update dictionary
info.update({
    "city": "udaipur"
})

print("Updated Dictionary:", info)


# ---------- SETS ----------

print("\n--- Sets in Python ---")

# Sets:
# - Do not allow duplicate values
# - Are unordered
# - Elements should be immutable

numbers = {1, 1, 2, 2, 33, 3, 3}

print("Set:", numbers)

print("Length of set:", len(numbers))

print("Type:", type(numbers))

# Empty set
empty_set = set()

print("Empty Set:", empty_set)

# Add element
numbers.add(5)

print("After Adding 5:", numbers)

# Remove element
numbers.remove(5)

print("After Removing 5:", numbers)

# Remove random element
numbers.pop()

print("After Pop:", numbers)


# ---------- UNION AND INTERSECTION ----------

print("\n--- Union and Intersection ---")

set_a = {1, 2, 3, 33}
set_b = {5, 6, 7, 8, 33}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a.union(set_b))

print("Intersection:", set_a.intersection(set_b))


# ---------- PRACTICE PROBLEM ----------

print("\n--- Student Course Data ---")

student_info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

courses_set = set()

for name, course in student_info:
    print(name, "-", course)

    courses_set.add(course)

print("\nUnique Courses:")

for course in courses_set:
    print(course)


# ==========================================
#            END OF PROGRAM
# ==========================================