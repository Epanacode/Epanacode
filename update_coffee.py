import re
import datetime

path = "README.md"

with open(path, "r+", encoding="utf-8") as f:
    text = f.read()
    match = re.search(r"☕ (\d+)", text)
    if match:
        new_number = int(match.group(1)) + 1
        new_text = re.sub(r"☕ \d+", f"☕ {new_number}", text)
        f.seek(0)
        f.write(new_text)
        f.truncate()
        print(f"Updated coffee count to {new_number}")
    else:
        print("No coffee counter found in README.")
