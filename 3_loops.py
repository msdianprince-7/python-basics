# ==========================================
#             LOOPS IN PYTHON
# ==========================================


# ---------- WHILE LOOP ----------

print("\n--- While Loop Examples ---")

# Print "Hello" 5 times
i = 1

while i <= 5:
    print("Hello")
    i += 1


# Print numbers from 1 to 5
print("\nNumbers from 1 to 5:")

i = 1

while i <= 5:
    print(i)
    i += 1


# Print numbers from 5 to 1
print("\nNumbers from 5 to 1:")

i = 5

while i > 0:
    print(i)
    i -= 1


# Multiplication Table
print("\n--- Multiplication Table ---")

table = int(input("Enter the table number: "))

i = 1

while i <= 10:
    print(table, "*", i, "=", table * i)
    i += 1


# ---------- BREAK STATEMENT ----------

print("\n--- Break Statement ---")

i = 1

while i <= 10:
    if i % 6 == 0:
        break

    print(i)
    i += 1

print("Outside loop:", i)


# ---------- CONTINUE STATEMENT ----------

print("\n--- Continue Statement ---")

i = 1

while i <= 10:
    if i % 2 == 0:
        i += 1
        continue

    print(i)
    i += 1


# ---------- FOR LOOP ----------

print("\n--- For Loop with String ---")

text = "priyansh"

for character in text:
    print(character)


# ---------- MEMBERSHIP OPERATOR ----------

print("\n--- Membership Operator ---")

if "z" in text:
    print("z exists in string")
else:
    print("z does not exist in string")


# ---------- RANGE FUNCTION ----------

print("\n--- Range Function ---")

for i in range(10):
    print(i)


print("\nRange with Start and Stop:")

for i in range(0, 5):
    print(i + 1)


print("\nRange with Step Value:")

for i in range(0, 5, 1):
    print(i + 1)


# ---------- COUNT VOWELS ----------

print("\n--- Count Vowels ---")

word = "artificial intelligence"

count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)


# ---------- SUM OF N NATURAL NUMBERS ----------

print("\n--- Sum of N Natural Numbers ---")

n = int(input("Enter a number: "))

total = 0

for i in range(n):
    total += (i + 1)

print("Sum is:", total)


# ==========================================
#            END OF PROGRAM
# ==========================================