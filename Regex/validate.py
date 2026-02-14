import re

email = input("What's your email? ").strip()

#if "@" in email:
#    print("Valid")
#else:
#    print("Invalid")

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")
else:
    print("Invalid")
