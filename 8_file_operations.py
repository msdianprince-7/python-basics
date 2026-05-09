# ===============================
# 📂 PYTHON FILE HANDLING (FULL)
# ===============================

"""
MODES:
r  → read only (error if file doesn’t exist)
w  → write (deletes old data, creates if not exists)
a  → append (adds at end, creates if not exists)
x  → create new file (error if already exists)

b  → binary mode (images, pdf, etc.)
t  → text mode (default)

+  → read + write both
"""

# ===============================
# 🔥 BASIC MODES
# ===============================

# 1. READ MODE (r)
# - File must exist
# - Only reading allowed
with open("file.txt", "r") as f:
    data = f.read()
    print("READ MODE:\n", data)


# 2. WRITE MODE (w)
# - Deletes old content
# - Creates file if not exists
with open("file.txt", "w") as f:
    f.write("Hello Priyansh\n")
    f.write("This overwrites old data\n")


# 3. APPEND MODE (a)
# - Adds content at end
# - Does NOT delete old data
with open("file.txt", "a") as f:
    f.write("Appending new line\n")


# 4. CREATE MODE (x)
# - Creates new file
# - Error if file already exists
try:
    with open("newfile.txt", "x") as f:
        f.write("This file is newly created\n")
except FileExistsError:
    print("File already exists")


# ===============================
# 🔥 COMBINATION MODES
# ===============================

# 5. READ + WRITE (r+)
# - File must exist
# - Does NOT delete data
with open("file.txt", "r+") as f:
    print("R+ READ:\n", f.read())
    f.write("Added using r+\n")


# 6. WRITE + READ (w+)
# - Deletes old data
# - Need seek(0) to read after writing
with open("file.txt", "w+") as f:
    f.write("Fresh content\n")
    f.seek(0)
    print("W+ READ:\n", f.read())


# 7. APPEND + READ (a+)
# - Writes at end only
# - Need seek(0) to read
with open("file.txt", "a+") as f:
    f.write("Appending with a+\n")
    f.seek(0)
    print("A+ READ:\n", f.read())


# ===============================
# 🔥 BINARY MODE
# ===============================

# Example: reading binary file (image)
try:
    with open("image.png", "rb") as f:
        data = f.read()
        print("Binary file read successful, size:", len(data))
except FileNotFoundError:
    print("Binary file not found")


# ===============================
# 🧠 IMPORTANT FUNCTIONS
# ===============================

with open("file.txt", "r") as f:
    print("read() ->", f.read())        # reads full file

with open("file.txt", "r") as f:
    print("readline() ->", f.readline())  # reads one line

with open("file.txt", "r") as f:
    print("readlines() ->", f.readlines())  # list of lines


# ===============================
# 🧠 POINTER CONTROL
# ===============================

with open("file.txt", "r") as f:
    print("First read:", f.read(5))  # read first 5 chars
    f.seek(0)                       # move pointer to start
    print("After seek:", f.read(5))


# DELETE A File
import os
os.remove("sample.txt")


# ===============================
# 🚀 BEST PRACTICE
# ===============================

# Always use 'with' → auto closes file
with open("file.txt", "r") as f:
    data = f.read()



# ===============================
# 📊 QUICK SUMMARY
# ===============================

"""
Mode   Delete Data   Create File   Read   Write
----------------------------------------------
r      ❌            ❌            ✔️     ❌
w      ✔️            ✔️            ❌     ✔️
a      ❌            ✔️            ❌     ✔️
r+     ❌            ❌            ✔️     ✔️
w+     ✔️            ✔️            ✔️     ✔️
a+     ❌            ✔️            ✔️     ✔️

"""

# ===============================
# ✅ END
# ===============================