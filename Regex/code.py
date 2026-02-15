import re

def main():
    code = input("Hexadecimal color code: ")

    pattern = r"^#[a-fA-F0-9]{6}$"

    match = re.search(code, pattern)

    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")
