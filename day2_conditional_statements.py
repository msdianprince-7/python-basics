# ==========================================
#       CONDITIONAL STATEMENTS IN PYTHON
# ==========================================


# ---------- SIMPLE IF ELSE ----------

print("\n--- Voting Eligibility Check ---")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ---------- IF ELIF ELSE ----------

print("\n--- Traffic Light System ---")

color = input("Enter traffic light color: ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else:
    print("Invalid color")


# ---------- AGE CATEGORY ----------

print("\n--- Age Category ---")

age = int(input("Enter your age: "))

if age <= 13:
    print("Child")
elif age <= 18:
    print("Young")
else:
    print("Adult")


# ---------- NESTED CONDITIONALS ----------

print("\n--- Login System ---")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "pass":
    print("Valid user")
else:
    if username != "admin":
        print("Invalid username")
    else:
        print("Invalid password")


# ---------- MATCH CASE ----------

print("\n--- Match Case Example ---")

signal = input("Enter signal color: ").lower()

match signal:
    case "green":
        print("Go")
    case "red":
        print("Stop")
    case "yellow":
        print("Look")
    case _:
        print("Default case")


# ==========================================
#            END OF PROGRAM
# ==========================================