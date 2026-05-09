# ==========================================
#        OOP CONCEPTS – REVISION NOTES
# ==========================================


# ==========================================================
# 🔒 ENCAPSULATION
# ==========================================================
# Definition:
# Encapsulation means wrapping data (variables) and methods
# (functions) together into a single unit (class).
#
# It also enables DATA HIDING.
#
# Access Modifiers in Python:
# 1. Public      → self.name       (accessible everywhere)
# 2. Protected   → self._balance   (accessible but discouraged outside class)
# 3. Private     → self.__balance  (name mangling, not directly accessible)
#
# Private variables can be accessed using:
# _ClassName__variableName


class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # Public
        self.__balance = balance  # Private (data hiding)

    # Getter → used to read private data
    def get_balance(self):
        return self.__balance

    # Setter → used to modify private data
    def set_balance(self, new_balance):
        self.__balance = new_balance


print("\n--- Encapsulation ---")

acc1 = BankAccount("Rahul Kumar", 100_000)

acc1.set_balance(200_000)

# Access using name mangling (not recommended in real projects)
print(acc1.name, acc1._BankAccount__balance)


# ==========================================================
# 🧬 INHERITANCE
# ==========================================================
# Definition:
# Inheritance allows a class (child) to reuse properties
# and methods of another class (parent).
#
# Types:
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance


# ---------- SINGLE INHERITANCE ----------

class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time


class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role


print("\n--- Single Inheritance ---")

t1 = Teacher("Math")
t1.change_time("5pm")

print(t1.subject, t1.start_time, t1.end_time)

staff1 = AdminStaff("Manager")

print(staff1.role, staff1.start_time, staff1.end_time)


# ---------- MULTILEVEL INHERITANCE ----------

class Employee:
    start_time = "10am"
    end_time = "6pm"


class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role


class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary


print("\n--- Multilevel Inheritance ---")

acc2 = Accountant(25000, "CA")

print(acc2.role, acc2.salary, acc2.start_time, acc2.end_time)


# ---------- MULTIPLE INHERITANCE ----------

class TeacherBase:
    def __init__(self, salary):
        self.salary = salary


class StudentBase:
    def __init__(self, gpa):
        self.gpa = gpa


class TA(TeacherBase, StudentBase):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)        # calls TeacherBase
        StudentBase.__init__(self, gpa) # manually call second parent
        self.name = name


print("\n--- Multiple Inheritance ---")

ta1 = TA(15000, 9.3, "Shradha")

print(ta1.name, ta1.gpa, ta1.salary)


# ==========================================================
# 🎭 ABSTRACTION
# ==========================================================
# Definition:
# Abstraction means hiding implementation details and showing
# only essential features.
#
# Achieved using:
# - Abstract classes
# - Abstract methods
#
# Abstract class cannot be instantiated directly.


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("Roar!")


class Cow(Animal):
    def make_sound(self):
        print("Moo!")


print("\n--- Abstraction ---")

lion = Lion()
lion.make_sound()


# ==========================================================
# 🔁 POLYMORPHISM
# ==========================================================
# Definition:
# Polymorphism means "many forms".
#
# Same method name behaves differently depending on object.
#
# Types:
# 1. Method Overriding (Runtime Polymorphism)
# 2. Duck Typing


# ---------- METHOD OVERRIDING ----------

class Employee:
    def get_designation(self):
        print("Designation = Employee")


class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")


print("\n--- Method Overriding ---")

t1 = Teacher()
t1.get_designation()


# ---------- DUCK TYPING ----------
# "If it walks like a duck and quacks like a duck, it’s a duck"
# Python doesn’t care about class type, only behavior matters


class Teacher:
    def get_designation(self):
        print("Designation = Teacher")


class Accountant:
    def get_designation(self):
        print("Designation = Accountant")


print("\n--- Duck Typing ---")

t1 = Teacher()
t1.get_designation()

acc3 = Accountant()
acc3.get_designation()


# ==========================================
#            END OF PROGRAM
# ==========================================