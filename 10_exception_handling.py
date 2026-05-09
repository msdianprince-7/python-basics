# ===============================
# ⚠️ EXCEPTION HANDLING IN PYTHON
# ===============================

"""
try    → code that may cause error
except → handles specific errors
else   → runs only if NO error occurs
finally→ runs always (optional)
"""

try:
    x = int(input("enter x: "))   # may cause ValueError (if not a number)
    ans = 10 / x                  # may cause ZeroDivisionError (if x = 0)

# Specific exception: division by zero
except ZeroDivisionError:
    print("Divide by 0 is not allowed")

# Specific exception: invalid input (string instead of int)
except ValueError:
    print("Invalid input")

# Runs only if no exception occurs
else:
    print(f"ans = {ans}")

# Optional: always runs
finally:
    print("Execution completed")


# ===============================
# 🧠 IMPORTANT NOTES
# ===============================

"""
1. Always catch specific exceptions (best practice)
   ❌ bad: except:
   ✔️ good: except ValueError:

2. Order matters
   - Specific exceptions first
   - General exception last

3. else block
   - Runs only if try is successful

4. finally block
   - Always runs (used for cleanup like closing files)

5. Common exceptions:
   - ValueError → wrong type (e.g., "abc" → int)
   - ZeroDivisionError → divide by zero
   - FileNotFoundError → file missing
"""


# ===============================
# 🔥 BONUS (GENERIC EXCEPTION)
# ===============================

try:
    x = int(input("enter x: "))
    ans = 10 / x

except Exception as e:
    print("Error:", e)   # prints actual error message