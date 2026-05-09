data = True
line = 1
word = "Python"

with open("sample.txt", "r") as f:
    while data:
        data = f.readline()

        if (word in data):
            print(f"{word} found at line {line}")
            break

        line += 1  

######   ORR

word = "Python"

with open("sample.txt", "r") as f:
    for line_no, line in enumerate(f, start=1):
        if word in line:
            print(f"{word} found at line {line_no}")
            break