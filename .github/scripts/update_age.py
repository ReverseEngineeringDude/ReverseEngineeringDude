from datetime import date
import re

# 🎂 Replace with your real birthdate
BIRTH_YEAR = 2003
BIRTH_MONTH = 12
BIRTH_DAY = 3

today = date.today()
# Adjust age if birthday hasn't occurred yet this year
age = today.year - BIRTH_YEAR - ((today.month, today.day) < (BIRTH_MONTH, BIRTH_DAY))

# Read README
with open("README.md", "r") as f:
    content = f.read()

# Replace {{AGE}} with calculated age
new_content = re.sub(r"\{\{AGE\}\}", str(age), content)

# Save back to README
with open("README.md", "w") as f:
    f.write(new_content)
