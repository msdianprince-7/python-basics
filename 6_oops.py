# ==========================================
#        OBJECT ORIENTED PROGRAMMING (OOP)
# ==========================================


# ---------- BASIC CLASS & OBJECT ----------

# class Student:
#     subject = "Python"
#     college = "ABC"

# student1 = Student()
# print(student1.college)


# ---------- NOTES ----------
# __init__ is a constructor (inbuilt in class)
# When we create an object → constructor gets called automatically
# self → refers to current object / instance


# ---------- CONSTRUCTOR EXAMPLE ----------

class StudentBasic:
    def __init__(self):
        print("Constructor was called")


stu1 = StudentBasic()


# ---------- TYPES OF CONSTRUCTOR ----------
# Default Constructor → only has 'self'
# Parameterized Constructor → has parameters other than 'self'
# Python allows only one constructor (__init__)


# ---------- ATTRIBUTES ----------
# 2 types:
# 1. Class Attributes → common for all objects
# 2. Instance Attributes → different for each object
# If same name exists → instance attribute gets higher priority


class StudentDetail:
    college_name = "ABC College"   # class attribute
    PI = 3.1

    def __init__(self, name, cgpa):
        self.name = name           # instance attribute
        self.cgpa = cgpa
        self.PI = 3.14             # overrides class attribute


stu2 = StudentDetail("Priyansh", 10)

print("\n--- Attributes ---")
print(StudentDetail.college_name)
print(stu2.college_name)
print(stu2.cgpa)
print(stu2.PI)


# ---------- METHODS ----------
# 3 types:
# 1. Instance Method → uses 'self'
#    → can access instance + class attributes
#
# 2. Class Method → uses 'cls'
#    → can access only class attributes
#    → defined using @classmethod
#
# 3. Static Method → no self / cls required
#    → cannot access class or instance attributes
#    → defined using @staticmethod


class Laptop:
    storage_type = "SSD"   # class attribute

    def __init__(self, RAM, storage):
        self.RAM = RAM      # instance attribute
        self.storage = storage

    # Class Method
    @classmethod
    def get_storage_type(cls):
        print(f"Storage type is {cls.storage_type}")

    # Instance Method
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    # Static Method
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Discounted price = {final_price}")


# ---------- OBJECTS ----------

l1 = Laptop("16GB", "512GB")
l2 = Laptop("8GB", "256GB")


# ---------- METHOD CALLS ----------

print("\n--- Laptop Info ---")
l1.get_info()
l2.get_info()

print("\n--- Class Method ---")
Laptop.get_storage_type()

print("\n--- Static Method ---")
l1.calc_discount(40000, 10)   # 40_000 = 40000


# ==========================================
#            END OF PROGRAM
# ==========================================