import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

occupation = re.search(r'Occupation:\s*(.*?);', text)

if occupation:
    print("Occupation:", occupation.group(1))
else:
    print("Occupation Not Found.")
