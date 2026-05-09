# ===============================
# 🔥 JSON MODULE (FULL GUIDE)
# ===============================

"""
json.loads() → JSON string ➝ Python object
json.dumps() → Python object ➝ JSON string

json.load()  → JSON file ➝ Python object
json.dump()  → Python object ➝ JSON file
"""

import json


# ===============================
# 🔥 1. JSON STRING → PYTHON (loads)
# ===============================

json_str = '{"name": "Shradha", "isTeacher": true}'

py_obj = json.loads(json_str)

print("loads() output:", type(py_obj), py_obj)
# Output: dict


# ===============================
# 🔥 2. PYTHON → JSON STRING (dumps)
# ===============================

py_obj = {
    "name": "Shradha",
    "isTeacher": None   # Python None → JSON null
}

json_str = json.dumps(py_obj)

print("dumps() output:", type(json_str), json_str)
# Output: str


# ===============================
# 🔥 3. PYTHON → JSON FILE (dump)
# ===============================

data = {
    "name": "Shradha",
    "age": 27,
    "isTeacher": True
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)

# indent=4 → pretty format
# sort_keys=True → sorts keys alphabetically


# ===============================
# 🔥 4. JSON FILE → PYTHON (load)
# ===============================

with open("data.json", "r") as f:
    data = json.load(f)

print("load() output:", type(data), data)


# ===============================
# 🧠 IMPORTANT NOTES
# ===============================

"""
Python ↔ JSON mapping:

Python        JSON
-------------------------
dict     ↔    object
list     ↔    array
str      ↔    string
int/float↔    number
True     ↔    true
False    ↔    false
None     ↔    null

Key differences:
- JSON uses true/false/null (lowercase)
- Python uses True/False/None (uppercase)

Common mistakes:
❌ Using True in JSON string → error
✔ Use true inside JSON string

❌ Forgetting quotes in JSON keys
✔ Keys must be in double quotes

Best practice:
✔ Always use json.dump/load with files
✔ Use indent for readability
"""