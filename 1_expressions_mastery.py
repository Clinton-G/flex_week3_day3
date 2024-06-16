import re


text = "Contact emails are: john.doe@example.com and Jane.Doe@example.com."
emails = re.findall(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", text, re.IGNORECASE)
print(emails)

