import sys

name = ""
names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

if len(names) == 1:
    final = f"to {names[0]}"
elif len(names) == 2:
    final = f"to {names[0]} and {names[1]}"
else:
    final = "to " + ", ".join(names[:-1]) + f", and {names[-1]}"

print("Adieu, adieu,", final)
