# ===============================
# 🔥 LIST COMPREHENSION EXAMPLES
# ===============================

# 1. Traditional way (for loop)
squares = []
for i in range(6):
    squares.append(i * i)

print("Using loop:", squares)


# 2. List comprehension (short & Pythonic)
sq = [i * i for i in range(6)]
print("Using list comprehension:", sq)


# ===============================
# 🔥 WITH CONDITION (FILTER)
# ===============================

# Only odd numbers' squares
sq = [i * i for i in range(6) if i % 2 != 0]
print("Odd squares:", sq)


# ===============================
# 🔥 CONDITIONAL EXPRESSION
# ===============================

nums = [-2, -3, 3, 4, -1, 7]

# Replace negative numbers with 0
nums = [0 if val < 0 else val for val in nums]
print("Replace negatives:", nums)


# ===============================
# 🧠 NOTES (IMPORTANT)
# ===============================

"""
1. Basic syntax:
   [expression for item in iterable]

2. With condition (filter):
   [expression for item in iterable if condition]

3. With if-else (value change):
   [value_if_true if condition else value_if_false for item in iterable]

4. Difference:
   - if at end → FILTERS elements
   - if-else in middle → TRANSFORMS elements

5. Why use it?
   - Shorter code
   - More readable
   - Faster than normal loop (in most cases)
"""