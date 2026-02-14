import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", "", re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))
